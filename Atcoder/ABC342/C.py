import collections
import io
import sys


def debug_input():
    _INPUT = """\
34
supercalifragilisticexpialidocious
20
g c
l g
g m
c m
r o
s e
a a
o f
f s
e t
t l
d v
p k
v h
x i
h n
n j
i r
s i
u a

    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    N = int(input())
    S = input()
    Q = int(input())
    query = []
    for _ in range(Q):
        c, d = input().split()
        query.append((c, d))

    changes = dict()
    for alphabet in alphabets:
        changes[alphabet] = alphabet
        for c, d in query:
            if changes[alphabet] == c:
                changes[alphabet] = d

    # S = S.replace(c, d)
    S = S.translate(str.maketrans(changes))
    print(S)


if __name__ == "__main__":
    # debug_input()
    main()
