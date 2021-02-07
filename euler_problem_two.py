a, b, c = 1, 1, 0
while a < 4000000:
    if a % 2 == 0:
        c = c + a
    b = a - b
    a = a + b
print(c)