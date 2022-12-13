# WAP to sort elements of string

# 1. Word wise sorting
# 2. Letter wise sorting

"""
2. Word Wise Sorting

s = input("Enter the string - ")
print("Original String : ",s)
lst = sorted(s)
asc = "".join(lst)
print(f"In Ascending Order : {asc}")
lst = sorted(s,reverse=1)
des = "".join(lst)
print(f"In Descending Order : {des}")
"""


# 1. Word wise sorting
# Algorithm
# Step 1 - split string in list of words
# Step 2 - sort above list of words
# Step 3 - join above list to get result


s = input("Enter the string - ")
lst = s.split()         # step 1
lst = sorted(lst)       # step 2
result = " ".join(lst)  # step 3
print(f"Original String :- {s}")
print(f"Sorted String in Ascending Order :- {result}")
lst = sorted(lst,reverse=1)
result = " ".join(lst)
print(f"Sorted String in Descending Order :- {result}")