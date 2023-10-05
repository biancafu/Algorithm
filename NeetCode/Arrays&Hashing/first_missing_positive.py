
def firstMissingPositive(nums):
    nums.append(0)
    n = len(nums)
    for i in range(len(nums)): #delete those useless elements
        if nums[i]<0 or nums[i]>=n:
            nums[i]=0
    for i in range(len(nums)): #use the index as the hash to record the frequency of each number
        #doing nums[i] % n, becuz if that number is repeated, we are gonna += n
        #the number that doesn't exist in the array will be left with its original value from nums
        #which was gauranteed to be < n, or we can also write it as nums[i] // n since now nums[i]/n will give us a float
        #with nums[i]//n, anything smaller than n == 0
        nums[nums[i]%n]+=n
    for i in range(1,len(nums)):
        print(nums[i] / n)
        print(nums[i] // n)
        if nums[i] < n: #nums[i] // n == 0:
            return i
    return n
        


a = firstMissingPositive([3,4,1,-1])
print(a)