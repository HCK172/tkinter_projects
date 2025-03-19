from tkinter import * 
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import string
import json

LAVENDER ="#E5D9F2"

#------- generate the password -------#

def generate_password():
    custom_special_chars = "!@#$%&*+()"

    nr_letter = random.sample(string.ascii_letters,6)  
    numbers = random.sample(range(1,10),4)
    nr_number = [ str(num) for num in numbers]
    nr_char = random.sample(custom_special_chars,2)

    password_list = nr_letter + nr_char + nr_number
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0,password)


#------ password saved into a file -----#
def save():
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()

    new_data = {
         website: {
              "email": email_username,
              "password":password
         }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("password_manager/data.json","r") as json_file:
                data = json.load(json_file)
               
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            with open("password_manager/data.json","w") as json_file:
                json.dump(new_data, json_file, indent=4)
        else: 
            data.update(new_data) 
            with open("password_manager/data.json","w") as json_file:
                json.dump(data, json_file, indent=4)
                
        finally:
            clear_entry()

def clear_entry():
    website_entry.delete(0, END)
    email_username_entry.delete(0,END)
    email_username_entry.insert(0, "dumb@gmail.com")
    password_entry.delete(0,END)
     
#-------- UI Setup --------------------#
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg=LAVENDER)

# canvas
canvas = Canvas(width=100, height=100, borderwidth=20, bg=LAVENDER, highlightthickness=0)
img = Image.open("password_manager/lock.png")
resize_image = img.resize((100,100))
lock_img = ImageTk.PhotoImage(resize_image)
canvas.create_image(80,80, image=lock_img)
canvas.grid(column=1, row=0)

# label
website_label = Label(text="Website:", bg=LAVENDER)
website_label.grid(column=0, row=1)
email_username_label = Label(text="Email/Username:", bg=LAVENDER)
email_username_label.grid(column=0, row=2)
password_label = Label(text="Password:", bg=LAVENDER)
password_label.grid(column=0,row=3)

# entries
website_entry = Entry(width=40, highlightthickness=0)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_username_entry = Entry(width=40, highlightthickness=0)
email_username_entry.insert(0, "dummy@gmail.com")
email_username_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=21, highlightthickness=0)
password_entry.grid(column=1, row=3)

# button 
generate_btn = Button(text="Generate Password",bg= LAVENDER, borderwidth=0, highlightthickness=0, command=generate_password)
generate_btn.grid(column=2,row=3)
add_btn = Button(text="Add", width=38, bg=LAVENDER, borderwidth=0, highlightthickness=0, command=save)
add_btn.grid(column=1, row=4, columnspan=2)


window.mainloop()