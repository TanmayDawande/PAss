n = int(input())
list1 = []
list2 = []
temp = ""
temp2 = []
counter = 0
counter2 = 0

for i in range(0, n, 1):
    list1.append(input())
    
for j in range(0, n, 1):
    temp = str(list1[j])
    temp2 = list1[j]
    for k in range(len(list1[j])):
        char = temp2[k]
        for l in range(0, len(temp2), 1):
            if temp2[l] == " ":
                continue
            else:
                if temp2[l] == char:
                    break
                else:
                    counter2 += 1
        
        if "very" in temp:
            temp = temp.replace("very", "")
            if " " in temp:
                counter += 1
        elif "really" in temp:
            temp = temp.replace("really", "")
            if " " in temp:
                counter += 1
        elif "quite" in temp:
            temp = temp.replace("quite", "")
            if " " in temp:
                counter += 1
        else:
            continue
    list2.append(temp.capitalize())
    
print(str(list2))
print(counter+1)
print(counter2)
    
