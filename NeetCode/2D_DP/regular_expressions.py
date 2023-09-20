class Solution(object):
    #top dowm memoization: 75% speed 10% memory
    def isMatch(self, s, p):
        '''
        -use recursion
        -the first element will not be * (since it depends on the previous char)

        -if i and j are out of bound at the same time, then its a match
        -if j is out of bound and i isn't, then its not a match (since theres no more pattern but theres more text)
        -if i is out of bound and j isn't, then we continue to check (since we can have stars which can be equal to 0 occurence)
        edge case: what about .*
        '''
        cache = {} #memoization
        

        def dfs(i,j):
            #dp
            # if (i,j) in cache:
            #     return cache[(i,j)]
            #breaking condition
            if i >= len(s) and j >= len(p): #both out of bound, its a match
                return True
            if j >= len(p): #only pattern is out of bound, not a match
                return False
            
            #continue if both are in bound or only i is out of bound


            #case 1: when characters match 
            match = i < len(s) and (s[i] == p[j] or p[j] == ".") #wild card character

            #case 2: star character
            d   #or not add previous character (we are keeping i as it is, and incrementing j by 2 since we are skipping the character and its * value)

                # return cache[(i,j)]

            #case 1 extension: continue the step for normal match here
            if match: 
                return dfs(i+1, j+1) #increment to the next pointer 
                # return cache[(i,j)]
               
            #case 3: if it doesn't match, and theres no star value
            # cache[(i,j)] = False
            return False
        return dfs(0,0)

        
        
        