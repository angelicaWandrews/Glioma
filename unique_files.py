#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 08:16:38 2019

@author: mlab
"""

import os
from PIL import Image 
import pandas as pd


folder_images = "/media/mlab/Samsung USB/high_fixed/"
folder_images1= "/media/mlab/Samsung USB/low_fixed/"
#size_images = dict()
size_images_h = []
size_images_w = []

def find_file_size(folder_images, size_images_h,size_images_w):
    for dirpath, _, filenames in os.walk(folder_images):
        for path_image in filenames:
            image = os.path.abspath(os.path.join(dirpath, path_image))
            with Image.open(image) as img:
                width, height = img.size
                size_images_h.append(height)
                size_images_w.append(width)
                
    return(pd.DataFrame({'width': size_images_w,'height':size_images_h}))
#            size_images[path_image] = {'width': width, 'heigth': heigth}
    


size_images_high = find_file_size(folder_images, size_images_h, size_images_w)
size_images_low = find_file_size(folder_images1, size_images_h, size_images_w)

print(size_images_high.drop_duplicates())

print(size_images_low.drop_duplicates())

def compare_two_df(df1,df2):
    df = pd.concat([df1, df2]) # concat dataframes
    df = df.reset_index(drop=True) # reset the index
    df_gpby = df.groupby(list(df.columns)) #group by
    idx = [x[0] for x in df_gpby.groups.values() if len(x) == 1] #reindex
    return(df.reindex(idx))


test = compare_two_df(size_images_high,size_images_low)
print(test)