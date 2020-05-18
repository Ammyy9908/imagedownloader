from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import requests
import random

root = Tk()
root.title("Image Downloader")
root.geometry('1080x400')
root.resizable(0,0)

def download():
      key = keyword.get()
      if(len(key)<3):
            messagebox.showerror("Warning","Keyword is Required or must be a valid Keyword")
            keyword.delete(0, 'end')
      else:
            image_url = 'https://source.unsplash.com/2283x3008/?'+key
      
            try:
                  response = requests.get(image_url).content
                  random_num = random.randint(0,99999)
                  random_num = str(random_num)
                  image_name = random_num + '.jpg'
                  with open('downloads/'+image_name, 'wb') as handler:
                   handler.write(response)
                  print("Image SuccessFully Downloaded! with name "+image_name)
                  messagebox.showinfo("Success", "Image SuccessFully Downloaded! with name "+image_name+" in downloads")
                  keyword.delete(0, 'end')
            except:
                  print('Some Error')
                  messagebox.showerror("Error", "Internet Error!")
                  keyword.delete(0, 'end')


      



def close():
      messagebox.showinfo("Greeting","Thanks to Use This Image Downloader")
      exit()
      

# grid system starts from here
# mylabel1 = Label(root,text="My Label1")
# mylabel2 = Label(root,text="My Label2")

# mylabel1.grid(row=0,column=0)
# mylabel2.grid(row=1,column=0)

load = Image.open("logo.png")
load.resize((5,5), Image.ANTIALIAS)
render = ImageTk.PhotoImage(load)
img = Label(root, image=render)
img.image = render
img.place(x=500, y=100)

# EditText start from here

keyword = Entry(master=root,cursor="arrow",selectforeground="red",width="50")
keyword.place(x="300",y="200")

#Download Button

dnldbtn = Button(root,text="Download",fg="blue",padx=50,pady=10,command=download).place(x=350,y=250)
closebtn = Button(root,text="Exit",fg="red",padx=50,pady=10,command=close).place(x=580,y=250)

root.mainloop()

