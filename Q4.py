import math

n = int(input())
tar = int(input())
transAmt = input().split()

main = list(map(int, transAmt))
temp = 0
temp2= 0
condition = False
temp3 = 0
tempList = []
sUm = 0

for i in range(0, n-1, 1):
    temp = main[i]
    for j in range(0, n-1, 1):
        if i == j:
            continue
        else:
            if temp + main[j] == tar:#checking if sum equals given target value
                print(f"{temp} {main[j]}")
                transAmt.pop(j)
                condition = True
    
for l in range(0, n, 2):#adding abs value of even indices
    temp3 = main[l]
    sUm = sUm + abs(temp3)
    
for k in range(0, n-1, 1):#multiplying adjacent to check maximum product
    if math.prod(main[k:k+1:1])>math.prod(main[k+1:k+2:1]):#did not work
        temp2 = math.prod(main[k:k+1:1])
    else:
        temp2 = math.prod(main[k+1:k+2:1])
    
    
if condition == False:
    print("No pairs")
    
print(temp2)
print(sUm)


    