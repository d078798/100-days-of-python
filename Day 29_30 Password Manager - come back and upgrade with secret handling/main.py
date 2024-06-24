from tkinter import *
from tkinter import messagebox
import json
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    psswd.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    letters_chosen = [random.choice(letters) for x in range(nr_letters)]
    numbers_chosen = [random.choice(numbers) for x in range(nr_numbers)]
    symbols_chosen = [random.choice(symbols) for x in range(nr_symbols)]
    password_list = letters_chosen + numbers_chosen + symbols_chosen
    
    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)

    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)

    random.shuffle(password_list)
    print(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    print(f"Your password is: {password}")
    psswd.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    passname = name.get()
    website = web.get()
    username = user.get()
    password = psswd.get()
    
    if website == "":
        warning = messagebox.showerror(title="Website blank",message="Website box blank")
    elif username == "":
        warning = messagebox.showerror(title="Username blank",message="Username box blank")
    elif password == "":
        warning = messagebox.showerror(title="Password blank",message="Password box blank")
    elif passname == "":
        warning = messagebox.showerror(title="Password Name blank",message="Password Name box blank")
    else:    
    
        detail_check = messagebox.askyesno(title="You Sure?",message="Are you sure the details are correct?")
        if detail_check:
            try:
                with open(r"Day 29_30 Password Manager\data.json", "r") as f:
                    password_dict = json.load(f)
            except FileNotFoundError:
                with open(r"Day 29_30 Password Manager\data.json", "w") as f:
                    json.dump({},f,indent=4)
            finally:
                with open(r"Day 29_30 Password Manager\data.json", "r") as f:
                    password_dict = json.load(f)
            
            inner_dict = {
                "website": website,
                "username": username,
                "password": password
            }
            if passname not in password_dict.keys():
                password_dict[passname] =inner_dict
                name.delete(0,END)
                psswd.delete(0,END)
                web.delete(0,END)
                web.focus()
            elif passname in password_dict.keys() and password != "" and password != password_dict[passname]["password"]:
                password_dict[passname]["password"] = password
                messagebox.askokcancel(title=f"Password changed for {passname}",message=f"Password changed for {passname}")
            else:
                print("Website already has username and password")
                messagebox.showerror(title="Password Name Already Exists",message="Password Name Already Exists")
            
            with open(r"Day 29_30 Password Manager\data.json", "w") as f:
                json.dump(password_dict,f, indent=4)
# ---------------------------- Find PASSWORD ------------------------------- #
def find_password():
    print("find")
    passname = name.get()
    if passname == "":
        warning = messagebox.showerror(title="Password Name blank",message="Password Name box blank")
    else:
    
        try:
            with open(r"Day 29_30 Password Manager\data.json", "r") as f:
                    password_dict = json.load(f)
        except FileNotFoundError:
            with open(r"Day 29_30 Password Manager\data.json", "w") as f:
                json.dump({},f,indent=4)
        finally:
            with open(r"Day 29_30 Password Manager\data.json", "r") as f:
                password_dict = json.load(f)
    
    try:
        psswd.delete(0,END)
        web.delete(0,END)
        user.delete(0,END)
        psswd.insert(0,password_dict[passname]["password"])
        web.insert(0, password_dict[passname]["website"])
        user.insert(0,password_dict[passname]["username"] )
        messagebox.askokcancel(title=passname,message=f'Website: {password_dict[passname]["website"]}\nUsername: {password_dict[passname]["username"]} \nPassword: {password_dict[passname]["password"]}')
    except KeyError:
        warning = messagebox.showerror(title="Password Name not found",message="Name not found in database")
    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.configure(padx=50,pady =50)

canvas = Canvas(width = 200, height=200, highlightthickness=0)
logo = PhotoImage(file=r"Day 29_30 Password Manager\logo.png")
canvas.create_image(100,100, image=logo)

web_label = Label(text="Website:")
web = Entry(width=53)
web.focus()

name_label = Label(text="Name:")
name = Entry(width=34)
name.focus()

user_label = Label(text="Email/Username:")
user = Entry(width=53)
user.insert(0, "email@d078798.com")
psswd_label = Label(text="Password:")
psswd = Entry(width=34)
psswd_gen = Button(text="Generate Password",command=generate_password)

add_entry = Button(text="Add",width=45,command=save_password)
search = Button(text="Search",width=15, command=find_password)


canvas.grid(column=1,row=0)

name_label.grid(column=0,row=1)
name.grid(column=1,row=1)
search.grid(column=2,row=1)

web_label.grid(column=0,row=2)
web.grid(column=1,row=2,columnspan=2)

user_label.grid(column=0,row=3)
user.grid(column=1,row=3,columnspan=2)

psswd_label.grid(column=0,row=4)
psswd.grid(column=1,row=4)
psswd_gen.grid(column=2,row=4)

add_entry.grid(column=1,row=5,columnspan=2)
window.mainloop()