#binary tree

# O(n - 1) -> O(n)
# worst case is ascending/descending

example_list = [17, 34, 8, 97, 52, 22, 156, 850, 4, 3, 0]

class Node: #only one class is needed for the binary tree
    
    #just like the doubly linked list, you need a head(self.data), next(self.right), prev(self.left)
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data: # if there is a root, left is scanned first
            if data < self.data:
                if self.left is None: #if left is none, set that as inputted data
                    self.left = Node(data)
                else: # if left is something, use that as the next point and try again
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None: #if right is none, set as inputted data
                    self.right = Node(data)
                else: # if right is something, use that as the next point and try again
                    self.right.insert(data)
        else: # if there was no root, the inserted data was set as the root
            self.data = data  

    def print_BT(self): #this print is in order, going from the left tree, to root, to right tree
        if self.left:
            self.left.print_BT()
        print(self.data) #only one print is needed, as self.left and self.right are called back recurisively
        if self.right:
            self.right.print_BT()

root = Node(17)
root.insert(34)
root.insert(8)
root.insert(97)
root.insert(52)
root.insert(22)
root.insert(156)
root.insert(850)
root.insert(4)
root.insert(3)
root.insert(0)
root.print_BT()