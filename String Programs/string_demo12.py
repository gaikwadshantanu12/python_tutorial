# WAP to print index number of each occurrence of substring in string

s = input("Enter your string - ")
sub = input("Enter substring to search - ")
index = s.find(sub)

while index != -1:
    print(index)
    index = s.find(sub,index+1)