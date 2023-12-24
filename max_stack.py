

class stack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def pop(self):
        self.max_stack.pop()
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)
        if len(self.max_stack) > 0:
            max_top = self.max_stack[-1]
        else:
            max_top = -1
        if item > max_top:
            self.max_stack.append(item)
        else:
            self.max_stack.append(max_top)

    def max(self):
        print(self.max_stack[-1])

stack = stack()
n = int(input())
for i in range(n):
    command = input()
    commands = command.split()
    if commands[0] == 'push':
        stack.push(int(commands[1]))
    elif commands[0] == 'max':
        stack.max()
    elif commands[0] == 'pop':
        stack.pop()