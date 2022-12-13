# WAP to remove duplicates from dictionary

# Note - we have to remove duplicate values because keys are never duplicate

d1 = {1:10,2:20,3:10,4:20,5:50}
d2 = {}
for k,v in d1.items():
    if v not in d2.values():
        d2[k] = v               # d2.update({k:v})

print(d2)