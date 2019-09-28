# Objects visible for all modules
import json, sys

with open('./data/settings.json','r') as ReadAll:
	DictAll = json.load(ReadAll)
IntMin = int(DictAll.get("IntMin"))
IntMax = int(DictAll.get("IntMax"))
FloatPrec = int(DictAll.get("FloatPrec"))
RCount = int(DictAll.get("RCount"))

GameLogoPath = './data/logotypes/ModeLogo/'
LogoPath = './data/logotypes/'
