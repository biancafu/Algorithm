class Solution(object):
    def twoSum(self, numbers, target):
        start = 0
        end = len(numbers) - 1
        while start < end:
            curr = numbers[start] + numbers[end]
            if curr > target:
                end -= 1
            elif curr < target:
                start += 1
            else: # curr == target
                return [start + 1, end + 1]
            


    #solution from discussion using binary search:
    def twoSum_binarysearch(self, numbers, target):
        investigatedSoFar = []
        for i in range(len(numbers)):
            if not numbers[i] in investigatedSoFar:
                investigatedSoFar.append(numbers[i])
                l, r = i + 1, len(numbers) - 1
                tmp = target - numbers[i]
                while l <= r:
                    mid = l + (r-l) // 2
                    if numbers[mid] == tmp:
                        return([i + 1, mid + 1])
                    elif numbers[mid] < tmp:
                        l = mid + 1
                    else:
                        r = mid - 1