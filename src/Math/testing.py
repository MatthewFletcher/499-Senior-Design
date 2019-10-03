#!/usr/bin/env python3

import CSV_Wizard as c
import numpy as np
import Stats_Wizard as s
import pandas as pd


df = c.openFile("../../TestData/sathead.csv")[0]

r = s.Regression(df)

ds = s.Statistics(df['high_GPA'])



