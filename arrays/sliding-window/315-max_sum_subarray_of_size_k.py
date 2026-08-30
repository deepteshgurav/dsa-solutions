# Input: nums = [2, 1, 5, 1, 3, 2]
# k = 3
# Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3].

def max_subarray_sum_of_size_k(nums, k):
    n = len(nums)
    
    if n < k:
        return -1  # Not enough elements to form a subarray of size k
    
    curr_sum = sum(nums[:k])
    max_sum = curr_sum
    
    left = 0
    right = k
    
    while right < n:
        curr_sum = curr_sum - nums[left] + nums[right]
        max_sum = max(max_sum, curr_sum)
        left += 1
        right += 1
        
    return max_sum

