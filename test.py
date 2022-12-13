# WAP to convert a given string list to a tuple
# Original String - python 3.0
# Expected Output - ('p','y','t','h','o','n','3','.','0')

s = "python 3.0"
print(tuple([ch for ch in s if ch != " "]))
