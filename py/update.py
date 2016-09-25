#!/usr/bin/env python2
from stack_overflow import *
from make_project import createNewProblem

#x = do_routine(2)
x = do_routine_oneshot('http://stackoverflow.com/questions/39687768/finding-variable-in-list')

for i in range(len(x)):
    code, output = x[i]
    try:
        createNewProblem("StackOverflowCorrect"+str(i), output, code, "py")
    except UnicodeDecodeError:
        pass
    except SyntaxError:
        pass
