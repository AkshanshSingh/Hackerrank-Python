n,m = input().split()
n,m= int(n),int(m)
li = [int(x) for x in input().split()]
a = set()
b = set()
happiness = 0
for i in input().split():
    a.add(int(i))
for j in input().split():
    b.add(int(j))
for k in li:
    if k in a:
        happiness += 1
    elif k in b:
        happiness -= 1
print(happiness)
