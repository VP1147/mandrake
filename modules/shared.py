# Objects visible for all modules
import json as j

with open('./data/settings.json','r') as r:
	d = j.load(r)
IntMin = int(d.get("IntMin"))
IntMax = int(d.get("IntMax"))
FloatPrec = int(d.get("FloatPrec"))
RCount = int(d.get("RCount"))

GameLogoPath = './data/logotypes/ModeLogo/'
LogoPath = './data/logotypes/'
