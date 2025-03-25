from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

current_card = {}
to_learn = {}
#----- read file ----#

try: 
    data = pd.read_csv("flashcard/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("flashcard/data/vocab_ko.csv")
    original_data.dropna(axis="columns", inplace=True)
    to_learn = original_data.to_dict('records')
else:
    to_learn = data.to_dict('records')

#----- flash card ----#

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title,text="korean",fill="black")
    canvas.itemconfig(card_word, text=current_card["Korean"], fill="black")
    canvas.itemconfig(canva_img, image=front_img)
    flip_timer = window.after(3000, func=flip_card)

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pd.DataFrame(to_learn)
    data.to_csv("flashcard/data/words_to_learn.csv", index=False)
    next_card()


# def next_card ():
#    num = random.randint(0, len(to_learn))
#    vocab = to_learn[num]['Korean']
#    vocab_eng = to_learn[num]['English']
#    return vocab

def flip_card():
    canvas.itemconfig(card_title,text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canva_img, image=back_img)


#------ UI ------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

front_img = PhotoImage(file="flashcard/images/card_front.png")
back_img = PhotoImage(file="flashcard/images/card_back.png")

canva_img= canvas.create_image(400,263, image=front_img)

card_title = canvas.create_text(400,150, text="",font=("Arial", 40, "italic"))
card_word = canvas.create_text(400,253, text="",font=("Arial",60,"bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_img = PhotoImage(file="flashcard/images/wrong.png")
wrong_btn= Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_btn.grid(column=0, row=1)

right_img = PhotoImage(file="flashcard/images/right.png")
right_btn = Button(image=right_img, highlightthickness=0, command=is_known)
right_btn.grid(column=1, row=1)

next_card()

window.mainloop()