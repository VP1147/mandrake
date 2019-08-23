# # -*- encoding: utf-8 -*-
# JSON functions lib for Mandrake

# External libs
import json

import utils, shared

#def SetMaxMin(MaxMinDict,SettingsMenu):
#    with open('settings.json','w') as ToDump:
#        json.dump(MaxMinDict,ToDump, indent=4)
#    return SettingsMenu()

# def ReadMaxMin(): # Exec at start
#    with open('settings.json','r') as ToRead:
#        MaxMin = json.load(ToRead)
#    shared.IntMin = int(MaxMin.get("min"))
#    shared.IntMax = int(MaxMin.get("max"))

def SaveAllFromCfg(SettingsMenu):
    DictAll = {"IntMin": shared.IntMin, "IntMax": shared.IntMax, "FloatPrec": shared.FloatPrec}
    with open('settings.json','w') as ToSave:
        json.dump(DictAll, ToSave, indent=4)
    return SettingsMenu()

def ReadJson(Str,Path): # Recebe local do .json e nome; retorna valor corresp. 
    data = json.loads(open(Path).read())
    return data[Str]
