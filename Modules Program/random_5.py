# Take list of boys and list of girls then create 10 random pairs

import random as r

boys = ['Diptesh','Ajinkya','Yadnesh','Vishal','Ketan','Shubham','Pratik','Abhishek','Himanshu','Bhushan',
        'Uddesh','Ranapratapsingh','Yash','Niranjan','Swanand','Shantanu','Siddhesh','Suraj','Sanket',
        'Kiran','Umesh','Prasad']

girls = ['Mrunal','Priyanka','Sanjeevani','Yashashri','Ashwini','Yashshree','Trupti','Mansi','Geeta','Sakshi',
         'Vaishnavi','Nikita','Sayali','Utkarsha','Shivani','Chaitali','Ruchita','Uma','Nandini','Priyanka',
         'Vaishnavi','Shital']

for i in range(20):
    boy = r.choice(boys)
    girl = r.choice(girls)
    print(f"Pair {i+1} : {boy} & {girl}")
    boys.remove(boy)
    girls.remove(girl)

    if not boys or not girls:
        print("Either List Is Empty")
        break

else:
    print("All Pairs Are Formed")