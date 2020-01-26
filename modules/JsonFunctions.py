# # -*- encoding: utf-8 -*-
# JSON functions lib for Mandrake

# External libs
import json as j

import utils as u
import shared as s

def SaveAllFromCfg(SettingsMenu):
	Path = './data/settings.json'
	DictAll = {"IntMin": s.IntMin, "IntMax": s.IntMax, "FloatPrec": s.FloatPrec, "RCount": s.RCount}
	with open(Path,'w') as ToSave:
		j.dump(DictAll, ToSave, indent=4)
	return 0

def ReadJson(Str,Path): # Recebe local do .json e nome; retorna valor corresp. 
    data = j.loads(open(Path).read())
    return data[Str]
