def checkStrict(a,test):
    if a.issuperset(test) and (len(a) > len(test)):
        return True
    else:
        return False

A = set(map(int, input().split()))
n = int(input())

for i in range(n):
    test = set(map(int, input().split()))
    flag = checkStrict(A,test)
    if not(flag):
        print('False')
        break

else:
    print('True')
