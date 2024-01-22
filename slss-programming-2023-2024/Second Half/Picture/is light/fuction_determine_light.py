r,g,b = map(int, input().split())
if (r+g+b)/3 >= 128:
    print("Dark")
else:
    print("Light")
