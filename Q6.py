n = int(input())
num_str = str(n)
length = len(num_str)
list1 = []
flag = True

temp = num_str
for i in range(length):
    list1.append(int(temp))
    temp = temp[-1] + temp[:-1]
    
for val in list1:
    print(val)
    
    if val<2:
        flag = False
    else:
        for j in range(2, int(val**0.5)+1):
            if val % j == 0:
                flag = False
                break
            
if flag:
    print("true")
else:
    print("false")
