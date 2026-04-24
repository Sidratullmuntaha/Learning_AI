import os
from dotenv import load_dotenv
from google import genai

# 1. Open the vault and load the secret key
load_dotenv()
my_api_key = os.getenv("GEMINI_API_KEY")

print("Vault opened successfully! Waking up the AI...")

# 2. Wake up the Gemini AI Client
client = genai.Client(api_key=my_api_key)

# 3. Prompt Engineering (Customized for you)
applicant_name = "Sidra Tull Muntaha"
education = "Bachelor of Computer Science"
job_title = "Junior AI Developer"
skills = "Python, Pandas, Machine Learning, FastAPI, Scikit-Learn"

print("Drafting your prompt...")
my_prompt = f"Write a short, powerful, and professional cover letter for {applicant_name}, a student studying {education}, applying for a {job_title} position. Highlight these specific skills: {skills}. Keep it under 3 paragraphs."

# 4. Send the prompt to the AI and wait for the response
print("Sending request to Google Gemini...")
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=my_prompt
)

# 5. Print the final result!
print("\n" + "="*50)
print("     YOUR AI GENERATED COVER LETTER")
print("="*50 + "\n")
# Print the final result to the terminal so we can see it
print(response.text)

# NEW: Save that exact text into a brand new file
file_path = "08_AI_Cover_Letter/my_cover_letter.txt"
with open(file_path, "w", encoding="utf-8") as file:
    file.write(response.text)

print(f"\n✅ Success! Your letter was also saved to: {file_path}")