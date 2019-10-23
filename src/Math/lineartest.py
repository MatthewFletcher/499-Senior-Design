#!/usr/bin/env python3

import CSV_Wizard as c
import numpy as np
import Stats_Wizard as s
import pandas as pd
import matplotlib.pyplot as plt 




df = c.openFile("../../TestData/linear.csv")[0]

r = s.Regression(df)
