#we go left when we keep an element
#we go right when we decide to discard it

class Tree:
    def __init__(self, number, counter=0):
        self.left = None
        self.right = None
        self.counter = counter
        self.number = number

    def initialise(self, batch):
        return __init__(0, batch[0]-1)  #for the given task, there is always precedent element lower by one, we will start from it

    def keep(self, passed_number):
        self.left = Tree(counter = 0, number=passed_number)
        self.right = None

    def discard(self, passed_number):
        self.left = None
        self.right = Tree(counter = 0, number=passed_number)

    def count_leaves(self):
        leaves = 0
        if self.left != None:
            leaves += count_leaves(self.left)
        if self.right != None:
            leaves += count_leaves(self.right)
        elif (self.left == None) and (self.right == None): #the node is a leaf
            leaves = 1
        return leaves

batch = [1,2,3,4,5]

create_trees_from_batch

root = Tree(number = batch[0]-1, counter=0)

print(root.number)
