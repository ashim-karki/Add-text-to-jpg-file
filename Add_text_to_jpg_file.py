# Importing the PIL library 
from PIL import Image 
from PIL import ImageDraw 
from PIL import ImageFont 
from tkinter.font import Font
  
#Template 
img = Image.open('E:\Penguin.jpg') 



# Call draw Method to add 2D graphis in an image 
I1 = ImageDraw.Draw(img) 
  
#Font for 1
myFont1 = ImageFont.truetype('D:\Jupyter\Proxima.otf', 20)

#Font for 2
myFont2 = ImageFont.truetype('D:\Jupyter\Proxima.otf', 113)

#Font for 3
myFont3 = ImageFont.truetype('D:\Jupyter\Proxima.otf', 86) 

#Font for 4
myFont4 = ImageFont.truetype('D:\Jupyter\Proxima.otf', 83)

#Font for 5
myFont5 = ImageFont.truetype('D:\Jupyter\Proxima.otf', 82)

#Font for 6
myFont6 = ImageFont.truetype('D:\Jupyter\Proxima.otf', 83)

#Font for 7
myFont7 = ImageFont.truetype('D:\Jupyter\Proxima.otf', 118)
  


#Add Photo 
img2 = Image.open(r"E:\Penguin.JPG") 
img2 = img2.resize((100, 100))

#Text1
I1.text((200, 385), "PENGUIN", font=myFont2, fill =(255, 255, 255)) 

#Text2 
I1.text((1530, 813), "B&W", font=myFont1, fill =(255, 255, 255)) 

#Text3 
I1.text((1380, 584), "I", font=myFont6, fill =(255, 255, 255))

#Text4 
I1.text((2500, 584), "AAA", font=myFont3, fill =(255, 255, 255))

#Text5 
I1.text((1550, 1036), "BBB", font=myFont4, fill =(255, 255, 255))

#Text6 
I1.text((1710, 1322), "CCC", font=myFont5, fill =(255, 255, 255))

#Text7
I1.text((1850, 1650), "DDD", font=myFont7, fill =(255, 255, 255))

#Paste an Player Photo
img.paste(img2, (130,778))
  
#Display edited image without circle
img.show() 

#Save the edited image 
img.save(r'D:\PenguinWithText.jpg')

#Display edited image with circle
#mask_im = Image.new("L", img2.size, 0)
#draw = ImageDraw.Draw(mask_im)
#draw.ellipse((50,35,850,835), fill=255)
#final_im = img.copy()
#final_im.paste(img2, (235, 620), mask_im)
#final_im.show()  



