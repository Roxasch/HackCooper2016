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

def overwriteProblem(problem, data):
    with open(datadir+"/"+name+"/"+name+".json", "w+") as f:
        json.dump(data, f)

# SETTERS
def upVote(problem):
    data = getProblem(problem)
    data['upvotes'] += 1
    overwriteProblem(problem, data)

def dnVote(problem):
    data = getProblem(problem)
    data['dnvotes'] += 1
    overwriteProblem(problem, data)

def addView(problem):
    data = getProblem(problem)
    data['views'] += 1
    overwriteProblem(problem, data)

def addCorrect(problem):
    data = getProblem(problem)
    data['correct'] += 1
    overwriteProblem(problem, data)

def addIncorrect(problem):
    data = getProblem(problem)
    data['incorrect'] += 1
    overwriteProblem(problem, data)

def addTag(problem, tag):
    data = getProblem(problem)
    data['tags'].append(tag)
    overwriteProblem(problem, data)


# GETTERS
def getIncorrectCode(problem):
    data = getProblem(problem)
    return data['code']

def getCorrectOutput(problem):
    data = getProblem(problem)
    return data['output']

def getLanguage(problem):
    data = getProblem(problem)
    return data['lang']

def getViews(problem):
    data = getProblem(problem)
    return str(data['views'])

def getUpvotes(problem):
    data = getProblem(problem)
    return str(data['upvotes'])

def getDnvotes(problem):
    data = getProblem(problem)
    return str(data['dnvotes'])

def getNetVotes(problem):
    data = getProblem(problem)
    return str(data['dnvotes'] - data['dnvotes'])

def getCorrect(problem):
    data = getProblem(problem)
    return str(data['correct'])

def getIncorrect(problem):
    data = getProblem(problem)
    return str(data['incorrect'])

def getTags(problem):
    data = getProblem(problem)
    return str(data['tags'])
