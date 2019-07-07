n = int(input())

ans = 1
for i in range(n):
    ans *= i + 1
    if ans >= 1000000007:
        ans = ans % 1000000007

print(ans)
