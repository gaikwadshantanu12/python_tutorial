row , column = [int(x) for x in input("Enter Rows X Columns - ").split()]
m = []
for i in range(row):
    a = []
    for j in range(column):
        a.append(1)

    m.append(a)


# j for loop will create a list - [1,1,1,1]
# i for loop will append it in empty list m and then it will empty the a list