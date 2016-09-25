import json
from sys import *
import os
from constants import *


def createNewProblem(name, output, code, lang, views=0, upvotes=0,
                     dnvotes=0, correct=0, incorrect=0, tags=[]):

    if not os.path.exists(datadir+"/"+name):
            os.makedirs(datadir+"/"+name)

    with open(datadir+"/"+name+"/"+name+".json", 'w+') as f:
        json_data = {'name': name,
                     'output': output, # text output by the program
                     'code': code,
                     'lang': lang,
                     'views': views,
                     'upvotes': upvotes,
                     'dnvotes': dnvotes,
                     'correct': correct,
                     'incorrect': incorrect,
                     'tags': tags
                    }

        json.dump(json_data, f)
