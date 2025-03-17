from tkinter import *
import  math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer(): 
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_b_sec = SHORT_BREAK_MIN * 60
    long_b_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_b_sec)
    elif reps % 2 == 0:
        count_down(short_b_sec)
    else:  
        count_down(work_sec)
    
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60 

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}") 
    if count > 0:
        window.after(10, count_down, count-1)
    else: 
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# -- canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomtao_img = PhotoImage(file="pomodoro/tomato.png")
canvas.create_image(100, 112, image=tomtao_img)
timer_text = canvas.create_text(100,130, text="25:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# -- label
title_label = Label(text="Timer",bg=YELLOW, fg=GREEN, font=(FONT_NAME, 48))
title_label.grid(column=1,row=0)

check_marks = Label(text="✔", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1,row=3)

#button
start_btn = Button(text="Start", highlightthickness=0, command=start_timer)
start_btn.grid(column=0, row=2)
reset_btn = Button(text="Reset", highlightthickness=0)
reset_btn.grid(column=2, row=2)


window.mainloop()
