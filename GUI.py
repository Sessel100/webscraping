from tkinter import *
from Scraper import get_artist
from Scraper import get_streams


# root 
root= Tk()
root.title(' Data Analysis Project')
root.configure(bg='LIGHT BLUE')
root.geometry("500x600")

background_image = PhotoImage(file='Spotify-Logo.png')

# Create a label widget with the background image
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1.5, relheight=1.5)


# Accepts entry
entry = Entry (root)
entry.pack()



def clear_field():
    entry.delete(0,END)

def capture_text():
    global  text
    text = entry.get()

    return text

 
# root buttton
# For artist name
btn = Button(root , text = "Get Artist Name" , command= lambda: (capture_text() , clear_field(), get_artist(text)))
btn.pack()

# For artist lead streams
btn_2 = Button (root , text = "Get Artist Streams" , command = lambda: (capture_text() , clear_field(), get_streams(text)))
btn_2.pack()


root.mainloop()


# captured text feeds into open window function
