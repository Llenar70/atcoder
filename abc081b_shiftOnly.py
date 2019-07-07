# -*- coding: utf-8 -*-
n = int(input())
listA = list(map(int, input().split()))
ans = 0
flag = True
# まずは全部偶数か確認して奇数があったらFalseにする
for a in listA:
    if a % 2 != 0:
        flag = False

# 奇数があったら操作を行わず0を表示
if flag is False:
    print(0)
# とりあえず全部偶数の場合
else:
    ans = 0
    while True:
        listA = list(map(lambda x: x // 2, listA))
        ans += 1
        for a in listA:
            if a % 2 != 0:
                flag = False
        if flag is False:
            print(ans)
            break
