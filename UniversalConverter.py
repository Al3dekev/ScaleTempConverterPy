

class UniversalConverter:

    def __init__(self, number, FromScale, ToScale):
        self.number = number
        self.FromScale = FromScale
        self.ToScale = ToScale


    # From C
    def convertCtoF(self):
        r = (self.FromScale*9/5) + 32
        return r

    def convertCtoK(self):
        r = self.FromScale + 273.15
        return r
    # End - From C

    # From F
    def convertFtoC(self):
        r = (self.FromScale-32)*5/9
        return r

    def convertFtoK(self):
        r = (self.FromScale-32)*5/9 + 273.15
        return r
    # End - From F

    # From K
    def convertKtoC(self):
        r = self.FromScale - 273.15
        return r

    def convertKtoF(self):
        r = (self.FromScale-273.15)*9/5 + 32
        return r
    # End - From K