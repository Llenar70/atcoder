H, W = map(int, input().split())

S = []

for i in range(H):
    S.append(list(input()))

flag = True

for i in range(H):
    for j in range(W):
        s_list = []
        if S[i][j] == "#":
            # right
            if j + 1 < W:
                s_list.append(S[i][j + 1])
            # left
            if j - 1 >= 0:
                s_list.append(S[i][j - 1])
            # up
            if i - 1 >= 0:
                s_list.append(S[i - 1][j])
            # down
            if i + 1 < H:
                s_list.append(S[i + 1][j])
            if "#" not in s_list:
                # print(i, j, s_list)
                flag = False


if flag:
    print("Yes")
else:
    print("No")
