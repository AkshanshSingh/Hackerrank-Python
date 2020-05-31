def findSub():
    n1 = int(input())
    A = [int(x) for x in input().split()]
    n2 = int(input())
    B = [int(y) for y in input().split()]
    Aset = set(A)
    Bset = set(B)
    return Aset.issubset(Bset)
T = int(input())
for m in range(T):
    temp = findSub()
    print(temp)
