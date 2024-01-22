#The program does not have a real data
import os
import csv
class record:
    def __init__(self):
        self.artist = "Jerry"
        self.title = "Payphone"
        self.danceability = 100


songs = list()

current_directory = os.path.dirname(__file__)

data_file = "data.csv"  

data_file_path=os.path.join(current_directory,  data_file)

with open(data_file_path, "r", encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)
    for single in csv_reader:
        songs.append(single)

    
    artistname=input("Problem 1: Enter an artist to know which songs are written by him/her, enter 'end' to end")
    while artistname != "end":
        for single in songs:
            if single[0]==artistname:
                sum=sum+1
                print(single[0])
        print(sum)
        artistname=input("Problem 1: Enter an artist to know which songs did he/she write, enter 'end' to end")
    
    for i in range(len(songs)):
        l=0
        for j in range(len(songs)-i-1):
            if(int(songs[j][3])<int(songs[j+1][3])):
                single=songs[j]
                songs[j]=songs[j+1]
                songs[j+1]=single
                l=1
        if l==0:
            break
    print("Problem 2: Songs after sorting by danceability:")
    for single in songs:
        print(single)
            

    

    
