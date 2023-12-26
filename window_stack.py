from max_stack import stack

# window = 1
size = int(input())
array = list(map(int, input().split()))
window = int(input())

stack1 = stack(window)
stack2 = stack(window)

# array = [2, 1, 5]
# array = [2, 7, 3, 1, 5, 2, 6, 2]

ans = []

for i in array:
    if not stack1.is_full():
        if not stack2.is_empty():
            ans.append(max(stack2.max(), stack1.max()))
            stack2.pop()
        stack1.push(i)
    else:
        while not stack1.is_empty():
            stack2.push(stack1.pop())

        ans.append(max(stack1.max(), stack2.max()))
        stack2.pop()
        stack1.push(i)

print('stack1 ', stack1.stack)
print('stack1_max', stack1.max_stack)

print('stack2 ', stack2.stack)
print('stack2_max ', stack2.max_stack)

ans.append(max(stack1.max(), stack2.max()))

print(ans)


