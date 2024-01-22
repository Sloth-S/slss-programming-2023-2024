from PIL import Image
import os

current_directory = os.path.dirname(__file__)

islight_name = "islight.png"  

islight_path = os.path.join(current_directory,islight_name)

islight=Image.open(islight_path)

width, height = islight.size

pixels = list(islight.getdata())

sum_brightness=list(islight.getdata())

i=0

for pixel in pixels :
    sum_brightness[i]=sum(pixel)/ 3 
    i=i+1

average_brightness = sum(sum_brightness) / len(sum_brightness)

print("The average brightness of the image is:",average_brightness)

if(average_brightness<128):
    print("It shows that it is LIGHT")
else:
    print("It shows that it is DARK")