import json
import requests
from user import *
from exam import *


lst = []
score = 0
realS = 0
reals2 = 0
score1 = 0

userName = str(input("Enter your username: "))
user1 = User(userName)
flag = True
while flag is True:
    if user1.checkThisUser():

        password = str(input("Enter your password: "))
        signInRes = user1.signIn(password)

        if signInRes is True:
            print("----" * 15)
            print(f"Welcome to this game {userName}")
            print("----" * 15)
            break
        else:
            print("Incorrect password! if you want to continue enter y")
            if str(input()) == "y":
                continue

    else:
        print("This User is Not Exist So, Please SignUP")
        newUserName = str(input("Enter your new username: "))
        newPassword = str(input("Enter your new password: "))
        user1.signUp(newUserName, newPassword)
        continue

exit_game = ""
user = Exam(userName)
b = user.subject()
while exit_game != "quit":
    r = user.get_subjects(b)
    exit_game = user.status(r)

    information = json.loads(r.text)
    correct_answer, answers = user.show_exam(information)
    user_answer = input()
    try:
        user_answer = int(user_answer)
        if user_answer >= 5:
            user_answer = str(user_answer)
    except ValueError:
        user_answer = str(user_answer)

    if type(user_answer) == int and user_answer <= 4:
        if answers[user_answer - 1].lower() == correct_answer.lower():
                score1, exit_game = user.check_answers(score1)
        else:
                exit_game = user.check_Fanswers(answers[user_answer - 1], correct_answer)
    else:
        if user_answer.lower() == correct_answer.lower():
            score1, exit_game = user.check_answers(score1)
        else:
            exit_game = user.check_Fanswers(answers[user_answer - 1], correct_answer)


user1.getScore(score1)
user1.Update_file()
