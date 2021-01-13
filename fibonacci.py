print("fibonacci series:")
n = int(input("enter nth term: "))
a = 0
b = 1
print(a)
print(b)
while n-2 > 0:
    c = a + b
    print(c)
    a = b
    b = c
    n -= 1
