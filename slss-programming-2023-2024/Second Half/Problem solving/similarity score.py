a = input("Please enter hobbies, separated by spaces\nPerson 1: ")
b = input("\nPerson 2: ")

a = a.lower()
b = b.lower()

c = ""
ans = 0

for i in range(len(a)):
    if a[i] != ' ':
        c += a[i]
    else:
        if c in b:
            ans += 1
        c = ""

print("\nYou have", ans, "hobbies in common.")
