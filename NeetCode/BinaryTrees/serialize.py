#was able to solve it but took a long time, used BFS method for serializing but got confused if i was able to use dfs for deserializing
# ** we need to use same logic for serializing/deserializing so if i used bfs i need to do for both, if i use dfs, i will do that for both

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque

#speed 85% memory 15% i think memory is a lot larger using this approach because when serializing, 
#we are using an array to store instead of string like i did in BFS
class Codec_DFS:

    def serialize(self, root):
        output = []
        #this will append null on every leaf node before it reaches the end
        def dfs(root):
            #preorder
            if not root:
                output.append('null')
                return
            output.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ",".join(output)
        

    def deserialize(self, data):
        vals = data.split(',')
        #use a universal counter
        self.i = 0 #using this so we dont hv to pass in anything
        def dfs():
            curr = vals[self.i]
            if curr == "null":
                self.i += 1
                return None
            root = TreeNode(int(curr))
            self.i += 1
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()


#pretty efficient: 94% speed, 69% memory
class Codec_BFS:

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

        
