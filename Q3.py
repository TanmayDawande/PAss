n = int(input())
lst = []
spec_char = {"!", "@", "#", "$", "%", "^", "&", "*"}


for i in range(n):
    lst.append(input())

for j in range(n):
    password = lst[j]
    specials = []
    normals = []
    
    for ch in password:
        if ch in spec_char:
            specials.append(ch)
        else:
            normals.append(ch)
            
    if len(specials) >= 2:
        print("".join(specials) + "".join(normals))
    else:
        print("Invalid")
            
                
