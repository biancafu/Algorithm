#https://www.youtube.com/watch?v=wU6udHRIkcc

#disjoint sets are useful for detecting cycle from non-directed graph
#famous algorithm to detect cycle in a graph:  Kruskal's algorithm

'''
What are disjoint sets?
sets that hv nothing in common (not connected)

find operation: finding out which set this element belongs to
union operation: add another edge to a node from each set to connect 2 sets to perform union
                if the nodes are from same set, then that means there is a cycle

usually we don't group the nodes with a set, we group it with a parent (representative) so a tree
union (Tree): select 1 as parent, and merge the other as its children
use an array to record the weight/rank and if it is a parent (if it is, use negative, weight is the number)
'''

