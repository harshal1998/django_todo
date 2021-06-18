n = int(input("enter year:"))
a = n // 100
b = n % 100
if b == 0:
    print("century =", a)
else:
    print("century =", a + 1)
