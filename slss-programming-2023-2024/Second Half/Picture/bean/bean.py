from PIL import Image
import os

def iswhite(a):
    r,g,b = a
    if r>200 and g>200 and b>200:
        return True
    else:
        return False
    
def islight(a):
    r,g,b=a
    if r>50 and g>50 and b>50 and r+g>=b and r+b>=g and b+g>=r:
        return True
    else:
        return False


def color(p):
    x,y,z=p 
    A=150
   # (150,0,0)
    B=A/3
    c=[]
    mean= (x+y+z)/3
    if(x>y and x>z):
        x=x-mean/2
    elif (y>x and y>z):
        y=y-mean/2
    else:
        z=z-mean/2

    c.append(abs(x-A)+y+z)
    c.append(x+abs(y-A)+z)
    c.append(x+y+abs(z-A))
    
    c.append(abs(x-B)+abs(y-B)+z)
    c.append(abs(x-B)+y+abs(z-B))

    c.append(x+y+z)
    
    min=1000
    minind=-1

    for i in range(6):
        if c[i]<min:
            min=c[i]
            minind=i

    return minind
    

current_directory = os.path.dirname(__file__)

beans_name = "beans.png"  

beans_path = os.path.join(current_directory,beans_name)

output_name="output.png"

output_path = os.path.join(current_directory, output_name)

beans=Image.open(beans_path)

output=Image.open(beans_path)

width, height = beans.size

pixels = list(beans.getdata())

sum=[0,0,0,0,0,0,0,0]

count=0
for w in range(width):
    for h in range(height):
        if(iswhite(pixels[h*width+w])):
            # print(w,h)
            # print(pixels[h*width+w])
            queue=[]
            queue.append((w,h))
            c=0
            cx=-1
            cy=-1
            while len(queue)>0:
                c=c+1
                x,y=queue.pop(0)
                output.putpixel( (x,y), (0,0,0))

                if(0<=y+1<height and 0<=x<width):
                    if(islight(pixels[(y+1)*width+x])):
                        pixels[(y+1)*width+x]=(0,0,0)
                        queue.append((x,y+1))
                    elif(pixels[(y+1)*width+x]!=(0,0,0)):
                        if(cx==-1):
                            cx=x
                            cy=y+1
                
                if(0<=y-1<height and 0<=x<width):
                    if(islight(pixels[(y-1)*width+x])):
                        pixels[(y-1)*width+x]=(0,0,0)
                        queue.append((x,y-1))
                    elif(pixels[(y-1)*width+x]!=(0,0,0)):
                        if(cx==-1):
                            cx=x
                            cy=y-1
                
                if(0<=y<height and 0<=x+1<width):
                    if(islight(pixels[y*width+x+1])):
                        pixels[y*width+x+1]=(0,0,0)
                        queue.append((x+1,y))
                    elif(pixels[(y)*width+x+1]!=(0,0,0)):
                        if(cx==-1):
                            cx=x+1
                            cy=y
                
                if(0<=y<height and 0<=x-1<width):
                    if(islight(pixels[y*width+x-1])):
                        pixels[y*width+x-1]=(0,0,0)
                        queue.append((x-1,y))
                    elif(pixels[(y)*width+x-1]!=(0,0,0)):
                        if(cx==-1):
                            cx=x-1
                            cy=y
            
            if(c>=30):
                count=count+1
                k=color(pixels[cy*width+cx])
                sum[k]=sum[k]+1
    

output.save(output_path, "PNG")

print("The number of beans is ",count)


print("The number of red beans is ",sum[0])
print("The number of green beans is ",sum[1])
print("The number of blue beans is ",sum[2])
print("The number of yellow beans is ",sum[3])
print("The number of pink or purple beans is ",sum[4])
print("The number of black beans is ",sum[5])
