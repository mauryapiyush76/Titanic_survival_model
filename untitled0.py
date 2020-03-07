# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 23:02:21 2020

@author: maury
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

train= pd.read_csv("train.csv")
test= pd.read_csv("test.csv")

train.describe()


