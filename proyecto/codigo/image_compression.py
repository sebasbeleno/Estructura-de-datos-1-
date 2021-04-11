# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 21:59:24 2021

@author: Beleño
"""
import random
import numpy as np
from save_image import save_image
import math

"""
    Interpolación 
"""
def scaling(image_data):

    new_size_y = math.floor(len(image_data)/2) 
    new_size_x = math.floor(len(image_data[0])/2) 

    image_compressed = np.zeros((new_size_y, new_size_x))
    
    px = 0
    py = 0
    
    
    for y in range(0, len(image_data)-2, 2):
        
        px = 0
        
        for x in range(0, len(image_data[y])-2, 2):
            
            pixel_compresed = int((int(image_data[y][x]) + int(image_data[y][x+1]) + int(image_data[y+1][x])  + int(image_data[y+1][x+1] )) / 4 )            
            image_compressed[py][px] = pixel_compresed            
            
            px += 1
            
        py += 1
            
        
    return image_compressed

def average(image_data):

    size_y = math.floor(len(image_data))
    size_x = math.floor(len(image_data[0]))

    image_compressed = np.zeros((size_y, size_x)) 

    for y in range(0, size_y-1, 2):
        for x in range(0, size_x-1, 2):

            average_pixel =  int((int(image_data[y][x]) + int(image_data[y][x+1]) + int(image_data[y+1][x])  + int(image_data[y+1][x+1] )) / 4 )

            image_compressed[y][x] = average_pixel
            image_compressed[y][x+1] = average_pixel
            image_compressed[y+1][x] = average_pixel
            image_compressed[y+1][x+1] = average_pixel
    
    return image_compressed

def nearest_neighbors(image_data):
    
    size_y = math.floor(len(image_data))
    size_x = math.floor(len(image_data[0]))

    image_compressed = np.zeros((size_y, size_x))

    for y in range(0, size_y-2, 3):
        for x in range(0, size_x-2, 3):

            neighbor = int(image_data[y+1][x+1])


            image_compressed[y][x] = neighbor

            image_compressed[y][x+1] = neighbor
            image_compressed[y][x+2] = neighbor

            image_compressed[y+1][x] = neighbor
            image_compressed[y+2][x] = neighbor

            image_compressed[y+1][x+1] = neighbor

            image_compressed[y+1][x+2] = neighbor
            image_compressed[y+2][x+1] = neighbor

            image_compressed[y+2][x+2] = neighbor

    return image_compressed
    


