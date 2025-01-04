
t = int(input())
for i in range(t):
    s = input()
    n = len(s)
    
    
    s1 = "a" + s
    if s1 != s1[::-1]:  
        print("YES")
        print(s1)
        continue

    
    s2 = s + "a"
    if s2 != s2[::-1]: 
        print("YES")
        print(s2)
    else:
        print("NO")
