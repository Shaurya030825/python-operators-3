x=5
if (type(x) is int):
    print("True")
else:
    print("False")

x= 5.5
if (type(x) is not float):
    print("False")
else:
    print("True")

x=20
y=20
if(x is y):
    print("x &and y has same identity.")
else:
    print("x & y has different identity.")

y=30
if (x is not y):
    print("x & y has different identity.")