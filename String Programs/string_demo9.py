# WAP to count occurrences of consonants or number of consonnants in string

s = input("Enter the string - ")
count = 0
for ch in s:
    if ch.lower() not in 'aeiou':
        count = count + 1

# print("No. of consonants in "+s+" are",count)
print(f"No. of consonants in {s} are {count}")