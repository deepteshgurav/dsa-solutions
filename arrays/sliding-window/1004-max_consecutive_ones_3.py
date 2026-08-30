# In this problem, instead of thinking which 0's to flip to 1, think like what is the maximum subarray with atmost k zeroes.

def max_consecutive_ones(nums, k):
    left = 0
    max_length = 0
    n = len(nums)
    zero_count = 0
    
    for right in range(n):
        if nums[right] == 0:
            zero_count += 1
            
            
        # If the count of zeroes exceeds k, we need to shrink the window from the left until we have at most k zeroes in the window.
        while zero_count > k:
            # If the number leaving the window is a 0 then decrement zero_count and move left by 1
            if nums[left] == 0:
                zero_count -= 1
            left += 1
            
        max_length = max(max_length, right - left + 1)
        
    return max_length