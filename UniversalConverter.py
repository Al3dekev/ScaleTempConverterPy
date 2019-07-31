

class UniversalConverter:

    def __init__(self, number, FromScale, ToScale):
        self.number = number
        self.FromScale = FromScale
        self.ToScale = ToScale



    def convertCtoF(self):
        result = (self.FromScale*9/5) + 32
        return result

    def convertFtoC(self):
        result = (self.FromScale-32)*5/9
        return result
