import json
from sys import *
import subprocess
from os import path

rootdir="/home/ubuntu/hackCooper/educode/"

def getProblem(prob):
     if (not path.isdir(rootdir+"/data/"+prob)):
         raise Exception("Problem not found:" + prob)

     if (not path.isfile(rootdir+"/data/"+prob+"/"+prob+".json")):
         raise Exception("Problem not found:" + prob)

     with open(rootdir+"/data/"+prob+"/"+prob+".json") as data:
         return json.load(data)

def runProblemJson(prob_name, code):
    prob = getProblem(prob_name)

    with open(rootdir+"exfile", 'w+') as exfile:
        exfile.write(code)

    return runProblemFile(prob)


def runProblemFile(info):

    output = ""
    try:
        output = subprocess.check_output([rootdir + "exfile"])
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
