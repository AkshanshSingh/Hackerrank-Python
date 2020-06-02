n1 = int(input())
A = set(map(int, input().split()))
n2 = int(input())
B = set(map(int, input().split()))

symdiff = A.union(B) - A.intersection(B)
li = list(symdiff)
li.sort()
for element in li:
    print(element)
