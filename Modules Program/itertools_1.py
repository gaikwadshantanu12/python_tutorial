"""
Write a python program which iterates the integers from 1 to a given number
and print "Coca" for multiples of three, prin "Cola" for multiplies of five, print
"CocaCola" for multiplies for both three and five using itertools module
"""

"""
# Method 1

end = int(input("Enter end : "))
for i in range(1,end+1):
    if i%3 == 0 and i%5 == 0:
        print("CocaCola")
    elif i%5 == 0:
        print("Cola")
    elif i%3 == 0:
        print("Coca")
    else:
        print(i)
"""

"""
# Method 2

import itertools as itr
end = int(input("Enter end : "))
a = itr.count(1)       # start counting from 1
for i in itr.islice(a,end):
    if i % 3 == 0 and i % 5 == 0:
        print("CocaCola")
    elif i % 5 == 0:
        print("Cola")
    elif i % 3 == 0:
        print("Coca")
    else:
        print(i)
"""

import itertools as itr

end = int(input("Enter end : "))

coca = ['','','Coca']
coca_cycle = itr.cycle(coca)
# print(list(itr.islice(coca_cycle,end)))

cola = ['','','','','Cola']
cola_cycle = itr.cycle(cola)
# print(list(itr.islice(cola_cycle,end)))

merger_list = (x+y for x,y in zip(coca_cycle,cola_cycle))
# print(list(itr.islice(merger_list,end)))

result = (word or num for word,num in zip(merger_list,itr.count(1)))
# print(list(itr.islice(result,end)))

for item in itr.islice(result,end):
    print(item)