from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Session


SQLALCHEMY_DATABASE_URL = "sqlite:///./wardrobe.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class DBClothingItem(Base):
    __tablename__ = "clothes"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    category = Column(String)
    color = Column(String)
    formality = Column(String)
    season = Column(String)


Base.metadata.create_all(bind=engine)

app = FastAPI()

class ClothingItemCreate(BaseModel):
    name: str
    category: str
    color: str
    formality: str
    season: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/add_item")
def add_clothing_item(item: ClothingItemCreate, db: Session = Depends(get_db)):
    
    new_db_item = DBClothingItem(
        name=item.name,
        category=item.category,
        color=item.color,
        formality=item.formality,
        season=item.season
    )
  
    db.add(new_db_item)
    db.commit()
    db.refresh(new_db_item)
    
    return {"message": f"Successfully added '{new_db_item.name}' to your permanent database!", "item_id": new_db_item.id}

@app.get("/wardrobe")
def view_all_clothes(db: Session = Depends(get_db)):
   
    all_clothes = db.query(DBClothingItem).all()
    return {"total_items": len(all_clothes), "wardrobe": all_clothes}
