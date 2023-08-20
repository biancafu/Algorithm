#was able to solve it but took a long time, used BFS method for serializing but got confused if i was able to use dfs for deserializing
# ** we need to use same logic for serializing/deserializing so if i used bfs i need to do for both, if i use dfs, i will do that for both

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque

class Codec:

    def serialize(self, root):
        output = ""
        q = deque()
        q.append(root)
        while root and q:
            qlength = len(q)
            for i in range(len(q)):
                node = q.popleft()
                if not node:
                    output += ",null"
                else:
                    if output:
                        output += ","
                    output += str(node.val)
                    q.append(node.left)
                    q.append(node.right)
        print(output)
        return output
                




    def deserialize(self, data):
        if not data:
            return None
        vals = data.split(",")
        
        root = TreeNode(int(vals))
        q = [root]
        i = 0
        #in the beginning i did the way with while nested for loop to ensure im popping according to level (i think)
        #over here we don't have to do that, since we don't need to keep track of each level and also empty nodes still exist in the vals array as null

        while q:
                node = q.pop(0)
                i += 1
                #over here instead of popping the values of vals, just use a counter
                #pop is slower so it takes more time even tho from time complexity, it will be the same
                left = vals[i]
                i += 1
                right = vals[i]

                if left != "null": #if its null, that means its None, we don't have to append it to the q and check again
                    node.left = TreeNode(left)
                    q.append(node.left) 
                if right != "null":
                    node.right = TreeNode(right)
                    q.append(node.right)
        return root

        
