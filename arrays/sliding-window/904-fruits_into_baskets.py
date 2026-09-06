# Input: fruits = [1,2,1]
# Output: 3
# Explanation: We can pick from all 3 trees.

# Input: fruits = [1,2,3,2,2]
# Output: 4
# Explanation: We can pick from trees [2,3,2,2].
# If we had started at the first tree, we would only pick from trees [1,2].

def total_fruit(fruits):
    left = 0
    n = len(fruits)
    max_count = 0
    fruit_count = {}
    
    for right in range(n):
        fruit_count[fruits[right]] = fruit_count.get(fruits[right], 0) + 1
        
        while len(fruit_count) > 2:
            fruit_count[fruits[left]] -= 1
            if fruit_count[fruits[left]] == 0:
                del fruit_count[fruits[left]]
            left += 1
            
        max_count = max(max_count, right - left + 1)
    
    return max_count