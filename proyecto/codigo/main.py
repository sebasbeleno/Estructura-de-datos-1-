import os 
import csv
from typing import Literal
from save_image import save_image
from image_compression import scaling, average, nearest_neighbors
from image_decompression import linear_interpolation
from lossless import lossless, dicompress
from save_compressed import save_compressed
import time

"""
Put here you folder path
"""
path = "D:/Universidad/ST0245-Eafit/proyecto/datasets/archivosCSV"
        
os.chdir(path)

sizes = []

all_times = []
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
                        
                        #Save the original image
                        save_image(data, "original", imagename)
                        save_compressed(data, "original", imagename)
                        #Apply lossy compression method
                        losslyImageCompressed = average(data)
                        
                        #Save image comprred
                        #save_image(losslyImageCompressed, "linal-interpolation", imagename)
                        
                        start_time  = time.time()
                        #Conver numpyArray to "native" list
                        losslyImageCompressed = losslyImageCompressed.tolist()
                        
                        #Save .txt image of data from the image
                        save_compressed(losslyImageCompressed, "Avere", imagename)
                        
                        #Apply lossless compress method
                        losslessImageCompressed = lossless(losslyImageCompressed)
                        
                        time_taken =  (time.time() - start_time)
                        print(str(time_taken), " seconds, for ", len(losslyImageCompressed), "px X", len(losslyImageCompressed[0]), "px")
                        
                        #Save .txt of image compresed by lossless method
                        save_compressed(losslessImageCompressed, "Burro", imagename)

                        #Decompress the image from Burrow method 
                        dicompressImage = dicompress(losslessImageCompressed)

                        all_times.append(time_taken)
                        #Save the .txt whit decompress result to compare and evalue
                        save_compressed(dicompressImage, "Di-Compress", imagename)

                        #Save the image with the result
                        save_image(dicompressImage, "Dicompressed", imagename)
                        
                        #save_image(linear_interpolation(data), "linear-scaling-3x", imagename)
                        #save_image(nearest_neighbors(data), "nearest_neighbors", imagename) 
                        #save_image(average(data), "interpolation-without-scaling", imagename)
                        #save_image(scaling(data), "interpolation-with-scaling", imagename)
                    
                        #tecla = input("Pulsa cualquier tecla para procesar la siguiente imagen")

if __name__ == '__main__':
    reader()

    print(sizes)

    print(sum(all_times) / len(all_times))
    

"""
    __
___( o)>
\ <_. )
 `---'   hey o/. Im just a dock.

"""