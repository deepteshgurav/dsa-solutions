# Input: numbers = [2,7,11,15], target = 9
# Output: [1, 2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

def two_sum(numbers, target):
    left = 0
    right = len(numbers) - 1
    
    while left <= right:
        two_sum = numbers[left] + numbers[right]
        
        if two_sum < target:
            left += 1
        elif two_sum > target:
            right -= 1
        else:
            result =  [left + 1, right + 1]
            
    return result

numbers = [2,7,11,15]
target = 9
print(two_sum(numbers, target))