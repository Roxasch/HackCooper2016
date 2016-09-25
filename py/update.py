#!/usr/bin/env python2
from stack_overflow import do_routine
from make_project import createNewProblem

x = do_routine(1)

for i in range(len(x)):
	code, output = x[i]
        try:
            createNewProblem("StackOverflow"+str(i), output, code, "py")
        except UnicodeDecodeError:
            pass

