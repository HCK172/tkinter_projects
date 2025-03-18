from tkinter import * 
from PIL import Image, ImageTk

LAVENDER ="#E5D9F2"


#------ password saved into a file -----#
def save():
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()

    if website and email_username and password:
        new = f"{website} | {email_username} | {password}\n"
        try: 
            with open("password_manager/password.txt", "r") as file:
                data = file.readlines()
                data.append(new)
            with open("password_manager/password.txt", "w") as file:
                file.writelines(data)
            success_label.config(text="Successfully added!😀")
        except Exception as e:
            success_label.config(text=f"Error: {e}")
    else: 
        success_label.config(text="Please fill in all fields!")
    clear_entry()
    

def clear_entry():
    website_entry.delete(0, END)
    email_username_entry.delete(0,END)
    email_username_entry.insert(0, "dumb@gmail.com")
    password_entry.delete(0,END)
    window.after(500, lambda: success_label.config(text=""))


         
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
success_label = Label(text="", bg=LAVENDER)
success_label.grid(column=1,row=5, columnspan=2)

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
generate_btn = Button(text="Generate Password",bg= LAVENDER, borderwidth=0, highlightthickness=0)
generate_btn.grid(column=2,row=3)
add_btn = Button(text="Add", width=38, bg=LAVENDER, borderwidth=0, highlightthickness=0, command=save)
add_btn.grid(column=1, row=4, columnspan=2)


window.mainloop()