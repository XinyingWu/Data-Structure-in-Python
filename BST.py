#Node
class Node(object): 
    def __init__(self, elem=-1, leftchild=None, rightchild=None):
        self.elem = elem
        self.leftchild = leftchild
        self.rightchild = rightchild

# Tree
class Tree(object):
    def __init__(self):
        self.root = Node()
        self.itemList = []
        
   # Add a node
    def add(self, elem):
        node = Node(elem)
        if self.root.elem == -1:  # if the tree is emplty, give the root a value
            self.root = node
            self.itemList.append(self.root)
        else:
            treeNode = self.itemList[0]  # the tree of the node is not equal
            if treeNode.leftchild == None:
                treeNode.leftchild = node
                self.itemList.append(treeNode.leftchild)
            else:
                treeNode.rightchild = node
                self.itemList.append(treeNode.rightchild)
                self.itemList.pop(0)  # abandon the right tree if it exists


    def front_digui(self, root):
        # pre-order recursion
        if root == None:
            return
        print(root.elem)
        self.front_digui(root.leftchild)
        self.front_digui(root.rightchild)


    def middle_digui(self, root):
       # in-order recursion
        if root == None:
            return
        self.middle_digui(root.leftchild)
        print(root.elem)
        self.middle_digui(root.rightchild)


    def later_digui(self, root):
       # post-order recursion
        if root == None:
            return
        self.later_digui(root.leftchild)
        self.later_digui(root.rightchild)
        print(root.elem)


if __name__ == '__main__':
    values = range(10)     #create 10 values for node
    tree = Tree()          #create a new tree
    for elem in values:                  
        tree.add(elem)     #add values into the node of trees

    print('\n\nPre-order recursion:')
    print(tree.front_digui(tree.root))
    
    print('\nIn-order recursion:')
    print(tree.middle_digui(tree.root))
    
    print ('\nPost-order recursion:')
    print( tree.later_digui(tree.root))

   
