# Objects visible for all modules
import json
with open('settings.json','r') as ReadAll:
    DictAll = json.load(ReadAll)
IntMin = int(DictAll.get("IntMin"))
IntMax = int(DictAll.get("IntMax"))
FloatPrec = int(DictAll.get("FloatPrec"))
Lang = str(DictAll.get("Lang"))
