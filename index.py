
from Beginning import *
from CelsiusScale import *
from FahrenheitScale import *

from UserCallConverter import *
from UniversalConverter import UniversalConverter
from ScaleUniversalDatas import *

#scaleNumberInProg = 2

Beg = Beginning()
Beg.welcome()
Beg.explanations()

UCC = UserCallConverter()

UCC.selectNumToConvert()
UCC.selectScaleFrom()
UCC.selectScaleTo()

UC = UniversalConverter()

for el in scaleList:
    # if el.get("ScaleSymbol") == UCC.getSelScaleF():
    #     for ele in scaleList:
    #         if ele.get("ScaleSymbol") == UCC.getselScaleT():

    # From
    if el.get("ScaleSymbol") == "C":
        for ele in scaleList:
            # To
            if ele.get("ScaleSymbol") == "F":
                UC.convertCtoF()
            if ele.get("ScaleSymbol") == "K":
                UC.convertCtoK()
    if el.get("ScaleSymbol") == "F":
        for ele in scaleList:
            # To
            if ele.get("ScaleSymbol") == "C":
                UC.convertFtoC()
            if ele.get("ScaleSymbol") == "K":
                UC.convertFtoK()
    if el.get("ScaleSymbol") == "K":
        for ele in scaleList:
            # To
            if ele.get("ScaleSymbol") == "C":
                UC.convertKtoC()
            if ele.get("ScaleSymbol") == "F":
                UC.convertKtoF()

# End for loop