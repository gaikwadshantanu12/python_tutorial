# WAP to get top three items in a shop

data = {'item1':45.50,'item2':35,'item3':41.30,'item4':55,'item5':24}

b = sorted(data.items(), key=lambda  t:t[1])

print(b[-1])
print(b[-2])
print(b[-3])