import hashlib
import tkinter as tk
from tkinter import ttk
import random
import string
from tkinter import messagebox
from tkinter import Toplevel
import send

root = tk.Tk()
root.title("Password generator")
root.geometry("395x400")
root.config(bg="#F7728A")
root.minsize(350, 400)
root.maxsize(350, 400)

frame = tk.Frame()
frame.config(bg="#220D02")
frame.grid(row=0, column=0)


lablePassword = tk.Label(frame, text="Enter length ",
                         bg='white', fg='black').grid(row=0, column=0, pady=5)
lengthPass = tk.IntVar()
entryPassword = tk.Entry(frame, textvariable=lengthPass)
entryPassword.grid(row=0, column=1)
entryPassword.delete(0, tk.END)
entryPassword.insert(tk.END, "12")
# entryPassword.insert(0, "12")


password_methods = [
    "Random_Character_Selection",
    "Dictionary_Words",
    "Pattern_Based",
    "Hash_Based"]


options = tk.StringVar()
combo = ttk.Combobox(frame, values=password_methods)
# combo.place(x=0, y=30)
combo.grid(row=1, column=0, padx=5, pady=5)
# combo.pack()
# combo.grid(row=1, column=1)

finalPassword = tk.Label(root, text="Password is ", bg="#F7728A", fg="white")
finalPassword.grid(row=3, padx=5, pady=5)


def show():
    global lengthPass
    global options
    lengthPass = int(entryPassword.get())

    options = combo.get()
    match (options):
        case ("Random_Character_Selection"):
            Random_Character_Selection(lengthPass)
        case ("Dictionary_Words"):
            Dictionary_Words(lengthPass)

        case ("Pattern_Based"):
            pattern = tk.StringVar()

            form2 = Toplevel()
            form2.title("Pattern method")
            form2.geometry("300x300")
            lable = tk.Label(form2, text="Enter pattern")
            lable.grid(row=0, column=0, padx=5, pady=5)
            entry = tk.Entry(form2, textvariable=pattern, width=15)
            entry.grid(row=0, column=1, padx=1, pady=5)
            # pattern = entry.get()
            # print(pattern.get())

            def call():
                Pattern_Based(pattern.get())
                form2.destroy()

            btn = tk.Button(form2, text="Submit", width=10,
                            bg="red", command=call)
            btn.grid(row=1, column=1)

        case ("Hash_Based"):
            pattern = tk.StringVar()

            form2 = Toplevel()
            form2.title("Hash methods")
            form2.geometry("300x300")
            lable = tk.Label(form2, text="Enter message")
            lable.grid(row=0, column=0, padx=5, pady=5)
            entry = tk.Entry(form2, textvariable=pattern, width=15)
            entry.grid(row=0, column=1, padx=1, pady=5)
            # pattern = entry.get()
            # print(pattern.get())

            def call():
                Hash_Based(pattern.get())
                form2.destroy()

            btn = tk.Button(form2, text="Submit", width=10,
                            bg="red", command=call)
            btn.grid(row=1, column=1)

        case (_):
            messagebox.showinfo("Something is wrong")


def Random_Character_Selection(lengthPass):
    character = string.ascii_letters + string.digits + string.punctuation
    passe = "".join(random.choice(character) for _ in range(lengthPass))
    # finalPassword.delete(0, tk.END)
    send.sendSms(passe)
    finalPassword.config(text=f"Password is {passe}")


def Dictionary_Words(lengthPass):
    password_methods = ["kamlesh", "Divya", "Chaitany",
                        "Vani", "Shubham", "Yogen", "Rahul"]
    passe = "".join(random.choice(password_methods)for _ in range(lengthPass))
    0

    send.sendSms(passe)
    finalPassword.config(text=f"Password is {passe}")


def Pattern_Based(pattern):
    password = ""
    global lengthPass
    # while lengthPass > 0:
    for char in pattern:
        if char == 'L' or char == 'l':
            password += random.choice(string.ascii_uppercase)
        elif char == 'K' or char == 'k':
            password += random.choice(string.ascii_lowercase)
        elif char == 'a' or char == 'A':
            password += random.choice(string.digits)
        elif char == 'o' or char == 'O':
            password += random.choice(string.punctuation)
        elif char == 'D' or char == 'd':
            password += random.choice(string.punctuation)
        else:
            password += char
        # lengthPass -= 1
    # print(password)
    password = password[:lengthPass]
    send.sendSms(password)
    finalPassword.config(text=f"Password is {password}")

# def pattern_password(pattern):
#     password = ""
#     for char in pattern:
#         if char == 'L':
#             password += random.choice(string.ascii_uppercase)  # Uppercase letter
#         elif char == 'l':
#             password += random.choice(string.ascii_lowercase)  # Lowercase letter
#         elif char == 'd':
#             password += random.choice(string.digits)  # Digit
#         elif char == 's':
#             password += random.choice(string.punctuation)  # Special character
#     return password

# # Example usage
# print("Pattern Password (LlDdSs):", pattern_password("LlDdSsLl"))


def Hash_Based(input_string):
    hashed = hashlib.sha256(input_string.encode()).hexdigest()
    password = hashed[:lengthPass]
    send.sendSms(password)
    finalPassword.config(text=f"Password is {password}")
#     import hashlib

# def hash_based_password(input_string):
#     # Create a SHA-256 hash of the input string and return the first 12 characters
#     hashed = hashlib.sha256(input_string.encode()).hexdigest()
#     return hashed[:12]


# Example usage
# print("Hash-Based Password:", Hash_Based("your_input_string"))


buttonPassword = tk.Button(frame, text="Select Option", command=show)
buttonPassword.grid(row=2, column=0, padx=2, pady=2)

root.mainloop()
