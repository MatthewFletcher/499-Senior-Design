import numpy
from subprocess import call 
import subprocess
import os 


FNULL = open(os.devnull, 'w')

f = 'mean.f'

call(['python3', '-m', 'numpy.f2py', '-c',f, '-m', 'mean'],
        stdout=FNULL,stderr=subprocess.STDOUT)

import mean

a = numpy.arange(10)
mean.mean(a)


