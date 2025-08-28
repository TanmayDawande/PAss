n = int(input())
k = int(input())
parts = input().split()
lst = []


for i in range(n):
    lst.append(int(parts[i]))
    
peaks = []
        
for j in range(1, n-1):
    
    if (lst[j] > lst[j-1]) and (lst[j] > lst[j+1]):
        peaks.append(lst[j])

if len(peaks) == 0:
    print("No peak")
else:
    for p in peaks:
        print(p)
    
majority = -1
for l in range(n):
    temp = lst[l]
    count = 0
    for m in range(n):
        if temp == lst[m]:
            count += 1
        if count > n//2:
            majority = temp
            break
        
if majority != -1:
    print(majority)
else:
    freq = []
    for i in range(n):
        temp = lst[i]
        count = 0
        for j in range(n):
            if lst[j] == temp:
                count += 1
        pair = [temp, count]
        if pair not in freq:
            freq.append(pair)
    
    for i in range(len(freq)):
        for j in range(i+1, len(freq)):
            if freq[j][1] > freq[i][1]:
                freq[i], freq[j] = freq[j], freq[i]
            
                
    freq_str = ""
                
    for i in range(len(freq)):
        freq_str = freq_str + str(freq[i][0])
        if  i != len(freq)-1:
            freq_str = freq_str + " "
    print(freq_str)
            

max_sum = 0    

for i in range(n-k+1):
    s = 0
    for j in range(i, i+k):
        s += lst[j]
    if s>max_sum:
        max_sum = s

print(max_sum)
