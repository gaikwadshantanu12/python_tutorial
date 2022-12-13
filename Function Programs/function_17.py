# WAP to check whether a string is a panagram or not
"""
For example : "The quick brown fox jumps over the lazy dog"
Means if our string has all 26 alphabets then it is panagram
"""

def isPanagramString(s):
    alpha = {chr(ch) for ch in range(ord('A'),ord('Z')+1)}
    s = s.upper()
    s = set(s)

    if alpha <= s:
        return True
    else:
        return False

print(isPanagramString(input("Enter string : ")))
