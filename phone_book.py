def process(line):
    commands = line.split()
    command = commands[0]
    phone = int(commands[1])
    if command == 'add':
        name = commands[2]
        arr[phone] = name
    elif command == 'find':
        name = arr[phone]
        if name is not None:
            print(name)
        else:
            print('not found')
    elif command == 'del':
        arr[phone] = None


arr = [None] * 10000001

n = int(input())

for i in range(n):
    process(input())
