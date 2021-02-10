x = 2
y = 600851475143
while y > x:
    if y % x != 0:
        x += 1
    else: y = y/x
print(x)