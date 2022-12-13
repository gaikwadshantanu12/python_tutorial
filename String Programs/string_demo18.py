# WAP to reverse order of words in string


"""
# Method 1


# Algorithm
# Step 1 - split string in list of words
# Step 2 - join list of words from last to first

s = input("Enter the string - ")
lst = s.split()         # step 1
res = " ".join(lst[::-1])
print(f"Original String :- {s}")
print(f"Words Reversed :- {res}")
"""

# Method 2
s  = input("Enter the string - ")
lst = s.split()
res = ""
for item in reversed(lst):          # or lst[::-1]
    res = res + item + " "

print(f"Original String - {s}")
print(f"Words Reversed - {res}")