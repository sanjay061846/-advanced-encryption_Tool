import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
import base64
import hashlib
import os

# 🔐 Generate AES-256 key from password
def generate_key(password):
    key = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(key)

# 🔒 Encrypt File
def encrypt_file():
    file_path = filedialog.askopenfilename()
    password = password_entry.get()

    if not file_path or not password:
        messagebox.showerror("Error", "Select file and enter password")
        return

    key = generate_key(password)
    fernet = Fernet(key)

    with open(file_path, "rb") as file:
        data = file.read()

    encrypted = fernet.encrypt(data)

    with open(file_path + ".enc", "wb") as file:
        file.write(encrypted)

    messagebox.showinfo("Success", "File Encrypted Successfully")

# 🔓 Decrypt File
def decrypt_file():
    file_path = filedialog.askopenfilename()
    password = password_entry.get()

    if not file_path or not password:
        messagebox.showerror("Error", "Select file and enter password")
        return

    key = generate_key(password)
    fernet = Fernet(key)

    try:
        with open(file_path, "rb") as file:
            encrypted_data = file.read()

        decrypted = fernet.decrypt(encrypted_data)

        original_file = file_path.replace(".enc", "")

        with open(original_file, "wb") as file:
            file.write(decrypted)

        messagebox.showinfo("Success", "File Decrypted Successfully")

    except:
        messagebox.showerror("Error", "Wrong password or invalid file")

# 🖥️ GUI Setup
root = tk.Tk()
root.title("Advanced Encryption Tool - AES-256")
root.geometry("400x250")
root.resizable(False, False)

tk.Label(root, text="Advanced Encryption Tool", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Enter Password").pack()
password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack(pady=5)

tk.Button(root, text="Encrypt File", width=20, command=encrypt_file).pack(pady=10)
tk.Button(root, text="Decrypt File", width=20, command=decrypt_file).pack(pady=5)

tk.Label(root, text="AES-256 Encryption | CODTECH Internship", font=("Arial", 8)).pack(pady=10)

root.mainloop()
