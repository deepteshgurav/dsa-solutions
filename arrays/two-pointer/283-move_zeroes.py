# Input : [0,1,0,3,12]
# Output: [1,3,12,0,0]

def move_zeroes(nums):
    n = len(nums)
    
    # If input array length is just one then return as it is
    if n == 1:
        return nums
    
    left = 0
    right = 1
    
    while right < n:
        if nums[left] == 0:
            # If both pointers are 0 then no need to swap. Just increment right
            if nums[right] == 0:
                right += 1
            else:
                # If both pointers are not 0 then swap left and right and increment both
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right += 1
    return nums

nums = [0,1,0,3,12]
print(move_zeroes(nums))
    