total=int(input("How many courses do you have"))

sum=0

for i in range(0,total):
    k=int(input("What is your grade out of 5 "))
    sum=sum+k

mean=sum/total
print(mean)
if(mean<=1):
    print("You need work harder!")
elif(mean>=3):
    print("Great")
else:
    print("Not bad")
