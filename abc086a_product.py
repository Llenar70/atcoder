a, b = map(int, input().split())

c = a * b
joyo = c % 2

if joyo == 0:
    print("Even")
else:
    print("Odd")
