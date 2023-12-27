def make_set(i):
    parent[i] = i
    index[i] = i


def find(i):
    while i != parent[i]:
        i = parent[i]
    return i


def union(i, j):
    i_id = find(i)
    j_id = find(j)
    if i_id == j_id:
        return
    if rank[i_id] > rank[j_id]:
        parent[j_id] = i_id
    else:
        parent[i_id] = j_id
        if rank[i_id] == rank[j_id]:
            rank[j_id] += 1

params = list(map(int, input().split()))
size = params[0]
equals = params[1]
not_equals = params[2]

rank = [0] * (size + 1)
index = [0] * (size + 1)
parent = [0] * (size + 1)

for i in range(size + 1):
    make_set(i)

for i in range(equals):
    unions = list(map(int, input().split()))
    union(unions[0], unions[1])

isPossible = True
for i in range(not_equals):
    unions = list(map(int, input().split()))
    if find(unions[0]) == find(unions[1]):
        print(unions[0], unions[1])
        isPossible = False
        break

if isPossible:
    print(1)
else:
    print(0)
