# WAP to get he max and min value from dictionary

d = {1:1,5:25,6:36,2:4,3:9}
print("Maximum Value -",max(d.values()))
print("Minimum Value -",min(d.values()))
print("Maximum Key -",max(d))
print("Minimum Key -",min(d))
print("Maximum Pair -",max(d.items()))
print("Minimum Pair -",min(d.items()))

# If we pass only "d", then it will only compare with keys and all keys must be of same type