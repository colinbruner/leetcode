def lengthOfLongestSubstring(s: str) -> int:
    anchor = 0
    substring = ""
    for i in range(len(s)):
        if s[i] in s[anchor:i]:
            substring = s[i]
            anchor = i
        else:
            substring += s[i]


print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring(""))
print(lengthOfLongestSubstring(" "))
