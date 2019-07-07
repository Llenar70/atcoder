# -*- coding: utf-8 -*-
n, y = map(int, input().split())

ans = []
# 計算せずに出せる例外を書いておく
if 1000 * n > y:
    print("-1 -1 -1")
elif 1000 * n == y:
    print("0 0 " + str(n))
else:
    if 5000 * n == y:
        print("0 " + str(n) + " 0")
    else:
        if 10000 * n == y:
            print(str(n) + " 0 0")
        elif 10000 * n < y:
            print("-1 -1 -1")
        else:
            for i in range(n + 1):
                if ans:
                    break
                for j in range(n - i + 1):
                    if ans:
                        break
                    zangaku = y - 10000 * i - 5000 * j
                    if 1000 * (n - i - j) == zangaku:
                        ans = [i, j, n - i - j]
            if ans:
                print(str(ans[0]) + " " + str(ans[1]) + " " + str(ans[2]))
            else:
                print("-1 -1 -1")
