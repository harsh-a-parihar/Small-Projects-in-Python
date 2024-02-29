from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

#--------------- Search Password --------------#
def search_password():
    website = web_entry.get()
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='No Data file Found.')
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f'Details:\nEmail: {email}\nPassword: {password}')
        else:
            messagebox.showinfo(title='Error', message=f'No details for {website} exists.')

#------------ Generate Password ---------#
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_letters + password_symbols
    shuffle(password_list)

    password = ''.join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

#---------- Save Password ----------#
def save():
    website = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            'email': email,
            'password': password,
        }
    }

    if (len(website) == 0) or (len(email) == 0) or (len(password) == 0):
        messagebox.showinfo(title='Oops', message='Fill the empty field.')
    else:
        try:
            with open('data.json', 'r') as data_file:
                # Reading the data
                data = json.load(data_file)
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        except json.decoder.JSONDecodeError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            web_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)

#---------- UI Setup -----------#

app = Tk()
app.title('Password-Manager')
app.config(padx=100, pady=100)

# canvas
canvas = Canvas(width=200, height=200, bg="#f0f0f0", highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1, pady=20)

# labels
web_label = Label(text='Website:', bg="#f0f0f0", fg="#333", font=("Arial", 12, "bold"))
web_label.grid(row=1, column=0, pady=10)
email_label = Label(text='Email/Username:', bg="#f0f0f0", fg="#333", font=("Arial", 12, "bold"))
email_label.grid(row=2, column=0, pady=10)
password_label = Label(text='Password:', bg="#f0f0f0", fg="#333", font=("Arial", 12, "bold"))
password_label.grid(row=3, column=0, pady=10)

# entries
web_entry = Entry(width=20, bg="white", fg="#333", font=("Arial", 12))
web_entry.grid(row=1, column=1, pady=10, sticky="w")
web_entry.focus()
email_entry = Entry(width=35, bg="white", fg="#333", font=("Arial", 12))
email_entry.grid(row=2, column=1, columnspan=2, pady=10, sticky="w")
password_entry = Entry(width=20, bg="white", fg="#333", font=("Arial", 12), show="*")
password_entry.grid(row=3, column=1, pady=10, sticky="w")

# buttons
search_detail = Button(text='Search', width=13, bg="#007bff", fg="white", font=("Arial", 12, "bold"), command=search_password)
search_detail.grid(row=1, column=2, pady=10, padx=5)
pgenerator = Button(text='Generate', width=13, bg="#28a745", fg="white", font=("Arial", 12, "bold"), command=generate_password)
pgenerator.grid(row=3, column=2, pady=10, padx=5)
add_button = Button(text='Add', width=30, bg="#17a2b8", fg="white", font=("Arial", 12, "bold"), command=save)
add_button.grid(row=4, column=1, columnspan=2, pady=10)

app.mainloop()
