class Beginning:

    def __init__(self):
        self.AppName = "ScaleTempConverter"
        self.welcomeMsg = "Welcome to "+self.AppName+". Enjoy !"

    def welcome(self):
        print(self.getWelcomeMsg())

    def explanations(self):
        ex = "All you have to do is to follow the damn steps, CJ"
        print(ex)

    def getAppName(self):
        return self.AppName

    def setAppName(self, sett):
        self.AppName = sett

    def getWelcomeMsg(self):
        return self.welcomeMsg

    def SetWelcomeMsg(self, sett):
        self.welcomeMsg = sett

