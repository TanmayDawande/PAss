n = int(input())
passwords = []
temp  = []

for i in range(0, n, 1):
    passwords.append(input())
    
for j in range(0, n, 1):
    for k in range(0, len(passwords[j],), 1):
        temp = [passwords[k]]
        for l in range(0, len(temp), 1):
            if temp[l] in "!@#$%^&*":
                temp.pop[l]