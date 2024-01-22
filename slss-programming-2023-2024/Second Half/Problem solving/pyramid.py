def pyramid(x):
    for i in range(x):
        for j in range(i + 1):
            print("*", end="")
        print()

a = int(input("Enter the height of the pyramid: "))
pyramid(a)
