def calculate_pows():
    pows = [0] * 15
    for i in range(pow_size):
        pows[i] = pow(X, i)
    return pows


class hash:
    def __init__(self, size):
        self.strings = [[] for _ in range(size)]

    def add(self, string):
        hash_sum = self.calculate_hash(string)
        sequence = self.strings[hash_sum]
        if string not in sequence:
            self.strings[hash_sum].append(string)

    def delete(self, string):
        hash_sum = self.calculate_hash(string)
        sequence = self.strings[hash_sum]
        if string in sequence:
            self.strings[hash_sum].remove(string)

    def find(self, string):
        hash_sum = self.calculate_hash(string)
        sequence = self.strings[hash_sum]
        if string in sequence:
            print('yes')
        else:
            print('no')

    def check(self, i):
        print(' '.join(self.strings[i][::-1]))

    def calculate_hash(self, string):
        hash_sum = 0
        for index, char in enumerate(string):
            hash_sum += ord(char) * pows[index] % p
        return hash_sum % p % m


m = int(input())
n = int(input())
S = 1000000007
p = 1000000007
X = 263
pow_size = 15

pows = calculate_pows()
hash = hash(m)

for i in range(n):
    command = input().split()
    if command[0] == 'add':
        hash.add(command[1])
    elif command[0] == 'check':
        hash.check(int(command[1]))
    elif command[0] == 'find':
        hash.find(command[1])
    elif command[0] == 'del':
        hash.delete(command[1])

# hash.add('world')
# hash.add('HellO')
# hash.check(4)
# hash.find('World')
# hash.find('world')
# hash.delete('world')
# hash.check(4)
# hash.delete('HellO')
# hash.add('luck')
# hash.add('GooD')
# hash.check(2)
# hash.delete('good')

