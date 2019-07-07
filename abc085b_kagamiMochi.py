# -*- coding: utf-8 -*-
n = int(input())
listD = []
for i in range(n):
    listD.append(int(input()))

print(len(list(set(listD))))
