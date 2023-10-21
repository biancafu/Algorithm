s = "abdba"

for i in range(len(s)-1,-1,-1):
    for j in range(i+1, len(s)):
        print(i,j)