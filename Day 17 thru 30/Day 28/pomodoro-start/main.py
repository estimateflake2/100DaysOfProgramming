
from tkinter import *
import winsound
from functools import partial
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 5
SHORT_BREAK_MIN =20
LONG_BREAK_MIN = 5
timerId =''
chk_mrk =''
reps = 0


def play_sound (break_type):
    if break_type == 'longbreak':
        winsound.PlaySound('longbreak.wav', winsound.SND_FILENAME)
    elif break_type == 'shortbreak':
        winsound.PlaySound('shortbreak.wav', winsound.SND_FILENAME)
    elif break_type == 'work':
        winsound.PlaySound('work.wav', winsound.SND_FILENAME)

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps
    global  chk_mrk
    reps = 0
    button_str.config(state='active')
    print (timerId)
    window.after_cancel(timerId)
    min = 0
    sec = 0
    chk_mrk = ''
    canvas.itemconfig(timer_text, text=f'{min:02d}:{sec:02d}')
    label_chkmk.config(text=chk_mrk)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    button_str.config(state='disabled')
    global reps
    global  chk_mrk
    reps +=1

    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps % 8 ==0:
        play_sound('longbreak')
        label.config(text= 'Long Break',  fg=RED)
        countdown(long_break_sec)
    elif reps %2 ==0:
        chk_mrk += '🗸'
        play_sound('shortbreak')
        label.config(text='Short Break', fg=PINK)
        countdown(short_break_sec)
    else:
        play_sound('work')
        label.config(text='Work',  fg=GREEN)
        countdown(work_sec)

    label_chkmk.config(text=chk_mrk)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global  timerId
    global  chk_mrk
    min = int(count/60)
    sec = int(count%60)
    canvas.itemconfig(timer_text, text=f'{min:02d}:{sec:02d}')
    if count>0:
        timerId = window.after(1000, countdown, count-1)
    else:
        start_timer()



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Tomato - Pomodoro')
window.config(padx=100, pady=50, bg = YELLOW)



label = Label(bg=YELLOW, fg=GREEN, text= 'Timer', font = (FONT_NAME, 35, 'bold'))
label.grid(column=1,row=1,padx=10,pady=20)

#Tkinter Canvas Widget:
canvas = Canvas(width=210, height=230, bg = YELLOW, highlightthickness=0)
img = PhotoImage(file = 'tomato.png')
canvas.create_image(103,112, image=img)
timer_text = canvas.create_text(103,130, text ='00:00', fill= 'white', font = (FONT_NAME, 35, 'bold'))
canvas.grid(column=1,row=2,padx=10,pady=20)


label_chkmk = Label(bg=YELLOW, fg=RED, font = (FONT_NAME, 20, 'bold'))
label_chkmk.grid(column=1,row=4,padx=10,pady=20)

button_str = Button(text='Start', command=start_timer)
button_str.grid(column=0,row=3,padx=10,pady=20)



button_rst = Button(text='Reset', command=reset)
button_rst.grid(column=2,row=3,padx=10,pady=20)





window.mainloop()


























