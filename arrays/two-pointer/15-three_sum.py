# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

def three_sum(nums):
    # Sort the input array to apply two pointer
    nums.sort()
    result = []
    n = len(nums)
    
    # The idea is to have one fix number i in the input array and then run 2Sum two pointer solution for the remaining part of the array.
    for i in range(n-2):
        # If the fixed number in input array is more than 0 then the triplet sum cannot be 0 as the array is sorted and all numbers towards the right of fixed number i will always be more than i
        if nums[i] > 0:
            break
        
        # Skip duplicate values
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        # Two pointers for the remaining part of the array (i+1 till n-1)
        left = i + 1
        right = n - 1
        
        # Apply 2Sum two pointer logic
        while left < right:
            triplet_sum = nums[i] + nums[left] + nums[right]
            if triplet_sum == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip computing triplet sum if the adjacent (next) element is same to skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                    
                left += 1
                right -= 1
                
            elif triplet_sum < 0:
                left += 1
            
            else:
                right -= 1
    return result
                

nums = [-1,0,1,2,-1,-4]
print(three_sum(nums))
                
        