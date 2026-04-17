def check_scores(scores_list):
    for score in scores_list:
        if score >= 10:
            print("Pass")
        else:
            print("Fail")

my_scores = [15, 8, 12]
check_scores(my_scores)