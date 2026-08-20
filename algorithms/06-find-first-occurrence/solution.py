def findFirstOccurrence(nums, target):
    left = 0
    right = len(nums) -1
    
    while left<=right:
        mid = (left + right)//2
        if target == nums[mid]:
            if mid == 0 or nums[mid] != nums[mid-1]:
                return mid
            else:
                right = mid -1
        elif target < nums[mid]:
            right = mid -1
        elif target > nums[mid]:
            left = mid + 1
    return -1