# WAP to read digit and print it in words

switch = {0:"ZERO",
          1:"ONE",
          2:"TWO",
          3:"THREE",
          4:"FOUR",
          5:"FIVE",
          6:"SIX",
          7:"SEVEN",
          8:"EIGHT",
          9:"NINE"}

d = int(input("Enter the digit - "))
print(switch.get(d,"Invalid Input"))