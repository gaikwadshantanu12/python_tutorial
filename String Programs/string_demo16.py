# WAP to count number of words in string

"""
# Method 1
string = input("Enter the string - ")
c = string.count(" ")
print(f"No. of words in '{string}' are {c+1}.")

Error - if no of space between 2 words are given
"""

# Method 2
string = input("Enter the string - ")
print(f"No. of words in '{string}' are {len(string.split())}.")