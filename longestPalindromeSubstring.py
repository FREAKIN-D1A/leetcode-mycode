def longestPalindrome(s: str) -> str:
    if not s:
        return ""

    n = len(s)
    start = 0  # Start index of the longest palindromic substring
    max_length = 1  # Length of the longest palindromic substring

    # Create a 2D DP table to store whether substrings are palindromic
    dp = [[False] * n for _ in range(n)]

    # All substrings of length 1 are palindromic
    for i in range(n):
        dp[i][i] = True

    # Check for palindromes of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_length = 2

    # Check for palindromes of length greater than 2
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if dp[i + 1][j - 1] and s[i] == s[j]:
                dp[i][j] = True
                start = i
                max_length = length

    return s[start : start + max_length]


# Example usage:
# print(longestPalindrome("babad"))  # Output: "bab" or "aba"
# print(longestPalindrome("cbbd"))  # Output: "bb"
print(
    longestPalindrome("cbbabadbsaippuakivikauppiasd")
)  # Output: "saippuakivikauppias"

"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        length = len(s)
        result = ""
        
        for i in range(length):
            odd = 1
            even = 0
            l = i - 1
            r = i + 1
            while l >= 0 and r < length:
                if s[l] == s[r]:
                    odd += 2
                    l -= 1
                    r += 1
                else:
                    break
            if odd > longest:
                longest = odd
                result = s[l + 1:r]
            l = i
            r = i + 1
            while l >= 0 and r < length:
                if s[l] == s[r]:
                    even += 2
                    l -= 1
                    r += 1
                else:
                    break
            if even > longest:
                longest = even
                result = s[l + 1:r]
        return result
        
"""
