# -*- coding: utf-8 -*-
n = int(input())
plan_list = []
for i in range(n):
    t, x, y = map(int, input().split())
    plan_list.append([t, x, y])

ans_flag = True
for i in range(n):
    if i == 0:
        shortest_time = plan_list[i][1] + plan_list[i][2]
        if (plan_list[i][0] - shortest_time) % 2 != 0 or (plan_list[i][0] - shortest_time) < 0:
            print("No")
            ans_flag = False
            break
    else:
        shortest_time = abs(plan_list[i][
                            1] - plan_list[i - 1][1]) + abs(plan_list[i][2] - plan_list[i - 1][2])
        if (plan_list[i][0] - plan_list[i - 1][0] - shortest_time) % 2 != 0 or (plan_list[i][0] - plan_list[i - 1][0] - shortest_time) < 0:
            print("No")
            ans_flag = False
            break

if ans_flag:
    print("Yes")
