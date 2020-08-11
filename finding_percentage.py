n = int(input())
D = dict()
for i in range(n):
    li = input().split()
    D[li[0]] = (float(li[1])+float(li[2])+float(li[3])) / 3

query = input()
print("{0:.2f}".format(D[query]))
