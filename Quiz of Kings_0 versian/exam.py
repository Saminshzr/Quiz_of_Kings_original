import uuid
import requests
import random
import html


class Exam:
    def __init__(self, name):
        self.name = name

    def subject(self):
        sublist = ["Science Math", "Science Computer", "Animals", "Others"]
        print("TYPE YOUR SUBJECT THAT YOU WANT TO PLAY: ")
        for i in range(0, len(sublist)):
            print(i + 1, "- ", sublist[i])
        sub = int(input()) - 1
        if sub == 0:
            print("you choose science math")
            return sub
        elif sub == 1:
            print("you choose science computer")
            return sub
        elif sub == 2:
            print("you choose animals")
            return sub
        else:
            print("you choose Others, and quiz will be about anything")
            return sub

    def show_exam(self, information):

        questions = (information['results'][0]['question'])
        print(html.unescape(questions))

        answers = information['results'][0]['incorrect_answers']
        correct_answer = information['results'][0]['correct_answer']
        answers.append(correct_answer)

        random.shuffle(answers)
        for i in range(0, len(answers)):
            print(i + 1, "- ", html.unescape(answers[i]))

        return correct_answer, answers

    def check_answers(self, score1):
        print("Nice job, You Got that")
        score1 += 1
        exit_game = input("if you want to exit enter 'quit' or enter if you want to continue: ")
        return score1, exit_game

    def check_Fanswers(self, user_answer, correct_answer):
        print(user_answer, " is INCORRECT\nthe correct answer was ", correct_answer)
        exit_game = input("if you want to exit enter 'quit' or enter if you want to continue: ")
        return exit_game

    def get_subjects(self, b):
        if b == 0:
            r = requests.get("https://opentdb.com/api.php?amount=1&category=19")
            return r
        elif b == 1:
            r = requests.get("https://opentdb.com/api.php?amount=1&category=18")
            return r
        elif b == 2:
            r = requests.get("https://opentdb.com/api.php?amount=1&category=27")
            return r
        else:
            r = requests.get("https://opentdb.com/api.php?amount=1")
            return r

    def status(self, r):
        status = r.status_code
        if status != 200:
            exit_game = input(
                "Sorry, some things went wrong please enter to reload or enter quit to quit this game\n").lower()
            return exit_game
