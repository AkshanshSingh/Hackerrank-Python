n1 = int(input())
E = set(map(int, input().split()))
n2 = int(input())
F = set(map(int, input().split()))

symdiff = E.symmetric_difference(F)
print(len(symdiff))
