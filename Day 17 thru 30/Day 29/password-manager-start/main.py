from tkinter import * #imports all tkinter classes only
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def action():
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
               'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # randomly decide how many of each type
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    ltrs = [random.choice(letters) for _ in range(nr_letters)]
    sym = [random.choice(symbols) for _ in range(nr_symbols)]
    numb = [random.choice(numbers) for _ in range(nr_numbers)]

    password_chars = ltrs + sym + numb
    random.shuffle(password_chars)
    usr_password = "".join(password_chars)

    # put password into entry field
    wg_passwd.delete(0, END)
    wg_passwd.insert(0, usr_password)

    # copy to clipboard
    window.clipboard_clear()
    window.clipboard_append(usr_password)
    window.update()  # keeps clipboard after app closes

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = wg_website.get().strip()
    username = wg_ursname.get().strip()
    password = wg_passwd.get().strip()

    if not website or not username or not password:
        messagebox.showinfo('Empty Field', 'website, username or password is empty')
        return
    is_ok = messagebox.askquestion(title= website, message='Are you sure you want to save this?')
    print('ideally i would do something cool here but its take a hike: ', is_ok)

    line = f"{website} | {username} | {password}\n"
    with open("data.txt", "a", encoding="utf-8") as f:
        f.write(line)

    wg_website.delete(0, END)
    wg_passwd.delete(0, END)
    wg_website.focus()
    messagebox.showinfo('Successful!', 'Save Successful')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

# Tkinter Canvas Widget:
canvas = Canvas(width=200, height=200, highlightthickness=0)
img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

# Labels & Inputs
lb_website = Label(text='Website:', font=('ariel', 10, 'bold'))
lb_website.grid(row=1, column=0)
wg_website = Entry(width=35)
wg_website.focus()
wg_website.grid(row=1, column=1, columnspan=2)

lb_ursname = Label(text='Email/Username:', font=('ariel', 10, 'bold'))
lb_ursname.grid(row=2, column=0)
wg_ursname = Entry(width=35)
wg_ursname.insert(0,'email@gmail.com')
wg_ursname.grid(row=2, column=1, columnspan=2)

lb_passwd = Label(text='Password:', font=('ariel', 10, 'bold'))
lb_passwd.grid(row=3, column=0)
wg_passwd = Entry(width=21)
wg_passwd.grid(row=3, column=1)

button_gn_password = Button(text="Generate Password", command=action)
button_gn_password.grid(row=3, column=2)

# Add button (with top padding so it doesn’t stick to the row above)
btn_add = Button(text='Add', width=36, command=save)
btn_add.grid(row=4, column=1, columnspan=2, pady=10)



window.mainloop()
