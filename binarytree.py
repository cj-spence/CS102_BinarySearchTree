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

    def search(self, data):
        if self.data == data: # when the node is equivalent to the key, it will return that it exists
            print("The data exists in the tree.")
            return

        if data < self.data: # if the given key is less than the scanned node, it will recursively search lower
            if self.left:
                self.left.search(data)
            else: # if all nodes are searched with no match, DNE is returned
                print("The data does not exist in the tree.")
                return

        else:
            if self.right: # if the given key is greater than the scanned node, it will recursively search higher
                self.right.search(data)
            else: # if all nodes are searched with no match, DNE is returned
                print("The data does not exist in the tree.")
                return 

    def insert(self, data): # this is equivalent to the requested add(x) method
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

    def delete(self, data):
        if data < self.data: # findind the value in the left tree
            if self.left is None: # if the data does not exist, return DNE
                print("The data does not exist in the tree.")
                return
            self.left = self.left.delete(data)
            return self # data is not deleted - yet
        elif data > self.data: # finding value in the right tree
            if self.right is None: # if the data does not exist, return DNE
                print("The data does not exist in the tree.")
                return 
            self.right = self.right.delete(data)
            return self # data is not deleted - yet
        else: 
            if self.left is None and self.right is None: # scans left and right children of the node
                return None # if there are no children, its a leaf (case 1) so we delete that 
            if self.left is None:
                return self.right # if there is only one child, we just delete the child
            if self.right is None:
                return self.left
            parent = self # setting temp values to be able to merge subtrees
            node = self.left 
            while node.right is not None: # finds the rightmost node to replace the node
                parent = node # no more need for parent to be parent, we change its use 
                node = node.right
            if parent.left is node: # last check for the left subtree to make sure everything is valid
                parent.left = None 
            else:
                parent.right = None
            self.data = node.data
            return self

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

root.search(850)
root.search(3)
root.search(100)
root.search(600)

root.delete(850)
root.delete(3)
root.delete(8)
root.print_BT()

