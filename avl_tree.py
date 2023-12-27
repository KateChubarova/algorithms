class root:
    def __init__(self, key, left=-1, right=-1):
        self.key = key
        self.left = left
        self.right = right


def print_tree_pre_order(index):
    print(tree[index].key, end=' ')
    if tree[index].left != -1:
        print_tree_pre_order(tree[index].left)
    if tree[index].right != -1:
        print_tree_pre_order(tree[index].right)


def print_tree_in_order(index):
    if tree[index].left != -1:
        print_tree_in_order(tree[index].left)
    print(tree[index].key, end=' ')
    if tree[index].right != -1:
        print_tree_in_order(tree[index].right)


def print_tree_post_order(index):
    if tree[index].left != -1:
        print_tree_post_order(tree[index].left)
    if tree[index].right != -1:
        print_tree_post_order(tree[index].right)
    print(tree[index].key, end=' ')


n = int(input())
tree = [None] * n
top = 0
for i in range(n):
    line = input().split()
    tree[i] = root(int(line[0]), int(line[1]), int(line[2]))

print_tree_pre_order(top)
print()
print_tree_in_order(top)
print()
print_tree_post_order(top)
