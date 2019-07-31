set zipName="ScaleTempConverterPy"
set verNum = "0.1.0"
set completeName = %zipName% - %verNum%

set /p newversion="[NUMERO NOUVELLE VERSION POUR TITRE RELEASE]: "

hub release create -o -a "LATEST: %zipName%" - m %verNum% Main