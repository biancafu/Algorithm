# https://app.codesignal.com/interview-practice/question/uX5iLwhc6L5ckSyNC/description?solutionId=2fdbQdtwrnYhYNRjL

def solution(s):
    for c in s:
        if s.index(c) == s.rindex(c):  #rindex is the last occuring index
            return c
    return '_'

#my solution
from collections import defaultdict

def solution(s):
    left = (0, '')
    right = (len(s) - 1, '')
    i,j = 0, len(s) - 1
    frequency = defaultdict(list)
    
    for i in range(len(s)):
        frequency[s[i]].append(i)
    
    index = float('inf')
    for key, value in frequency.items():
        if len(value) == 1:
            index = min(index, value[0])
    
    return "_" if index == float('inf') else s[index]
            
            

