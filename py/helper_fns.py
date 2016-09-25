import json
from sys import *
import subprocess
from os import path
from constants import *

def getProblem(prob):
     if (not path.isdir(datadir+"/"+prob)):
         raise Exception("Problem not found:" + prob)

     if (not path.isfile(datadir+"/"+prob+"/"+prob+".json")):
         raise Exception("Problem not found:" + prob)

     with open(datadir+"/"+prob+"/"+prob+".json") as data:
         return json.load(data)

def runProblemJson(prob_name, code):
    prob = getProblem(prob_name)

    with open(exfile, 'w+') as exfile_instance:
        exfile_instance.write(code)

    return runProblemFile(prob)

def runProblemFile(info):

    output = ""
    try:
        output = subprocess.check_output([exfile])
    except subprocess.CalledProcessError:
        output = "Process returned non-zero"

    ret = ""
    if (output == info['output']):
        ret += "Success!"
    else:
        ret += "Failure!"

    ret += "\n\nCode output:\n\n"
    ret += output

    # TODO Return a comparison of output to the expected output
    return ret
