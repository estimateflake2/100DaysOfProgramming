#========================== Creating Classes
#========================== Final Project: Quiz Game
# PscalCase, camelCase, snake_case
from questions_class import Questions
from user_score import User

q = Questions()
usr = User()
correct_ans = 0
total_questions = 0
done = False
while not done:
    curr_question = q.get_question()
    response = input (f"Q.{total_questions+1}: {curr_question[1]["question"]} (True/False): ")

    if response in ["True","true",'t','False','false','f'] :
        if (response in ["True","true",'t'] and curr_question[1]["answer"] == "True") or(response in ['False','false','f'] and curr_question[1]["answer"] == "False") :
            total_questions += 1
            correct_ans += 1
            print ("You got the right answer!")
        else:
            total_questions += 1
            print (f"That's wrong, the correct answer is: {curr_question[1]["answer"]} ")
    elif response == "exit":
        done = True
    else:
        print ("Invalid Input. Please try again.")
    usr.current_score = correct_ans
    usr.total_questions = total_questions
    print (f"Your current score is: {usr.current_score}/{usr.total_questions}\n\n")
