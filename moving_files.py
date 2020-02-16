#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 08:44:54 2019

@author: mlab
"""

#/home/mlab/Documents/brats_jpeg/high
#/home/mlab/Documents/brats_jpeg/low
#/media/mlab/Samsung USB/high_fixed
#/media/mlab/Samsung USB/low_fixed
#import os
#import shutil
#
#os.rename("/media/mlab/Samsung USB/high_fixed/", "/home/mlab/Documents/brats_jpeg/high")
#shutil.move("/media/mlab/Samsung USB/high_fixed/", "/home/mlab/Documents/brats_jpeg/high/")
#os.replace("/media/mlab/Samsung USB/high_fixed/", "/home/mlab/Documents/brats_jpeg/high")

import glob
import shutil
import os

src_dir = "/media/mlab/Samsung USB/low_fixed"
dst_dir = "/home/mlab/Documents/brats_jpeg/low"
for jpgfile in glob.iglob(os.path.join(src_dir, "*.jpg")):
    shutil.copy(jpgfile, dst_dir)