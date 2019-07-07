# -*- coding: utf-8 -*-
H, W = map(int, input().split())
S = []
for i in range(H):
    S.append(list(input()))
ans = []
for i in range(H):
    ans_s = []
    for j in range(W):
        if S[i][j] == "#":
            ans_s.append("#")
        else:
            bom = 0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if 0 <= i - x and i - x <= H - 1 and 0 <= j - y and j - y <= W - 1:
                        if not (x == 0 and y == 0):
                            if S[i - x][j - y] == "#":
                                bom += 1
            ans_s.append(str(bom))
    ans.append(ans_s)

for s in ans:
    print("".join(s))
