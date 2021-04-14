
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 0
my_timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(my_timer)
    timer_label.config(text="Timer")
    check_mark_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    global timer_label
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer_label.config(text="Long Break", fg=RED)
        #timer_label.update()
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text="Short Break", fg=PINK)
        #timer_label.update()
        count_down(short_break_sec)

    else:
        timer_label.config(text="Work", fg=GREEN)
        #timer_label.update()
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count / 60) #math.floor gives result of division without decimals. Not it does not round but ignores the decimal
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    if count_sec in range(0, 10):   # This is my take on it. Commented out below is Angela's simple approach
       count_sec = "0" + str(count_sec)
    # if count_sec < 10:
        # count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global my_timer
        my_timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        check_mark_label.config(text=mark)




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("My Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)#highlightthickness gets rid of the borders around the image within the canvas
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.pack()


timer_label = Label(text="Timer")
timer_label.config(font=("Courier", 25, "bold"), fg=GREEN, bg=YELLOW)
timer_label.place(relx=0.5, rely=-0.1, anchor=CENTER)


check_mark_label = Label(text="")
check_mark_label.config(font=("Courier", 25, "bold"), fg=GREEN, bg=YELLOW)
check_mark_label.place(relx=0.5, rely=1.1, anchor=CENTER)


start_button = Button(text="Start", command=start_timer)
start_button.config(font=("courier", 15))
start_button.place(relx=-0.2, rely=1.1, anchor="sw")


reset_button = Button(text="Reset", command=reset_timer)
reset_button.config(font=("courier", 15))
reset_button.place(relx=0.9, rely=1.1, anchor="sw")



window.mainloop()