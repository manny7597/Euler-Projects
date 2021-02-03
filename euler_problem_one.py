n, z, x = 0, 0, 0
while n < 999:
    n = n + 3
    z = z + n
while x < 995:
    x = x + 5
    if x % 3 != 0:
        z = z + x
print(z) 