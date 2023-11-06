

ans1=input("Do you want a burgern for 5 ")

ans2=input("Do you want some fries for 3 ")

ans1.lower()

ans2.lower()

if(ans1=="yes"):
    money=5.0

if(ans2=="yes"):
    money=money+3.0

money=money*1.14

print(money)