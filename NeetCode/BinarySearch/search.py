'''
had the right idea to split the search in half first then condition it further
but made the mistake of not conditioning properly
when split in half doing nums[low] <= nums[mid] or nums[mid] > nums[high] is the same
however for the if condition we need to split in ascending order so if mid > high
we will create if condition for low ~ mid and then else (mid + 1 ~ high)
this way we are gauranteed that binary search will work in the subdivision
'''

def search(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        
        # if nums[low] <= nums[mid]:
        #     if target <= nums[mid] and target >= nums[low]:
        #         high = mid - 1
        #     else:
        #         low = mid + 1
        # else: #nums[low] > nums[mid]
            # if target >= nums[mid] and target >= nums[low]:
            #     high = mid - 1
            # else:
            #     low = mid + 1

        if nums[mid] > nums[high]: #right side small
            if target <= nums[mid] and target >= nums[low]:
                high = mid - 1

            else:
                low = mid + 1

        else:
            if target >= nums[mid] and target <= nums[high]:
                low = mid + 1

            else:
                high = mid - 1


    return -1

a = search([4,5,6,7,0,1,2], 0)
print(a)