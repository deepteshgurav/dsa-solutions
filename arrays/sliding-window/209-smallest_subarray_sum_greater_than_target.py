# Input: target = 7, nums = [2,3,1,2,4,3]
#Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

def smallest_subarray_sum_greater_than_target(target, nums):
    left = 0
    curr_sum = 0
    min_length = float('inf')
    n = len(nums)
    
    for right in range(n):
        curr_sum += nums[right]
        
        while curr_sum > target:
            min_length = min(min_length, right - left + 1)
            curr_sum -= nums[left]
            left += 1
            
    return min_length if min_length != float('inf') else 0