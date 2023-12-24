n = int(input())
roots = list(map(int, input().split()))
main_root = None
##test 1
# n = 10
# roots = [9, 7, 5, 5, 2, 9, 9, 9, 2, -1]
#ans = 4
##test 2
# n = 5
# roots = [4, -1, 4, 1, 1]
#test3
# n = 5
# roots = [-1, 0, 4, 0, 3]

# test4
# n = 6
# roots = [-1, 0, 1, 2, 3]
#ans = 5

tree = [[] for _ in range(n)]

class Root:
    def __init__(self, value):
        self.value = value
        self.roots = []

    def add_root(self, root):
        self.roots.append(root)

    def get_roots(self):
        return self.roots


def create_tree():
    global main_root
    for index, parent in enumerate(roots):
        if parent == -1:
            main_root = index
        else:
            tree[parent].append(index)


create_tree()


def print_tree(r):
    print(r)
    for i in tree[r]:
        print_tree(i)


# print_tree(main_root)
# for i in tree:
#     print(i)
# max_height = 0


def height(r):
    max_child_height = 0
    for child in tree[r]:
        child_height = height(child)
        max_child_height = max(child_height, max_child_height)
    return max_child_height + 1


print(height(main_root))
