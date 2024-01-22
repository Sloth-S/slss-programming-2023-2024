def maximum(x, y, z):
    if x > y:
        if x > z:
            return x
        else:
            return z
    if y > z:
        return y
    else:
        return z


a, b, c = map(int, input().split())
print(maximum(a, b, c))


