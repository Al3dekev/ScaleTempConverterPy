

class UserCallConverter:

    # Default values added for Py reasons.
    def __init__(self):
        self.SelNum = 1
        self.SelScaleF = "C"
        self.selScaleT = "F"


    def selectNumToConvert(self):
        self.setSelNum(input("What's the Number you'd want to convert?"))
        return self.getSelNum()

    def selectScaleFrom(self):
        self.setSelScaleF(input("What Scale this number is from?[°C/°F/K] "))
        return self.getSelScaleF()

    def selectScaleTo(self):
        self.setselScaleT(input("What will be the new Scale?[°C/°F/K] "))
        return self.getselScaleT()



    def getSelNum(self):
        return self.SelNum

    def setSelNum(self, sett):
        self.SelNum = sett

    def getSelScaleF(self):
        return self.SelScaleF

    def setSelScaleF(self, sett):
        self.SelScaleF = sett

    def getselScaleT(self):
        return self.selScaleT

    def setselScaleT(self, sett):
        self.selScaleT = sett