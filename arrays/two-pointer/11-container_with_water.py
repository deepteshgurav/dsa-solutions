# Input: height = [1,8,6,2,5,4,8,3,7]

def container_with_most_water(height):
    n = len(height) - 1
    left = 0
    right = n 
    area = 0
    
    while left < right:
        temp_area = (right - left) * min(height[left], height[right])
        area = max(area, temp_area)
        
        if height[left] >= height[right]:
            right -= 1
        else:
            left += 1
            
    return area

height = [1,8,6,2,5,4,8,3,7]
print(container_with_most_water(height))