#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
ROWS = 220  
COLS =  255
fin = open("/Users/abelng/Desktop/2021fall/CS688 Web Analy & Mining/Homework 3/Bug Final.png")
print(fin)


# In[9]:


# Loading the input image
print("... Load input image")
img = np.fromfile(fin, dtype = np.uint8, count = ROWS * COLS)
print("Dimension of the old image array: ", img.ndim)
print("Size of the old image array: ", img.size)


# In[10]:


# Conversion from 1D to 2D array
img.shape = (img.size // COLS, COLS)
print("New dimension of the array:", img.ndim)
print("----------------------------------------------------")
print(" The 2D array of the original image is: \n", img)
print("----------------------------------------------------")
print("The shape of the original image array is: ", img.shape)


# In[12]:


# Save the output image
print("... Save the output image")
img.astype('int8').tofile('NewImage.raw')
print("... File successfully saved")
# Closing the file
fin.close()


# In[ ]:




