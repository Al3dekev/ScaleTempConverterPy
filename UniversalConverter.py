

class UniversalConverter:

    def __init__(self, number, FromScale, ToScale):
        self.number = int(number)
        self.FromScale = FromScale
        self.ToScale = ToScale


    # From C
    def convertCtoF(self):
        r = (self.number * 9 / 5) + 32
        return print(str(self.number)+" °"+self.FromScale+" have been converted into "+str(r)+" °"+self.ToScale)

    def convertCtoK(self):
        r = self.number + 273.15
        return print(str(self.number)+" °"+self.FromScale+" have been converted into "+str(r)+" °"+self.ToScale)
    # End - From C

    # From F
    def convertFtoC(self):
        r = (self.number-32)*5/9
        return print(str(self.number)+" °"+self.FromScale+" have been converted into "+str(r)+" °"+self.ToScale)

    def convertFtoK(self):
        r = (self.number-32)*5/9 + 273.15
        return print(str(self.number)+" °"+self.FromScale+" have been converted into "+str(r)+" °"+self.ToScale)
    # End - From F

    # From K
    def convertKtoC(self):
        r = self.number - 273.15
        return print(str(self.number)+" °"+self.FromScale+" have been converted into "+str(r)+" °"+self.ToScale)

    def convertKtoF(self):
        r = (self.number-273.15)*9/5 + 32
        return print(str(self.number)+" °"+self.FromScale+" have been converted into "+str(r)+" °"+self.ToScale)
    # End - From K