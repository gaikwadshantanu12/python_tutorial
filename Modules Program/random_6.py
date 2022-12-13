# Project - Dance floor random partner pair

"""
Logic :
1. Read a name from user
2. It its girl then pick up a boy as partner & vice versa
3. Pairs should be unique (no boy or girl should be repeat)
4. Stop if dance floor is full or either list is empty
"""

import random as r
boys = ['Diptesh','Ajinkya','Yadnesh','Vishal','Ketan','Shubham','Pratik','Abhishek','Himanshu','Bhushan',
        'Uddesh','Ranapratapsingh','Yash','Niranjan','Swanand','Shantanu','Siddhesh','Suraj','Sanket',
        'Kiran','Umesh','Prasad']

girls = ['Mrunal','Priyanka','Sanjeevani','Yashashri','Ashwini','Yashshree','Trupti','Mansi','Geeta','Sakshi',
         'Vaishnavi','Nikita','Sayali','Utkarsha','Shivani','Chaitali','Ruchita','Uma','Nandini','Priyanka',
         'Vaishnavi','Shital']

pairs = int(input("Enter number of maximum pairs : "))
count = 0
while count < pairs:
    name = input("Enter Name : ")
    if name in boys:
        partner = r.choice(girls)
        boys.remove(name)
        girls.remove(partner)
        print(f"Hello {name}, Your Partner is {partner}")
        count += 1
    elif name in girls:
        partner = r.choice(boys)
        girls.remove(name)
        boys.remove(partner)
        print(f"Hello {name}, Your Partner is {partner}")
        count += 1
    else:
        print("Your Are Not Registered Or Already Picked Up...")

    if not boys or not girls:
        print("Sorry, No More Partners Left...")
        break

else:
    print("\nAll Pairs Are Formed...")