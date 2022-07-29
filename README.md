
# Random Imgur Image

This python script fetches and displays a pseudo-random image from imgur.com using the urllib3 library in python.


## Setup

Before running Main.py, you can change a couuple lines of code to best suit your needs.

Line 9 - Chnage the working directory of the project
```
os.chdir(r'D:\code\cmnoNow\random_imgur_image')  # My working dir
```

Line 15 - Change the path and name of the downloaded imgur image
```
download_image_path = 'downloaded.png'
```

Line 89-91 - Change Keybindings for fetching a new image and hiding the current image
You can see a full list of Tkinter keys via [this link](https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/key-names.html).
```
root.bind('<Return>', reload_image)

root.bind('<BackSpace>', hide_image)
```

    