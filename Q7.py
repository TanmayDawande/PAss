arr = list(map(int, input().split()))

arr = sorted(list(set(arr)))

longest = []
current = [arr[0]]

for i in range(1, len(arr)):
    if arr[i] == arr[i-1] + 1:
        current.append(arr[i])
    else:
        if len(current) > len(longest):
            longest = current
        current = [arr[i]]
        
if len(current) > len(longest):
    longest = current
    
print(tuple(longest))
