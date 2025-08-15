landr = input().split()
l = int(landr[0])
r = int(landr[1])
minSummaxSum = input().split()
minSum = int(minSummaxSum[0])
maxSUm = int(minSummaxSum[1])

a = 0
revNum = 0
step = 0
counter = 0
condition = False
sumNum = 0

for i in range(l, r, 1):
    if a==0:
        condition = False
    else:
        step = step+1
        
        
    for m in range(l, r, 1):
        a = m%10
        sumNum = sumNum + a
    
    a = int(a/10)
    for j in range(0, len(str(i))):
        b = i%10
        if i%b == 0:
            step = step+1
        else:
            condition = False
        
        revNum = a*pow(10, len(str(i))) + revNum
        
    for k in range(0, len(str(revNum))):
        b = revNum%10
        if revNum%b == 0:
            step = step+1
        else:
            condition = False
        b = int(b/10)
        
    if sumNum>=minSum and sumNum<=maxSUm:
        if step == 3:
            counter = counter+1
        
print(counter)
print(sumNum)
print(sumNum/counter)
    
        