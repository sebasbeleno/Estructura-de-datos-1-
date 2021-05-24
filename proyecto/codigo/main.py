import os 
import csv
from typing import Literal
from save_image import save_image
from image_compression import scaling, average, nearest_neighbors
from image_decompression import linear_interpolation
from lossless import lossless, dicompress
from save_compressed import save_compressed

"""
Put here you folder path
"""
path = "D:/Universidad/ST0245-Eafit/proyecto/datasets/archivosCSV"
        
os.chdir(path)

sizes = []


def reader():
    
    for root, subDirs, files in os.walk("."):
        
        """
        We read each folder saved in a CSV archive 
        """
        for subDir in subDirs:
            """
            For each subDirectory we create a path where we can save all the archives.
            Aditionally we change the path created in os for later reading if the CSV archives in it recorded.
            """
            new_path = path+'/'+subDir
            os.chdir(new_path)

            
            """
            We iterate the subDirectory previously mentioned and get the anrchives in it.
            """
            for a,b,c in os.walk("."):
                """
                For each archive found we create am absolute path for later reading.
                """
                os.chdir(new_path)

                for file_data in c:
                    os.chdir(new_path)
                    file_path = os.path.abspath(file_data)
                 
                    with open(file_path, 'r') as csv_file:
                        reader = csv.reader(csv_file, delimiter=",")
                        """
                        Once read the archive, we save it inside or data structure.
                        """
                        data = []
                        for row in reader:
                            data.append(row)
                            
                        filename = os.path.basename(file_path)
                        imagename = filename.split('.')[0]
                        
                            
                        save_image(data, "original", imagename)
                        
                        losslyImageCompressed = average(data)
                        losslyImageCompressed = losslyImageCompressed.tolist()
                        losslessImageCompressed = lossless(losslyImageCompressed)
                        save_compressed(losslessImageCompressed, "Burro", imagename)

                        losslessImageCompressed = eval(losslessImageCompressed)
                        dicompressImage = dicompress(losslessImageCompressed)
                        save_image(dicompressImage, "Burro", imagename)
                        #save_image(linear_interpolation(data), "linear-scaling-3x", imagename)
                        #save_image(nearest_neighbors(data), "nearest_neighbors", imagename) 
                        #save_image(average(data), "interpolation-without-scaling", imagename)
                        #save_image(scaling(data), "interpolation-with-scaling", imagename)
                    
                        #tecla = input("Pulsa cualquier tecla para procesar la siguiente imagen")

if __name__ == '__main__':
    reader()

    print(sizes)
    

"""
    __
___( o)>
\ <_. )
 `---'   hey o/. Im just a dock.

"""