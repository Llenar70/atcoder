N, A, B = map(int, input().split())

S = []
for n in range(1, N + 1):
    c = n // 10000
    d = (n - 10000 * c) // 1000
    e = (n - 10000 * c - 1000 * d) // 100
    f = (n - 10000 * c - 1000 * d - 100 * e) // 10
    g = n - 10000 * c - 1000 * d - 100 * e - 10 * f
    keta = c + d + e + f + g
    if A <= keta and keta <= B:
        S.append(n)

ans = 0
for i in S:
    ans += i

print(ans)
