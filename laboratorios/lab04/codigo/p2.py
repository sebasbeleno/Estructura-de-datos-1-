class Tree:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val): #
        #Si no está
        if not self.val: #1
            self.val = val #1
            return #1
        #Si son iguales
        if self.val == val: #1
            return #1
        #Menos   
        if val < self.val: #1
            
            if self.left: #1
                self.left.insert(val) #T(N/2)
                return #1
            self.left = Tree(val) #1
            return #1
        
        if self.right: 
            self.right.insert(val)
            return
        self.right = Tree(val)

    def preorder(self, vals):
        if self.val is not None:
            vals.append(self.val)
        if self.left is not None:
            self.left.preorder(vals)
        if self.right is not None:
            self.right.preorder(vals)
        return vals

    def postorder(self, vals):
        if self.left is not None:
            self.left.postorder(vals)
        if self.right is not None:
            self.right.postorder(vals)
        if self.val is not None:
            vals.append(self.val)
        return vals

def main():
    nums = [50,30,24,5,28,45,98,52,60]
    bst = Tree()

    for num in nums:
        bst.insert(num)

    print(bst.preorder([]))
    print(bst.postorder([]))
    
if __name__ == "__main__":
    main()

    Wil
    Joa
    EU
    FKI
    EUHIA
    SUF
    PIO
    QUKV}
    PIO
