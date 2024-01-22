places = ['Asia', 'Europe', 'North America', 'South America', 'Africa', 'Oceania', 'Antarctica']
count = 0

for i in range(7):
    ans = input("Have you been to " + places[i] + "? ")
    if ans.lower() == "yes":
        count += 1

print("You have been to " + str(count) + " continents on Earth.")
