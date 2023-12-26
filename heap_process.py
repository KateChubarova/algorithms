class root:
    def __init__(self, processor, time):
        self.processor = processor
        self.time = time

    def __lt__(self, other):
        if self.time == other.time:
            return self.processor < other.processor
        return self.time < other.time


def swap(i, min_index):
    temp = H[i]
    H[i] = H[min_index]
    H[min_index] = temp


def create_heap():
    for processor in range(size):
        H.append(root(processor, 0))


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


def insert(p):
    print(H[0].processor, H[0].time)
    H[0].time = H[0].time + p
    lift_down(0)


H = []
# arr = [1, 2, 3, 4, 5]
arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
size = 4

create_heap()

for i in arr:
    insert(i)
