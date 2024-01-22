print("I will decode if you can join the dark side")

capes_answer = input("Do you like capes? ")
color_answer = input("Is red your favorite color? ")

capes_answer = capes_answer.lower()
color_answer = color_answer.lower()

if capes_answer == "yes" or color_answer == "yes":
    print("Welcome to the Dark Side")
else:
    print("You are on the Light Side")
