# WAP to count occurrences of vowel or number of vowels in string

s = input("Enter the string - ")
count = 0
for ch in s:
    if ch.lower() in 'aeiou':
        count = count + 1

# print("No. of vowels in "+s+" are",count)
print(f"No. of vowels in {s} are {count}")