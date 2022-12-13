# Define a function largest which takes exactly three numeric parameters and return maximum

def largest(n1,n2,n3):
    type_check = [type(i) is int or type(i) is float for i in (n1,n2,n3)]
    if not all(type_check):
        return

    if n1 > n2:
        if n1 > n3:
            largest_no = n1
        else:
            largest_no = n2
    else:
        if n2 > n3:
            largest_no = n2
        else:
            largest_no = n3
    return largest_no

print("Largest =",largest(10,20,30))
