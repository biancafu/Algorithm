# from collections import defaultdict

#speed 87.7% memory 35.72%
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        prereq length == 2: meaning that we will only hv 1 prereq course to record at a time however we can hv repeated ones with diff prereq 
        use dfs to go through every course's pre req list, if we hv a loop, that means it is impossible, if it goes to an end, that means this set of courses can be completed
        """
        #set it outside (using it like backtracking)
        visiting = set() #keep track of the curr visiting courses, so we see if it forms a loop

        # cannot use default dict because an error shows up saying that the dictionary size is changing 
        # (since we are changing some to [] which i think in defaultdict, it will see it as deleted, so the error shows up)
        # this way we are implementing every single possible course and even if we set it to [] it still count as 1 length in normal dict
        # coursesMap = defaultdict(list) #all the courses and its prereq
        coursesMap = { i: [] for i in range(numCourses) }

        #organize all the courses
        for curr, pre in prerequisites:
            coursesMap[curr].append(pre)
        
        #dfs
        def dfs(course): #input parameter of which course we are checking
            #breaking condition when course is seen before => forms loop
            if course in visiting:
                return False
            #breaking condition if course is [] (from our default dict) meaning no prereq from this course
            if not coursesMap[course]: #return True in this case because 
                return True 
            
            #otherwise, lets dfs into the prereq for this course
            visiting.add(course)
            for pre in coursesMap[course]:
                #dfs returns something
                if not dfs(pre): #if it fails, we just simply return false
                    return False
            visiting.remove(course) #remove from set once we finish checking
            coursesMap[course] = [] #we finished checking all prereq, so then we can set it to empty
            return True #if we finished checking everything, return True
        
        #go through every course on the map and dfs search, if it comes back false, means it is impossible
        for course in coursesMap:
            if not dfs(course):
                return False 
        
        return True #if we pass all the courses check
        



        








        