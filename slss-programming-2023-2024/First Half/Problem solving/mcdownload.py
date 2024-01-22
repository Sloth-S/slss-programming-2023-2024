burgers_answer = input("Do you want a burger for $5? ")
fries_answer = input("Do you want some fries for $3? ")

burgers_answer = burgers_answer.lower()
fries_answer = fries_answer.lower()

total_cost = 0.0

if burgers_answer == "yes":
    total_cost += 5.0

if fries_answer == "yes":
    total_cost += 3.0

total_cost_with_tax = total_cost * 1.14

print("Total cost with tax: $" + str(total_cost_with_tax))
