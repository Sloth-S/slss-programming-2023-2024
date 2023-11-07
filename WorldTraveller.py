place = ['asia', 'europe', 'North America','South America', 'Africa', 'Oceania', 'Antarctica']
sum=0
for i in range(0,7):
    ans=input("Have you been to "+place[i]+".")
    if ans=="yes" or ans=="Yes" or ans=="YES":
        sum=sum+1

print("You have been to" + sum + "continents in the earth")
