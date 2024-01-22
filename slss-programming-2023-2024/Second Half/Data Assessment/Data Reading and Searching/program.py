import os
import csv
class record:
    def __init__(self):
        self.name = "Jerry"
        self.food = "Air"
        self.movie = "Interstellar"
        self.card = 0
        self.city = "Jinan"

people = list()

current_directory = os.path.dirname(__file__)

data_file = "data_example.csv"

data_file_path=os.path.join(current_directory,  data_file)

with open(data_file_path, "r", encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)
    first = next(csv_reader)
    people.append(first)
    second = next(csv_reader)
    people.append(second)
    print("Problem 1:The information of the second person:", people[1])
    for person in csv_reader:
        people.append(person)
    pos=int(input("Problem 2: The information of the n-th people (input an int value n; input 0 to end this): "))
    while pos>0:
        print("The information of the",pos,"-th person:", people[pos-1])
        pos=int(input("The information of the n-th people (input an int value n; input 0 to end this): "))
    print("Problem 3: Every line has already stored")
    
    input_food=input("Problem 4: Enter a food name to know how many people like this food; enter 'end' to end ")
    while input_food != "end":
        sum=0
        for person in people:
            print(person[1].lower())
            if person[1].lower()==input_food.lower():
                sum=sum+1
        print(sum)
        input_food=input("Problem 4: Enter a food name to know how many people like this food; enter 'end' to end ")
    
    start=input("Problem 5: Enter a letter to know how many people start with this letter; enter 'end' to end ")
    while start != "end":
        sum=0
        for person in people:
            if person[0][0]==start:
                sum=sum+1
        print(sum)
        start=input("Problem 5: Enter a letter to know how many people start with this letter; enter 'end' to end ")
    
    input_place=input("Problem 6: Enter a place to know how many people come from there; enter 'end' to end ")
    while input_place != "end":
        sum=0
        for person in people:
            if person[4].lower() ==input_place.lower() :
                sum=sum+1
        print(sum)
        input_place=input("Problem 6: Enter a place to know how many people come from there; enter 'end' to end ")
    
    sum=0
    counter=0
    for person in people:
        if int(person[3])%2==0:
            sum=sum+1
        counter=counter+1
    print("Problem 7: There are ",sum,"/",counter," people's cards are even number ")

    food=list()
    counter=list()
    for person in people:
        l=0
        for i in range(len(food)):
            if(person[1]==food[i]):
                counter[i]=counter[i]+1
                l=1
                break
        if l==0:
            food.append(person[1])
            counter.append(1)
    maxfood=""
    maxcount=0
    for i in range(len(counter)):
        if(counter[i]>maxcount):
            maxfood=person[i]
            maxcount=counter[i]
    print("Extra problem: The most favorite food is ", maxfood," and there are ", maxcount ,"people like it")



