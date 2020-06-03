import builtins
n = int(input())
li = [int(x) for x in input().split()]
a = tuple(li)
print(hash(a)) 
