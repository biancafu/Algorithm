#looked at solution 
def threesum(nums): # O(nlogn)
    #sort the number to easier eliminate repeated values
    nums.sort()
    results = [] #put the results at wrong space before (within the loop), silly mistake

    for i, num in enumerate(nums):
        #check if we have repeated values
        #the logic is that, when we start with the same number, we will get the same combo
        #therefore skip the same number as starting
        if i > 0 and num == nums[i - 1]: 
            continue

        #use two pointer method for the rest of the value to find the target sum
        #easy cuz the list is sorted
        low = i + 1 #starting from the next of i
        high = len(nums) - 1
        target = 0 - num
        while low < high: 
            currsum = nums[low] + nums[high]
            if currsum > target:
                high -= 1
            elif currsum < target:
                low += 1
            else: #currsum == target:
                results.append([num, nums[low], nums[high]]) #found one match!
                #but it is possible that there are multiple matches for this target, so we need to continue checking
                low += 1 #increment one side to start checking process for next round
                #also skip repeated numbers, because this will generate the same numbers again
                #since a + b = target, if a is the same, then be must also be same
                while nums[low] == nums[low - 1] and low < high: #remember to check for index 
                    low += 1
        
    return results



def threeSum(nums): #faster solution: O(n^2)?, didn't use sort

	res = set()

	#1. Split nums into three lists: negative numbers, positive numbers, and zeros
	n, p, z = [], [], []
	for num in nums:
		if num > 0:
			p.append(num)
		elif num < 0: 
			n.append(num)
		else:
			z.append(num)

	#2. Create a separate set for negatives and positives for O(1) look-up times
	N, P = set(n), set(p)

	#3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
	#   i.e. (-3, 0, 3) = 0
	if z:
		for num in P:
			if -1*num in N:
				res.add((-1*num, 0, num))

	#3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
	if len(z) >= 3:
		res.add((0,0,0))

	#4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
	#   exists in the positive number set
	for i in range(len(n)):
		for j in range(i+1,len(n)):
			target = -1*(n[i]+n[j])
			if target in P:
				res.add(tuple(sorted([n[i],n[j],target])))

	#5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
	#   exists in the negative number set
	for i in range(len(p)):
		for j in range(i+1,len(p)):
			target = -1*(p[i]+p[j])
			if target in N:
				res.add(tuple(sorted([p[i],p[j],target])))

	return res
a = threesum([-1,0,1,2,-1,-4])
print(a)