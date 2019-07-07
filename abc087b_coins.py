A = int(input())
B = int(input())
C = int(input())
X = int(input())

count = 0
for a in range(A + 1):
    for b in range(B + 1):
        x = X - 500 * a - 100 * b
        if x >= 50:
            if x // 50 <= C:
                count += 1
        elif x == 0:
            count += 1

print(count)
