a = [None] * 4
questions = ["Did you eat?", "Did you study?", "Did you do your laundry?", "Did you call your grandma?"]

for i in range(4):
    print(questions[i])
    a[i] = input().lower()

p = sum(1 for answer in a if answer == "yes")

if p == 0:
    print("I'm coming over")
elif p < 3:
    print("Ok")
else:
    print("Good!")
