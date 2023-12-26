H = [7, 6, 5, 4, 3, 2]
# H = [0, 1, 2, 3, 4, 5]
size = 6
# size = int(input())
# H = list(map(int, input().split()))
ans = []

def swap(i, min_index):
    ans.append((i,min_index))
    temp = H[i]
    H[i] = H[min_index]
    H[min_index] = temp


def lift_down(i):
    min_index = i
    left = i * 2 + 1
    right = i * 2 + 2
    if left < size and H[left] < H[min_index]:
        min_index = left
    if right < size and H[right] < H[min_index]:
        min_index = right
    if i != min_index:
        swap(i, min_index)
        lift_down(min_index)


for i in range((size // 2), -1, -1):
    lift_down(i)

print(len(ans))
for i in ans:
    print(i[0], i[1])
