#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 14:55:38 2019

@author: mlab
"""
#/home/mlab/Documents/brats_jpeg/224_by_224/high/

import os
import shutil
import numpy as np

base_dir="/home/mlab/Documents/brats_data"

sourceN = base_dir + "/train/high"
destN = base_dir + "/val/high"
sourceP = base_dir + "/train/low"
destP = base_dir + "/val/low"

filesN = os.listdir(sourceN)
filesP = os.listdir(sourceP)       



for f in filesN:
    if np.random.rand(1) < 0.2:
        shutil.move(sourceN + '/'+ f, destN + '/'+ f)

for i in filesP:
    if np.random.rand(1) < 0.2:
        shutil.move(sourceP + '/'+ i, destP + '/'+ i)

print(len(os.listdir(sourceN)))
print(len(os.listdir(sourceP)))
print(len(os.listdir(destN)))
print(len(os.listdir(destP)))