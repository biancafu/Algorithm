from collections import deque
class Solution(object):
    #the essential logic we have to understand for this question is: we want to work on the task that has the most occurence first, 
    #this is because there is a cool down for same tasks, with this restriction, we want to use the cool down time to work on other tasks for efficiency (so we are not just sitting and waiting)

    #65% speed 38% memory O(n) since we hv to go through every single tasks even if we do log(n) for each heappush
    def leastInterval_neetcode(self, tasks, n):
        #heap solution (heap + queue) by neetcode
        #since we only want the min length and not the actual tasks, we dont hv to keep track of the task
        #using a heap to keep track of which tasks to do first according to amount of tasks left.
        q = deque()
        counts = Counter(tasks) #this returns a dict with the tasks and number of occurence
        heap = [ -counts[k] for k in counts ]
        heapq.heapify(heap)
        timer = 0

        while heap or q:
            timer += 1
            #if we don't have any elements in heap, check if we have stuff in q, if we do, then we can skip the timer to the first element of q, since there are no other task available for us to do while waiting for the task in q to cool down
            if not heap:
                timer = q[0][1]
            
            else: #if heap has element
                occurence = heapq.heappop(heap) + 1 #we're adding 1 since its max heap so we used negative value for occurence
                if occurence: #occurence != 0
                    q.append([occurence, timer + n])
            
            if q and timer == q[0][1]: #check this for every loop
                heapq.heappush(heap, q.popleft()[0])
            
        return timer




        

        