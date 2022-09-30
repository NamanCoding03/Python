def swap(a, b):
    #Using XOR 
    a = a^b
    b = a^b
    a = a^b
    return a,b

    a = int(input())
    b = int(input())
    swap(a,b)
