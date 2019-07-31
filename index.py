
from Beginning import *
from CelsiusScale import *
from FahrenheitScale import *

from UserCallConverter import *
from UniversalConverter import UniversalConverter
from ScaleUniversalDatas import *

# scaleNumberInProg = 2

Beg = Beginning()
Beg.welcome()
Beg.explanations()

UCC = UserCallConverter()

UCC.selectNumToConvert()
UCC.selectScaleFrom()
UCC.selectScaleTo()

UC = UniversalConverter(UCC.getSelNum(), UCC.getSelScaleF(), UCC.getselScaleT())

for el in scaleList:

    # From
    if el.get("ScaleSymbol") == "C" and el.get("ScaleSymbol") == UCC.getSelScaleF():
        for ele in scaleList:
            # To
            if ele.get("ScaleSymbol") == "F" and ele.get("ScaleSymbol") == UCC.getselScaleT():
                UC.convertCtoF()
            if ele.get("ScaleSymbol") == "K" and ele.get("ScaleSymbol") == UCC.getselScaleT():
                UC.convertCtoK()
    if el.get("ScaleSymbol") == "F" and el.get("ScaleSymbol") == UCC.getSelScaleF():
        for ele in scaleList:
            # To
            if ele.get("ScaleSymbol") == "C" and ele.get("ScaleSymbol") == UCC.getselScaleT():
                UC.convertFtoC()
            if ele.get("ScaleSymbol") == "K" and ele.get("ScaleSymbol") == UCC.getselScaleT():
                UC.convertFtoK()
    if el.get("ScaleSymbol") == "K" and el.get("ScaleSymbol") == UCC.getSelScaleF():
        for ele in scaleList:
            # To
            if ele.get("ScaleSymbol") == "C" and ele.get("ScaleSymbol") == UCC.getselScaleT():
                UC.convertKtoC()
            if ele.get("ScaleSymbol") == "F" and ele.get("ScaleSymbol") == UCC.getselScaleT():
                UC.convertKtoF()

# End for loop

while 1:
    lett = input("Press q to exit program")
    if lett == "q":
        exit()
        break