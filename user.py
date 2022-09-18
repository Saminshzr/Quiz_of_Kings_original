import json


class User:
    userName = ""
    password = ""
    reals2 = 0
    realS = 0
    score = 0
    Dict = dict()
    lst = []
    index = int()
    new_dict = {}

    def __init__(self, userName):
        self.userName = userName
        with open('quiz_list.json') as json_file:
            self.Dict = json.load(json_file)
            self.lst = self.Dict['users']

    def check_this_user(self):
        f = False
        Username_temp = self.userName
        num = len(self.lst)
        for i in range(0, num):
            if Username_temp == self.lst[i]['id']:
                self.index = i
                f = True
                break
        return f

    def signIn(self, password):
        f = False
        if password == self.lst[self.index]['password']:
            f = True
        else:
            f = False

        if f is True:
            self.score = self.lst[self.index]['score']
            self.score = int(self.score)
        return f

    def signUp(self, newUsername, NewPass):
        self.newUsername = newUsername
        self.NewPass = NewPass
        num = len(self.lst)
        num = int(num)
        f = True
        for j in range(0, num):
            if newUsername == self.lst[j]['id']:
                f = True
                print(f"{newUsername} is Valid")
                break
            else:
                f = False
        if f is False:
            self.new_dict = {'id': self.newUsername, 'password': self.NewPass, 'score': "0"}
            self.lst.append(self.new_dict)
            self.index += 1
            self.userName = newUsername

    def getScore(self, score1):
        self.score1 = score1
        score_total = self.score + self.score1

        print("---- " * 15)
        print("your score was: ", self.score)
        print("now your score is", score_total)
        print("---- " * 15)

        score_total = str(score_total)
        self.lst[self.index]['score'] = score_total

    def Update_file(self):
        self.Dict["users"] = self.lst
        self.Dict = json.dumps(self.Dict, sort_keys=True, indent=4)

        with open('quiz_list.json', 'w') as json_file:
            json_file.write(self.Dict)
