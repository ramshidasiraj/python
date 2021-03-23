a = int(input(" enter the first number : "))
b = int(input("enter the second number : "))
c = int(input("enter the third number : "))
if a>b:
    if a>c:
        print("a is large")
    else:
        print("c is large")
elif b>c:
    print("b is large")
else:
    print("c is large")
