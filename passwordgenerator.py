import tkinter as tk
import random
import string

class PasswordGenerator:
    def __init__(self, master):
        self.master = master
        master.title("Simple Password Generator")

        # Label for password length
        self.label = tk.Label(master, text="Password Length:")
        self.label.pack()

        # Entry for password length
        self.length_entry = tk.Entry(master)
        self.length_entry.pack()

        # Checkbox options
        self.include_uppercase = tk.BooleanVar()
        self.include_lowercase = tk.BooleanVar()
        self.include_numbers = tk.BooleanVar()
        self.include_special = tk.BooleanVar()

        self.uppercase_checkbox = tk.Checkbutton(master, text="Include Uppercase Letters", variable=self.include_uppercase)
        self.uppercase_checkbox.pack()

        self.lowercase_checkbox = tk.Checkbutton(master, text="Include Lowercase Letters", variable=self.include_lowercase)
        self.lowercase_checkbox.pack()

        self.numbers_checkbox = tk.Checkbutton(master, text="Include Numbers", variable=self.include_numbers)
        self.numbers_checkbox.pack()

        self.special_checkbox = tk.Checkbutton(master, text="Include Special Characters", variable=self.include_special)
        self.special_checkbox.pack()

        # Generate button
        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

        # Label to display generated password
        self.password_label = tk.Label(master, text="", font=("Helvetica", 16))
        self.password_label.pack()

    def generate_password(self):
        length = self.length_entry.get()
        try:
            length = int(length)
            if length <= 0:
                raise ValueError("Length must be positive.")
        except ValueError:
            self.password_label.config(text="Please enter a valid length.")
            return

        characters = ""
        if self.include_uppercase.get():
            characters += string.ascii_uppercase
        if self.include_lowercase.get():
            characters += string.ascii_lowercase
        if self.include_numbers.get():
            characters += string.digits
        if self.include_special.get():
            characters += string.punctuation

        if not characters:
            self.password_label.config(text="Please select at least one character set.")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_label.config(text=password)

if __name__ == "__main__":
    root = tk.Tk()
    password_generator = PasswordGenerator(root)
    root.mainloop()