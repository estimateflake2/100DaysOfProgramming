from tkinter import Tk, Canvas, Button, PhotoImage
import pandas as pd
import random
import os

# ---------- Config ----------
BG_COLOR = "#B1DDC6"
WINDOW_TITLE = "Flashy"
FLIP_DELAY_MS = 9000

DATA_DIR = "data"
SOURCE_CSV = os.path.join(DATA_DIR, "core 2.csv")       # original full list
LEARN_CSV  = os.path.join(DATA_DIR, "words_to_learn.csv")  # progress file

# ---------- Data load ----------
def load_cards():
    try:
        if os.path.exists(LEARN_CSV):
            df = pd.read_csv(LEARN_CSV)
        else:
            df = pd.read_csv(SOURCE_CSV)
    except FileNotFoundError:
        raise SystemExit("Could not find the CSV. Check your data folder.")

    if "Question" not in df.columns or "Answer" not in df.columns:
        raise SystemExit("CSV must include 'Question' and 'Answer' columns.")
    return df.to_dict(orient="records")

cards = load_cards()
current_card = {}
flip_after_id = None

# ---------- UI ----------
window = Tk()
window.title(WINDOW_TITLE)
window.config(padx=50, pady=50, bg=BG_COLOR)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img  = PhotoImage(file="images/card_back.png")
wrong_img = PhotoImage(file="images/wrong.png")
right_img = PhotoImage(file="images/right.png")

canvas = Canvas(width=800, height=526, bg=BG_COLOR, highlightthickness=0)
card_image = canvas.create_image(400, 263, image=card_front_img)
title_text = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"), fill="black")
# set width so long questions wrap nicely
word_text  = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"), fill="black", width=700)
canvas.grid(row=0, column=0, columnspan=2)

# ---------- Helpers ----------
def adjust_font(text):
    base_size = 60
    min_size  = 15
    length = len(text)
    size = int(base_size - 0.9 * length)
    size = max(min_size, min(base_size, size))
    return "Arial", size, "bold"

def cancel_flip():
    global flip_after_id
    if flip_after_id is not None:
        window.after_cancel(flip_after_id)
        flip_after_id = None

def schedule_flip():
    global flip_after_id
    flip_after_id = window.after(FLIP_DELAY_MS, flip_card)

def save_progress():
    """Write remaining cards to words_to_learn.csv."""
    if len(cards) == 0:
        # If user learned everything, remove the file so next run uses the full set again.
        if os.path.exists(LEARN_CSV):
            os.remove(LEARN_CSV)
        return
    df = pd.DataFrame(cards)
    df.to_csv(LEARN_CSV, index=False)

# ---------- Core actions ----------
def next_card():
    cancel_flip()
    if not cards:
        canvas.itemconfig(card_image, image=card_front_img)
        canvas.itemconfig(title_text, text="Done", fill="black")
        canvas.itemconfig(word_text, text="All cards learned!", font=("Arial", 40, "bold"), fill="black")
        return

    global current_card
    current_card = random.choice(cards)

    canvas.itemconfig(card_image, image=card_front_img)
    canvas.itemconfig(title_text, text="Core 2", fill="black")

    q_text = current_card["Question"]
    canvas.itemconfig(word_text, text=q_text, font=adjust_font(q_text), fill="black")

    schedule_flip()

def flip_card():
    a_text = current_card.get("Answer", "")
    canvas.itemconfig(card_image, image=card_back_img)
    canvas.itemconfig(title_text, text="Answer", fill="white")
    canvas.itemconfig(word_text, text=a_text, font=adjust_font(a_text), fill="white")

# ---------- Button handlers ----------
def on_wrong():
    # keep the card in the deck
    next_card()

def on_right():
    # remove card from the deck and persist progress
    try:
        cards.remove(current_card)
    except ValueError:
        pass
    save_progress()
    next_card()

# ---------- Buttons ----------
unknown_button = Button(image=wrong_img, highlightthickness=0, borderwidth=0,
                        bg=BG_COLOR, activebackground=BG_COLOR, command=on_wrong)
unknown_button.grid(row=1, column=0)

known_button = Button(image=right_img, highlightthickness=0, borderwidth=0,
                      bg=BG_COLOR, activebackground=BG_COLOR, command=on_right)
known_button.grid(row=1, column=1)

# ---------- Start ----------
next_card()
window.mainloop()
