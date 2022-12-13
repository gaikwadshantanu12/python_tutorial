# WAP to concatenate follwoing dictionaries to create a new one
"""
Sample dictionary -
dict1 = {1:10,2:20}
dict2 = {3:30,4:40}
dict3 = {5:50,6:60}

Expected Result - {1:10,2:20,3:30,4:40,5:50,6:60}
"""

dict1 = {1:10,2:20}
dict2 = {3:30,4:40}
dict3 = {5:50,6:60}
dict4 = {}
dict4.update(dict1)
dict4.update(dict2)
dict4.update(dict3)
print(dict4)

"""
Method 2
dict4 = {**dict1,**dict2,**dict3}
"""