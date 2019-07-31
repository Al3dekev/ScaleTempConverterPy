
from Beginning import *
from CelsiusScale import *
from FahrenheitScale import *

from UserCallConverter import *
from UniversalConverter import UniversalConverter

scaleNumberInProg = 2

Beg = Beginning()
Beg.welcome()
Beg.explanations()

UCC = UserCallConverter()

UCC.selectNumToConvert()
UCC.selectScaleFrom()
UCC.selectScaleTo()

x = 0

while(x <= scaleNumberInProg):
    x += 1

