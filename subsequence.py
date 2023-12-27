# рубина-карпа

P = 10001
X = 1
sub_sequence = 'aba'
sequence = 'abacaba'
ans = []


def hash(sequence):
    h = 0
    for index, char in enumerate(sequence):
        h += ord(char) % P * pows[index] % P
    return h % P


def should_add(hash, i):
    if hash == hash_sub_sequence:
        if sub_sequence == sequence[i:i + p]:
            ans.append(i)


p = len(sub_sequence)
start = len(sequence) - p
pows = [0] * p

def calculate_pows():
    for i in range(p):
        pows[i] = pow(X,i)


calculate_pows()

hash_sub_sequence = hash(sub_sequence)
hashi_1 = hash(sequence[start:start + p])
should_add(hashi_1, start)

for i in range(start - 1, -1, -1):
    ti_p = ord(sequence[i + p]) % P * pows[p - 1] % P
    hashi_1 = ((hashi_1 - ti_p) * X % P + ord(sequence[i]) % P) % P
    should_add(hashi_1, i)

for i in range(len(ans) - 1, -1, -1):
    print(ans[i], end=' ')
