# -*-coding: utf-8 -
'''
    @author: MD. Nazmuddoha Ansary
'''
#--------------------
# imports
#--------------------
import os
import random
import cv2
import numpy as np
import math
import PIL.Image,PIL.ImageDraw,PIL.ImageFont


#--------------------
# helper
#--------------------
def stripPads(arr,val):
    '''
        strip specific values
    '''
    arr=arr[~np.all(arr == val, axis=1)]
    arr=arr[:, ~np.all(arr == val, axis=0)]
    return arr

def getImageData(data):
    '''
        extracts the binary image data for a given string 
    '''
    # constants
    HEIGHT = 1024
    WIDTH = 1024
    data_dim=128
    # create an image
    image = PIL.Image.new('RGB', (WIDTH, HEIGHT))
    draw = PIL.ImageDraw.Draw(image)
    myfont = PIL.ImageFont.truetype('resources/font.ttf',data_dim)
    w, h = draw.textsize(data, font=myfont)
    draw.text(((WIDTH - w) / 2,(HEIGHT - h) / 2), data, font=myfont)
    
    image=image.convert('L')

    image=np.array(image)
    image[image <= 128]=0
    image[image > 128]=255
    
    image=stripPads(image,0)
    return image

