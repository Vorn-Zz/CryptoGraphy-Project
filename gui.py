# gui.py
import tkinter as tk
from tkinter import filedialog, messagebox

from encrypt import encrypt_file
from decrypt import decrypt_file
from utils import ensure_dirs, encrypted_path, decrypted_path


def start_gui():
    ensure_dirs()

    root = tk.Tk()
    root.title("Secure File Locker")
    root.geometry("400x250")

    file_path = tk.StringVar()

    tk.Label(root, text="Secure File Locker", font=("Arial", 16)).pack(pady=10)

    frame = tk.Frame(root)
    frame.pack(pady=5)

    tk.Entry(frame, textvariable=file_path, width=30).pack(side=tk.LEFT, padx=5)

    def browse():
        path = filedialog.askopenfilename()
        if path:
            file_path.set(path)

    tk.Button(frame, text="Browse", command=browse).pack(side=tk.LEFT)

    tk.Label(root, text="Password").pack(pady=(10, 0))
    password_entry = tk.Entry(root, show="*", width=25)
    password_entry.pack()

    def encrypt_action():
        if not file_path.get() or not password_entry.get():
            messagebox.showerror("Error", "Select file and enter password")
            return

        out = encrypted_path(file_path.get())
        encrypt_file(file_path.get(), out, password_entry.get())
        messagebox.showinfo("Success", f"Encrypted to:\n{out}")

    def decrypt_action():
        if not file_path.get() or not password_entry.get():
            messagebox.showerror("Error", "Select file and enter password")
            return

        out = decrypted_path(file_path.get())
        ok = decrypt_file(file_path.get(), out, password_entry.get())

        if not ok:
            messagebox.showerror("Error", "Wrong password or file")
            return

        messagebox.showinfo("Success", f"Decrypted to:\n{out}")

    btn = tk.Frame(root)
    btn.pack(pady=20)

    tk.Button(btn, text="Encrypt", width=12, command=encrypt_action)\
        .pack(side=tk.LEFT, padx=10)

    tk.Button(btn, text="Decrypt", width=12, command=decrypt_action)\
        .pack(side=tk.LEFT)

    root.mainloop()
