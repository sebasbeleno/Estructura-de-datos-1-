import numpy as np

"""
    px = len(image[0])
    py = len(image)
"""
def create_empy_image( px, py):


    nx = sum(3 for i in range(1, px)) + 1
    ny = sum(3 for i in range(1, py)) + 1

    return np.zeros((ny, nx))


def linear_interpolation(image_data):

    size_x = len(image_data[0])
    size_y = len(image_data)

    image_climbing = create_empy_image(size_x, size_y)

    for y in range(0, len(image_data)):
        for x in range(0, len(image_data[0])):
            
            py = int((y/(len(image_data)-1)) * (len(image_climbing)-1))
            px = int((x/(len(image_data[0])-1)) * (len(image_climbing[0])-1))

            image_climbing[py][px] = image_data[y][x]

    for y in range(0, len(image_climbing)-3, 3):
        for x in range(0, len(image_climbing[0])-3, 3):

            p1 = image_climbing[y][x]
            p2 = image_climbing[y][x+3]
            p3 = image_climbing[y+3][x+3]
            p4 = image_climbing[y+3][x]

            lx1 = (image_climbing[y][x] - image_climbing[y][x+3])/4
            #TODO: Sino da sumar la minimo
            image_climbing[y][x+2] = lx1+ image_climbing[y][x+3]
            image_climbing[y][x+1] = lx1+ image_climbing[y][x+2]

            ly1 = (image_climbing[y][x] - image_climbing[y+3][x])/4
            image_climbing[y+2][x] = ly1 + image_climbing[y+3][x]
            image_climbing[y+1][x] = ly1 + image_climbing[y+2][x]

            lx2 = (image_climbing[y][x+3] - image_climbing[y+3][x+3])/4
            image_climbing[y+3][x+2] = lx2 + image_climbing[y+3][x+3] 
            image_climbing[y+3][x+1] = lx2 + image_climbing[y+3][x+2] 

            ly2 = (image_climbing[y+3][x+3] - image_climbing[y][y+3])/4
            image_climbing[y+2][x+3] = ly2 + image_climbing[y+3][x+3]
            image_climbing[y+1][x+3] = ly2 + image_climbing[y+2][x+3]

            lc1 = (image_climbing[y][x+1] - image_climbing[y+3][x+1]) / 4
            image_climbing[y+1][x+1] = lc1 + image_climbing[y][x+1]
            image_climbing[y+2][x+1] = lc1 + image_climbing[y+3][x+1]

            lc2 = (image_climbing[y][x+2] - image_climbing[y+3][x+2]) / 4
            image_climbing[y+2][x+2] = lc2 + image_climbing[y][x+2] 
            image_climbing[y+1][x+2] = lc2 + image_climbing[y+3][x+2]
 
        
            
    return image_climbing


    