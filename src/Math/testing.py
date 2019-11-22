#!/usr/bin/env python3

import sys, os
from pathlib import Path
sys.path.append(str(Path(os.getcwd()).joinpath("../csvtools").resolve()))
import CSV_Wizard as c
import numpy as np
import Stats_Wizard as sw
import pandas as pd
import matplotlib.pyplot as plt 
import sys
import inspect


mydata = c.openFile("../../TestData/sat.csv")[0]

df = sw.Regression(mydata)
ds = sw.Statistics(mydata['high_GPA'])

for _, test in [m for m in inspect.getmembers(sw) if m[0].startswith("s_")]:
    temp = test(ds.d)
    print(f"Test: {temp.name}\nResult: {temp.func()}\n")

rr = sw.Regression(df.df)
for _, test in [m for m in inspect.getmembers(sw) if m[0].startswith("r_")]:
    temp = test(rr.df)
    print(f"Test: {temp.name}\nResult: {temp.func()}\n")
