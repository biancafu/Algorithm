import math
#O(nlogn)

class Solution(object):
    #faster solution i think it is because 
    def minEatingSpeed_faster(self, piles, h):
        low = 1
        high = max(piles)
        while low < high:
            speed = (low + high) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(float(p) / speed)
            if hours > h:
                low = speed + 1
            else:
                high = speed #doesn't exclude itself when hours == speed because this could be the min, we need to go left to check but cannot exclude 
                #because of this condition, our while loop has to be exclusive (low < high)
                #this is because if low == high, and if hours == h, we will be in an infinite loop because it will never increment (low or high)
                #essentially we want to return the value when low == high

                '''
                can also do high = speed - 1, but the while condition will become low <= high, however this is slower than the above one
                this worked because after you do high = speed - 1, you can go back higher by having low speed + 1
                with the case ([30,11,23,4,20], 6), the last run was low = 22, high = 22 but the answer was supposed to be 23
                this is because  when low == high == 22, it ran and hours > h, therefore low = 22 + 1 which give us the correct answer in the end
                '''
        return low
    #Neetcode solution
    def minEatingSpeed(self, piles, h):
        low = 1 #cannot be 0
        high = max(piles)
        res = high #gaurantee if we use the max of piles, we can finish banans within time
        while low <= high:
            mid = (low + high) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(float(p)/mid)
            if hours > h:
                low = mid + 1
            else:
                high = mid - 1
                res = min(res, mid)
        return res
    
    
                
# 1 2 3 4 5 6 7 8 9 10 11
        
s =  Solution()
a = s.minEatingSpeed_faster([30,11,23,4,20], 6)
print(a)