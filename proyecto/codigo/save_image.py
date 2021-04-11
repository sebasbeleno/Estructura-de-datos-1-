# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 21:54:54 2021

@author: Beleño
"""
import numpy as np
from PIL import Image
import os

def save_image(image_data, method, name):
    
    image_name = '{}-{}.png'.format(name, method)
    csv_name = '{}-{}.csv'.format(name, method)
        
    py = len(image_data[0])
    px = len(image_data)

    print(image_name)
        
    pixels = np.array(image_data, dtype='uint8')
    pixels = pixels.reshape((px, py))
    
    path = create_directory(name)
    image_path = os.path.join(path, image_name)
    csv_path = os.path.join(path, csv_name)

    image = Image.fromarray(pixels)
    image.save(image_path)
    


    #np.savetxt(csv_path, pixels, fmt='%5.0f', delimiter=",")

    #print("Se guardó la imagen: " + image_name)

    pass

def create_directory(directory_name):

    os.chdir("D:/Universidad/ST0245-001")
    absolute_path = os.getcwd()


    path = os.path.join(absolute_path, "proyecto", "images", directory_name)

    if not os.path.exists(path):
        try:
            os.mkdir(path)
        except OSError as error:
            print ("Creation of the directory %s failed" % path, error)
   
    return path