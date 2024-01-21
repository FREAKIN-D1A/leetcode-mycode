def lengthOfLongestSubstring(s):
    char_index = {}
    start = max_length = 0
    for end, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
            pass
        char_index[char] = end
        max_length = max(max_length, end - start + 1)
        pass
    pass
    return max_length


# Example usage:
print(lengthOfLongestSubstring("abcabcbb"))  # Output: 3
print(lengthOfLongestSubstring("bbbbb"))  # Output: 1
print(lengthOfLongestSubstring("pwwkew"))  # Output: 3


# ---------------------------------------------------------

"""
def lengthOfLongestSubstring(self, s: str) -> int:
    # lets do another implementation with for loop for r, cleaner, less code same complexity
    l = 0
    chrs = set()
    longest = 0

    for r in range(len(s)):
        # while our right pointer is already in our set we have to move the left and
        # remove from the set
        while s[r] in chrs:
            chrs.remove(s[l])
            l += 1
        chrs.add(s[r])
        longest = max(longest, len(chrs))
    return longest
"""


# ---------------------------------------------------------

"""
def lengthOfLongestSubstring(s):
    # Initialize a dictionary to store the index of each character
    char_index = {}
    start = max_length = 0

    for end, char in enumerate(s):
        # If the character is already in the dictionary and its index is after the start,
        # update the start pointer to the next index of the repeated character
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1

        # Update the index of the current character in the dictionary
        char_index[char] = end

        # Update the maximum length
        max_length = max(max_length, end - start + 1)

    return max_length

"""
