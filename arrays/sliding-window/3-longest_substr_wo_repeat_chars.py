# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

# Solution using hash set and sliding window technique
def lengthOfLongestSubstring(s):
    char_set = set()
    left = 0
    n = len(s)
    max_length = 0
    
    for right in range(n):
        # If the character at right pointer is already in the set, we need to move the left pointer to the right until we remove the duplicate character
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        # Add the current character to the set
        char_set.add(s[right])
        
        # Update the maximum length of substring found so far
        max_length = max(max_length, right - left + 1)
    
    return max_length


# Solution using hash map and sliding window technique
def lengthOfLongestSubstring(s):
    char_index_map = {}
    left = 0
    n = len(s)
    max_length = 0

    for right in range(n):
        # If the character at right pointer is already in the map, we need to move the left pointer to the right until we remove the duplicate character
        if s[right] in char_index_map and char_index_map[s[right]] >= left:
            left = max(left, char_index_map[s[right]] + 1)

        # Update the index of the current character
        char_index_map[s[right]] = right

        # Update the maximum length of substring found so far
        max_length = max(max_length, right - left + 1)

    return max_length