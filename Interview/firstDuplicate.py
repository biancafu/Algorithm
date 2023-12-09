# https://app.codesignal.com/interview-practice/question/pMvymcahZ8dY4g75q/description

def solution(a):
    '''
    create a set to keep track of what has occured
    go through the list, check if the number is already in set
    if so return the number (first occurence will be the minimal index)
    return -1 if no duplicated values
    '''
    numlist = set()
    for num in a:
        if num in numlist:
            return num
        
        numlist.add(num)
    
    return -1

