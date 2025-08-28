landr = input().split()
l = int(landr[0])
r = int(landr[1])
minSummaxSum = input().split()
minSum = int(minSummaxSum[0])
maxSum = int(minSummaxSum[1])

counter = 0
totalSum = 0

for i in range(l, r+1, 1):
    condition = True
    sumNum = 0
    temp = i
    digits = []
    
    while temp > 0:
        d = temp%10
        if d == 0:
            condition = False
            break
        digits.append(d)
        sumNum +=d
        temp //=10
        
    if not condition:
        continue
    
    for d in digits:
        if i % d != 0:
            condition = False
            break
    if not condition:
        continue
    
    if not (minSum <= sumNum <= maxSum):
        continue
    
    revNum = int(str(i)[::-1])
    
    for d in digits:
        if revNum % d != 0:
            condition = False
            break
        
    if condition:
        counter += 1
        totalSum += i
        
        
        
print(counter)
print(totalSum)
if counter > 0:
    print(f"{totalSum/counter:.2f}")
else:
    print("0.00")
