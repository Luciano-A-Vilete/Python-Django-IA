def max_of_three(a, b, c):
    if a >= b and a >= c:
        print(a)
    elif b >= a and b >= c:
        print(b)
    else:
        print(c)
        
def min_of_three(a, b, c):
    if a <= b and a <= c:
        print(a)
    elif b <= a and a <= c:
        print(b)
    else:
        print(c)