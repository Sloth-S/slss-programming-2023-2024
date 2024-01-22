from PIL import Image
import os

def isred(a):
    r,g,b = a
    if r>150 and g+b<r/1.5:
        return True
    else:
        return False
    
def center_of_circ(picture_path):

    picture = Image.open(picture_path)

    data = picture.getdata()
    first = (0,0)
    last = (0,0)

    for x in range(picture.width):
        for y in range(picture.height):
            if isred(data[y*picture.width+x]):
                if first==(0,0):
                    first=(x,y)
                last=(x,y)
    a1,b1=first
    a2,b2=last
    print (first,last)
    print("(",(a1+a2)/2,",",(b1+b2)/2,")")

current_directory = os.path.dirname(__file__)


picture_file_name = "picture.png"  

picture_path = os.path.join(current_directory,  picture_file_name)


center_of_circ(picture_path)
