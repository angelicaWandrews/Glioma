#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 17:25:52 2019

@author: mlab
"""

import split_folders

# Split with a ratio.
# To only split into training and validation set, set a tuple to `ratio`, i.e, `(.8, .2)`.
split_folders.ratio('/home/mlab/Documents/totaldata', output="/home/mlab/Documents/totaldata_fixed", seed=1337, ratio=(.8, .1, .1)) # default values