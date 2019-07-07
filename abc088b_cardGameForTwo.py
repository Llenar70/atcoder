# -*- coding: utf-8 -*-
n = int(input())
listA = list(map(int, input().split()))

alice = 0
bob = 0
listA.sort(reverse=True)
for i, a in zip(range(n), listA):
    if i % 2 == 0:
        alice += a
    else:
        bob += a

print(alice - bob)
