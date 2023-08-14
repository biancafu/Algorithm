#16 min 70-90% speed (one 97% one 78%), big difference memory (one 98% one 35%)

from collections import deque
from collections import defaultdict
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        #level order (BFS) -> queue
        q = deque()
        res = defaultdict(list)
        q.append([root, 0])

        while q:
            node, count = q.popleft()
            if node:
                res[count].append(node.val)
                q.append([node.left, count + 1])
                q.append([node.right, count + 1])
        
        return res.values()
    
    #speed 78%, better memory: 90% (ran again drop to 20% lol...)
    def levelOrder_neetcode(self, root):
        q = deque()
        res = []
        q.append(root)

        while q:
            qlen = len(q)
            level = []
            for i in range(qlen):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    level.append(node.val)

            if level:
                res.append(level)

        return res