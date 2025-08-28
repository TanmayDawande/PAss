str1 = input()
str2 = input()
str5 = ""
str6 = ""
count = 0
str7 = ""
tempChar = ""
visted = ""

str3 = "".join(str1+str2)
str4 = list(str3)
print(f"Concatenated String: {str3}")

for i in range(0, len(str4)-1, 1):#vowel Removed
    if str4[i].lower() not in "aeiou":
        str5 = str5 + str4[i]
print(f"Vowel removed string: {str5}")

for j in range(len(str5)-1, -1, -1):#reversed string
    str6 = str6 + (list(str5))[j]
print(f"Reversed String: {str6}")

for k in range(0, len(str6), 1):#Case Converted
    str7 = str7 + ((list(str6))[k]).swapcase()
print(f"Case Converted Final String: {str7}")

print("Character frequency count in the final string: ")
liststr7 = list(str7)
for l in range(len(liststr7)):
    tempChar = liststr7[l]
    if tempChar in visted:
        continue
    count = 0
    for m in range(len(liststr7)):
        if tempChar == liststr7[m]:
            count = count+1
    print(f"{tempChar} : {count}")
    visted = visted + tempChar
        


    
