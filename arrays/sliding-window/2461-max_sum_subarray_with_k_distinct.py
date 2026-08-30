# Input: nums = [1,5,4,2,9,9,9], k = 3
# Output: 15
# Explanation: The subarrays of nums with length 3 are:
# - [1,5,4] which meets the requirements and has a sum of 10.
# - [5,4,2] which meets the requirements and has a sum of 11.
# - [4,2,9] which meets the requirements and has a sum of 15.
# - [2,9,9] which does not meet the requirements because the element 9 is repeated.
# - [9,9,9] which does not meet the requirements because the element 9 is repeated.
# We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions

def max_sum_subarray_with_k_distinct(nums, k):
    left = 0
    right = 0
    n = len(nums) - 1
    max_sum = 0
    curr_sum = 0
    
    num_set = set()
    
    while right < n:
        while nums[right] in num_set:
            num_set.remove(nums[left])
            curr_sum -= nums[left]
            left += 1
            
        num_set.add(nums[right])
        curr_sum += nums[right]
        
        if (right - left + 1) == k:
            max_sum = max(max_sum, curr_sum)
            num_set.remove(nums[left])
            curr_sum -= nums[left]
            left += 1
            
        right += 1
        
    return max_sum
        
        
        
    