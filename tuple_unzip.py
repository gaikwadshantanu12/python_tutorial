# WAP to unzip list of tuple(pair) into individual lists
# Sample list = [(1,2),(2,3),(3,4)]
# Expected Output - [[1,2,3],[2,3,4]]

a = [(1,2),(2,3),(3,4)]
print([list(x) for x in list(zip(*a))])
