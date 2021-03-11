import os 
import csv

"""
Put here you folder path
"""
path = "C:/Users/Usuario/Desktop/Universidad/ST0245-Eafit/proyecto/datasets/archivosCSV"
os.chdir(path)

def image_compression(image_data):
    pass

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
            for file_data in c:
                file_path = os.path.abspath(file_data)
                
                with open(file_path, 'r') as csv_file:
                    reader = csv.reader(csv_file, delimiter=",")
                    """
                    Once read the archive, we save it inside or data structure.
                    """
                    for data in reader:
                        image_compression(data)
                        
"""
    __
___( o)>
\ <_. )
 `---'   hey o/. Im just a dock.

"""