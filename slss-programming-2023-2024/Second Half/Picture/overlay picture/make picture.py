from PIL import Image
import os

def isgreen(a):
    r,g,b = a
    if g>150 and r+b<g:
        return True
    else:
        return False
    
def overlay_images(background_path, overlay_path, output_path):

    background = Image.open(background_path)
    overlay = Image.open(overlay_path)


    overlay = overlay.resize(background.size)


    overlay = overlay.convert("RGBA")
    data = overlay.getdata()
    new_data = []
    for item in data:
        l=1
        if isgreen(item[:3]):
            new_data.append((0, 0, 0, 0))  
        else:
            new_data.append(item)



    overlay.putdata(new_data)

    result = Image.alpha_composite(background.convert("RGBA"), overlay)


    result.save(output_path, "PNG")


current_directory = os.path.dirname(__file__)


background_file_name = "background.png"  
overlay_file_name = "child.png"  
output_file_name = "output.png"   

background_path = os.path.join(current_directory,  background_file_name)
overlay_path = os.path.join(current_directory,  overlay_file_name)
output_path = os.path.join(current_directory, output_file_name)


overlay_images(background_path, overlay_path, output_path)
