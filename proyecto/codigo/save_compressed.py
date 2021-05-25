import os

def save_compressed(image_data, method, name):

    image_data  = str(image_data)
    file_name = '{}-{}.txt'.format(name, method)

    path = create_directory(name)
    file_path = os.path.join(path, file_name)

    file = open(file_path, "w+")

    file.write(image_data)

    file.close()

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