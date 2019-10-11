#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 08:09:24 2019

@author: mlab
"""
     #only to convert   
import pydicom as dicom
import os
import cv2
import PIL # optional
# make it True if you want in PNG format
PNG = False
# Specify the .dcm folder path
folder_path = "/media/mlab/Samsung USB/brats_high/"
# Specify the output jpg/png folder path
jpg_folder_path = "/media/mlab/Samsung USB/high_fixed/"
images_path = os.listdir(folder_path)
for n, image in enumerate(images_path):
    ds = dicom.dcmread(os.path.join(folder_path, image))
    pixel_array_numpy = ds.pixel_array
    if PNG == False:
        image = image.replace('.dcm', '.jpg')
    else:
        image = image.replace('.dcm', '.png')
    cv2.imwrite(os.path.join(jpg_folder_path, image), pixel_array_numpy)
    if n % 50 == 0:
        print('{} image converted'.format(n))
        
#  #only to export patients info      
#import pydicom as dicom
#import os
#import PIL # optional
#import pandas as pd
#import csv
## list of attributes available in dicom image
## download this file from the given github link
#dicom_image_description = pd.read_csv("/media/mlab/Samsung USB/dicom_image_description.csv")
## Specify the .dcm folder path
#folder_path = "/media/mlab/Samsung USB/brats_high/"
#images_path = os.listdir(folder_path)
## Patient's information will be stored in working directory #'Patient_Detail.csv'
#with open('/media/mlab/Samsung USB/Patient_Detail_High.csv', 'w', newline ='') as csvfile:
#    fieldnames = list(dicom_image_description["Description"])
#    writer = csv.writer(csvfile, delimiter=',')
#    writer.writerow(fieldnames)
#    for n, image in enumerate(images_path):
#        ds = dicom.dcmread(os.path.join(folder_path, image))
#        rows = []
#        for field in fieldnames:
#            if ds.data_element(field) is None:
#                rows.append('')
#            else:
#                x = str(ds.data_element(field)).replace("'", "")
#                y = x.find(":")
#                x = x[y+2:]
#                rows.append(x)
#        writer.writerow(rows)