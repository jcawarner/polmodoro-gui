from tkinter import *
import math
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
checkmark = ""
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
	window.after_cancel(timer)
	canvas.itemconfig(timer_text, text="00:00")
	timer_label.config(text="Timer")
	check_label.config(text="")
	global reps
	global checkmark
	checkmark = ""
	reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
	global reps
	global WORK_MIN
	global SHORT_BREAK_MIN
	global LONG_BREAK_MIN
	global checkmark
	reps += 1
	if reps % 8 == 0:
		count_down(LONG_BREAK_MIN * 60)
		timer_label.config(text="Long Break", fg=RED)
		checkmark += "✔"
		check_label.config(text=checkmark)
	elif reps % 2 == 0:
		count_down(SHORT_BREAK_MIN * 60)
		timer_label.config(text="Short Break", fg=PINK)
	else:
		count_down(WORK_MIN * 60)
		timer_label.config(text="Working")
		checkmark += "✔"
		check_label.config(text=checkmark)
	# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
	global timer
	count_min = math.floor(count / 60)
	count_sec = count % 60
	if count_sec < 10:
		count_sec = f"0{count_sec}"
	if count_sec == 0:
		count_sec = "00"
	if count_min == 0:
		count_min = "00"


	canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
	if count > 0:
		timer = window.after(1000, count_down, count - 1)
	else:
		start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

window.after(1000, )

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer_label = Label(window, text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(row=0, column=1)

start_button = Button(window, text="Start", bg=GREEN, fg="white", font=(FONT_NAME, 12, "bold"), command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(window, text="Reset", fg=RED, bg="white", font=(FONT_NAME, 12, "bold"), command=reset_timer)
reset_button.grid(row=2, column=2)

check_label = Label(window, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold"))
check_label.grid(row=3, column=1)

window.mainloop()








