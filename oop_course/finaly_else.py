def div(a, b):
    try:
        return  a / b
    except ZeroDivisionError as z:
        return z
res = 0
try:
    x, y = map(int, input().split())
    res = div(x, y)
except ValueError as  z:
    print(z)

print(res)


