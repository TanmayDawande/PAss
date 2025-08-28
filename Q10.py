n = int(input())
k = int(input())
lst = []

for i in range(n-1):
    lst.append(int(input()))
    
for j in range(1, n-2, 1):
    
    for k in range(n-2):
        if lst[j] == lst[j+1]:
            print("No peak")
            break
    
        if (lst[j] > lst[j-1]) and (lst[j] > lst[j+1]):
            print(lst[j])
            
for l in range(n-1):
    temp = lst[l]
    for m in range(n-1):
        if temp==lst[m]: