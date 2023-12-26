str = input()
stack = []
index_stack = []
for index, char in enumerate(str):
    if char in ['(', '[', '{']:
        stack.append(char)
        index_stack.append(index)
    elif char in [')', ']', '}']:
        if len(stack) == 0:
            index_stack.append(index)
            break
        top = stack.pop()
        top_index = index_stack.pop()
        if (top == '[' and char != ']') or (top == '(' and char != ')') or (top == '{' and char != '}'):
            index_stack.append(index)
            break
if len(index_stack) == 0 and len(stack) == 0:
    print('Success')
else:
    print(index_stack.pop() + 1)