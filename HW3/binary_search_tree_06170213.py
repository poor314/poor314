class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

        
class Solution(object):
    def insert(self, root, val):
        if root is None:
            root = Node(val, None, None)
        elif val < root.val:
            root.left = insert(root.left, val)
        else:
            root.right = insert(root.right, val)

        return root

        
    def delete(self, root, target):
        if self.root is None:
            return ValueError(data, ' does not exist, BST is empty.')
        try:
            self.root = self.root.delete(val)
        except ValueError as err:
            print(err)
        finally:
            self.printInOrder()
        
    def search(self, root, target):
        if root==[]:
            print("Can't find",val)
            
        elif root[0]==value:
            print("Found",val)
   
        elif root[0]>value:
            self.search(T[1],val)
     
        elif root[0]<value:
            self.search(T[2],val)

    def modify(self, root, target, new_val):
        if target is not new_val:       
            Solution().insert(root,new_val)
            return Solution().delete(root,target)
        else:
            return root

#https://gist.github.com/aaronjwood/916cbe6bd97b5ec41f6c
#https://github.com/SNavleen/Binary-Search-Tree-Python/blob/master/BinarySearchTree.py
