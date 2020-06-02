n = int(input())
s = set(map(int, input().split()))
commands = int(input())

for i in range(commands):
    command = [x for x in input().split()]
    if len(command) > 1:
        command[1] = int(command[1])
    if command[0] == 'pop':
        s.pop()
    elif command[0] == 'remove':
        s.remove(command[1])
    else:
        s.discard(command[1])

print(sum(s))
