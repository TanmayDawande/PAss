n = input()
yorn = input()

if yorn.lower() == 'y':
    op = input()
    
    if op == '+':
        n2 = input()
        if int(n)>9 or int(n)<1:
            print("Invalid Input")
        else:
            result = int(n)+int(n2)
            print(f"The result of the operation is: {result}")
    elif op =='*':
        n2 = input()
        if int(n)>9 or int(n)<1:
            print("Invalid Input")
        else:
            result = int(n)*int(n2)
            print(f"The result of the operation is: {result}")
    elif op =='-':
        n2 = input()
        if int(n)>9 or int(n)<1:
            print("Invalid Input")
        else:
            result = abs(int(n)-int(n2))
            print(f"The result of the operation is: {result}")
    else:
        print("Invalid operation")
        
else:
    print(n)