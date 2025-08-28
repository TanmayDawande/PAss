n = int(input())
tar = int(input())
transAmt = input().split()

main = list(map(int, transAmt))
temp2 = float("-inf")
condition = False
sUm = 0
pairs = set()

for i in range(n):
    for j in range(i+1, n):
        if main[i] + main [j] == tar:
            pair = tuple(sorted((main[i], main[j])))
            if pair not in pairs:
                pairs.add(pair)
                print(f"{pair[0]} {pair[1]}")
                condition = True
                
                
if condition == False:
    print("No pairs")
    
for l in range(0, n, 2):#adding abs value of even indices
    sUm = sUm + abs(main[l])
    
for k in range(n-1):#multiplying adjacent to check maximum product
    product = main[k] * main[k+1]
    if product > temp2:
        temp2 = product
    

print(temp2)
print(sUm)


    