# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two
# 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

y, ans = 999, 0
while y > 99:
    x = 999
    while x > 99:
        z = str(x * y)
        if z[:3] == z[-1] + z[-2] + z[-3]:
            if int(z) > ans:
                ans = int(z)
            break
        else: x = x - 1
    y = y - 1
print(ans)