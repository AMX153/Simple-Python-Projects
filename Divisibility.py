a = int(input("Enter start number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
        
for n in range(a, b):
    if n % c == 0:
        print(n, end=" ")
        continue