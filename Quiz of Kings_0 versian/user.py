class User:
    userName = ""
    password = ""
    reals2 = 0
    realS = 0
    score = 0
    lst = []

    def __init__(self, username):
        self.userName = username
        with open('quiz_list.txt', 'r') as f:
            self.lst = f.readlines()

    def checkThisUser(self):
        Username_temp = self.userName + '\n'
        if Username_temp in self.lst:
            return True
        else:
            return False

    def signIn(self, password):

        Username_temp = self.userName + '\n'
        if Username_temp in self.lst:
            realPass = self.lst.index(Username_temp) + 1
            password_temp = password + '\n'
            if self.lst[realPass] == password_temp:
                self.realS = realPass + 1
                self.score = int(self.lst[self.realS])
                return True
            else:
                return False

    def signUp(self, newUsername, NewPass):
        new_user = newUsername + '\n'
        if new_user not in self.lst:
            self.lst.append(new_user)
            password_new = NewPass
            password_new = password_new + '\n'
            self.lst.append(password_new)
            self.reals2 = self.lst.index(password_new) + 1
            s = str(0) + '\n'
            self.lst.append(s)
            self.userName = newUsername
        return True

    def getScore(self, score1):
        self.score1 = score1
        scoreTotal = self.score + self.score1

        print("----"*15)
        print("your score was: ", self.score)
        print("now your score is", scoreTotal)
        print("----"*15)

        scoreTotal = str(scoreTotal)
        if self.realS == 0:
            self.lst[self.reals2] = scoreTotal + '\n'
        else:
            self.lst[self.realS] = scoreTotal + '\n'
        return self.score

    def Update_file(self):
        with open('quiz_list.txt', 'w') as f:
            for i in self.lst:
                x = i.strip()
                f.write(i)

