def methods(li,n):
    li_1 = []
    for i in range(n):
        if li[i][0] == 'print':
            print(li_1)
        elif li[i][0] == 'sort':
            li_1.sort()
        elif li[i][0] == 'reverse':
            li_1.reverse()
        elif li[i][0] == 'pop':
            li_1.pop()
        elif li[i][0] == 'remove':
            li_1.remove(int(li[i][1]))
        elif li[i][0] == 'append':
            li_1.append(int(li[i][1]))
        else:
            a = int(li[i][1])
            if a < len(li_1):
                li_1.insert(int(li[i][1]),int(li[i][2]))
            else:
                li_1.append(int(li[i][2]))

n = int(input())
li = [[x for x in input().split()] for i in range(n)]
methods(li,n)
