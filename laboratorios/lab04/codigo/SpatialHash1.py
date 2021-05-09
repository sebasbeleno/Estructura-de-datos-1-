from collections import deque 
class spatialHash3D():
    
    def __init__(self, cellSize):
        self.cellSize = cellSize
        self.cells = {}
        
    def hashFunction(self, point):
        return (int(point[0] // self.cellSize), int(point[1] // self.cellSize), int(point[2] // self.cellSize))
    
    def insert(self, point):
        if(len(point) == 2):
            point = (point[0], point[1], 0)
        key = self.hashFunction(point)
        if (key not in self.cells):
            self.cells[key] = deque()
            self.cells[key].append(point)
        else:
            self.cells[key].append(point)
            
    def search(self, point):
        key = self.hashFunction(point)
        if point in self.cells[key]:
            return True
        return False
    
    def retrieveCell(self, key = False, point = None):
        if key:
            return self.cells[key]
        elif(point is not None):
            key = self.hashFunction(point)
            return self.cells[key]
        else:
            raise Exception("Invalid input")
            
    def getFriends(self, point, radious):
        friends = deque()
        keys = self.__getNeighbourKeys(point, radious)
        for neigKey in keys:
            for key in self.cells:
                if(key[0] <= neigKey[0] or key[1] <= neigKey[1] or key[2] <= neigKey[2]):
                    cell = self.cells[key]
                    for friend in cell:
                        d = self.__getDistance(point, friend)
                        if(d <= radious and friend != point and friend not in friends):
                            friends.append(friend)
        return friends
        
    def __getNeighbourKeys(self, point, radious):
        keys = deque()
        posx = point[0]
        posy = point[1]
        posz = point[2]
        for z in range(-1,1):
            for y in range(-1,1):
                for x in range(-1,1):
                    tempPoint = (posx + x*radious, posy + y*radious, posz + z*radious)
                    key = self.hashFunction(tempPoint)
                    keys.append(key)
        return keys
                
    def getCells(self):
        return self.cells
    
    def __getDistance(self, p1, p2):
        return  (((p1[0] - p2[0])**2) + ((p1[1] - p2[1])**2) + ((p1[2] - p2[2])**2))**(1/2)