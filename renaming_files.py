#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 07:54:22 2019

@author: mlab
"""

# Pythono3 code to rename multiple  
# files in a directory or folder 
  
# importing os module 
import os 
  
# Function to rename multiple files 
def main(): 
    i = 0
      
    for filename in os.listdir("/media/mlab/Samsung USB/brats/"): 
        dst ="Low" + str(i) + ".dcm"
        src ='/media/mlab/Samsung USB/brats/'+ filename 
        dst ='/media/mlab/Samsung USB/brats/'+ dst 
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
        i += 1
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 