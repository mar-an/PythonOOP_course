import random

class Account():
    def __init__(self):
        self.my_dict = {}

    def newAccount(self):
        print("Type your new login:")
        self.login = input()
        print("Type your deposit:")
        self.deposit = input()
        return ([self.login, self.deposit])

    def createAccount(self, accountdata):
        self.accountdata = accountdata
        self.accountID = random.randint(10000,99999)
        self.my_dict[self.login] = [self.accountID, self.deposit]
        print ("Your accont ID is: {}".format(self.accountID))
        print (self.my_dict[self.login])

    def loginTo(self):
        print("Type your login:")
        self.login = input()
        print("Type your accountID:")
        self.id = input()
        return ([self.login, self.id])

    def verifyUser(self, logindata):
        self.logindata = logindata
        if logindata[0] in self.my_dict.keys():
            if int(logindata[1]) == int(self.my_dict[logindata[0]][0]):
                print ("login {} and account {} exsist".format(logindata[0], logindata[1] ))
                print("You are in login to your account!!!")
            else:
                print("login {} and account {} not exsist".format(logindata[0], logindata[1]))
        else:
            print("login {} not exsist".format(logindata[0]))


account = Account()


while True:
    print()
    print("___Option list, type number 1..4___")
    print("1: new Account")
    print("2: login")
    print("4: exit")

    userChoice = int(input())

    if (userChoice == 1):
        accountData = account.newAccount()
        account.createAccount(accountData)
    elif (userChoice == 2):
        loginData = account.loginTo()
        account.verifyUser(loginData)
    elif (userChoice == 4):
        quit()

