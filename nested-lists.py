n = int(input())
li = [[input() if j == 0 else float(input()) for j in range(2)] for i in range(n)]

def sortSecond(val): 
    return val[1]
  
li.sort(key = sortSecond) 
min2 = li[0][1]
li_final = []
for i in range(1,len(li)):
    if li[i][1] == min2:
        continue
    else:
        min2 = li[i][1]
        li_final.append(li[i][0])
        for j in range(i+1,len(li)):
            if li[j][1] == min2:
                li_final.append(li[j][0])
        break
li_final.sort()
for i in li_final:
    print(i)
