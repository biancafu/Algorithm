class Solution(object):
    #this uses topological sort
    def findOrder(self, numCourses, prerequisites):
        """
        total of numCourses labeled from 0 ~ numCourses-1
        prereq in the form of [curr course, prereq for the curr course]
        return order of courses u should take to finish all courses
        if impossible return empty array
        if possible return one of the possible solutions

        #prereq map
        map = {course: [ all prereq ]} 
        #deque for order (?)
        result = deque()
        dfs into all 
        {
            0: []
            1: [0]
            2: [0]
            3: [1,2]
        }
        once we reach [], meaning this course doesn't need prereq, then we will add it to output. we will hv to not put this corse in the output again. otherwise we will go through the entire list from the mapping like before
        """
        # 83% speed 34% memory 
        # had to watch video
        
        map = { i:[] for i in range(numCourses) }
        for curr, pre in prerequisites:
            map[curr].append(pre)

        output = []
        visited = set()
        def dfs(course):
            if course in visited: 
                return False
            if course in output: #if in output, that means we gone through it already
                return True
            if not map[course]:
                output.append(course)
                return True

            visited.add(course)
            for pre in map[course]:
                #check all this course's prereqs
                if not dfs(pre):
                    return False
            visited.remove(course)
            output.append(course) #can add after we gone through all the prereq
            map[course] = []
            return True
        
        for course in map:
            if not dfs(course):
                return []
        return output

            
        
s = Solution()
a = s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
print(a)