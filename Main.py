import random
import string
from tkinter import *
from io import BytesIO
from PIL import ImageTk, Image, UnidentifiedImageError
import os
import urllib3
from time import time

os.chdir(r'D:\code\cmnoNow\random_imgur_image') #My working dir

http = urllib3.PoolManager()

defImg = Image.open('imgur.png') #default imgur image not found png

download_image_path = "downloaded.png"

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

def get_random_imgur_url(length, chars):
    final = 'https://imgur.com/'
    for i in range(length):
        final += random.choice(chars)
    final += ".jpg"
    return final

def returnImage(imgur_url, headers = None):
    if headers is None:
        headers = hdr

    response = http.request("GET", imgur_url, headers = headers)
    if response.status == 404:
        return False, ''

    try:
        image = Image.open(BytesIO(response.data))
        return True, image
    except UnidentifiedImageError:
        return False, ''

def download_random_imgur_image(chars_length, chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.digits):
    length = chars_length

    imgur_url = get_random_imgur_url(length, chars)
    
    success, image = returnImage(imgur_url)

    if not success or image is None or image == defImg: # If image is imgur.png, or it doesn't exist, get a new one
        download_random_imgur_image(chars_length) # Recursion!
    else:
        image.save(download_image_path)


root = Tk()

img = ImageTk.PhotoImage(Image.open("temporary.png"))
tkinter_panel = Label(root, image = img)
tkinter_panel.pack(side = "bottom", fill = "both", expand = "yes")

def reload_image(event):
    now = time()
    download_random_imgur_image(5)
    print(time()-now)
    imgur_image = ImageTk.PhotoImage(Image.open(download_image_path))
    tkinter_panel.configure(image=imgur_image)
    tkinter_panel.image = imgur_image

root.bind("<Return>", reload_image)

root.mainloop()