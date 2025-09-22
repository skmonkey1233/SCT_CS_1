import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result

def process_text(mode):
    text = entry_message.get("0.0", "end").strip()
    shift_val = entry_shift.get()
    if not shift_val.isdigit():
        messagebox.showerror("Error", "Shift value must be a number!")
        return
    shift = int(shift_val)
    result = caesar_cipher(text, shift, mode)
    entry_result.delete("0.0", "end")
    entry_result.insert("end", result)

def brute_force():
    text = entry_message.get("0.0", "end").strip()
    if not text:
        messagebox.showerror("Error", "Please enter a message to brute-force.")
        return
    entry_result.delete("0.0", "end")
    brute_results = ""
    for shift in range(1, 26):
        decrypted = caesar_cipher(text, shift, mode='decrypt')
        brute_results += f"Shift {shift:2}: {decrypted}\n"
    entry_result.insert("end", brute_results)

def copy_to_clipboard():
    result = entry_result.get("0.0", "end").strip()
    if result:
        app.clipboard_clear()
        app.clipboard_append(result)
        messagebox.showinfo("Copied", "Result copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No result to copy!")

def clear_fields():
    entry_message.delete("0.0", "end")
    entry_shift.delete(0, "end")
    entry_result.delete("0.0", "end")

def switch_theme():
    current = theme_var.get()
    ctk.set_appearance_mode(current)
    # Optionally show a message
    # messagebox.showinfo("Theme", f"Switched to {current} mode.")

# ------------------- GUI Setup -------------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("🔐 Caesar Cipher - Supercharged")
app.geometry("700x600")

# Theme switcher
theme_var = tk.StringVar(value="dark")
theme_frame = ctk.CTkFrame(app)
theme_frame.pack(pady=10)
theme_label = ctk.CTkLabel(theme_frame, text="Theme:", font=("Arial", 13))
theme_label.pack(side="left", padx=5)
theme_switch = ctk.CTkOptionMenu(theme_frame, variable=theme_var, values=["dark", "light", "system"], command=lambda _: switch_theme())
theme_switch.pack(side="left", padx=5)

# Title
title_label = ctk.CTkLabel(app, text="Supercharged Caesar Cipher", font=("Arial", 26, "bold"))
title_label.pack(pady=10)

# Message input
entry_message = ctk.CTkTextbox(app, width=600, height=100, corner_radius=8)
entry_message.pack(pady=10)
entry_message.insert("end", "Enter your message here...")

# Shift + Buttons frame
helper_frame = ctk.CTkFrame(app)
helper_frame.pack(pady=8)

ctk.CTkLabel(helper_frame, text="Shift Value:", font=("Arial", 14)).pack(side="left", padx=3)
entry_shift = ctk.CTkEntry(helper_frame, width=70)
entry_shift.pack(side="left", padx=4)

encrypt_button = ctk.CTkButton(helper_frame, text="🔒 Encrypt", width=110, command=lambda: process_text('encrypt'))
encrypt_button.pack(side="left", padx=5)

decrypt_button = ctk.CTkButton(helper_frame, text="🔓 Decrypt", fg_color="green", width=110, command=lambda: process_text('decrypt'))
decrypt_button.pack(side="left", padx=5)

brute_button = ctk.CTkButton(helper_frame, text="🤖 Brute Force Decrypt", fg_color="orange", width=160, command=brute_force)
brute_button.pack(side="left", padx=5)

clear_button = ctk.CTkButton(helper_frame, text="🧹 Clear", fg_color="gray", width=80, command=clear_fields)
clear_button.pack(side="left", padx=5)

# Result output
ctk.CTkLabel(app, text="Result:", font=("Arial", 15, "bold")).pack(pady=(15,5))
entry_result = ctk.CTkTextbox(app, width=600, height=180, corner_radius=8)
entry_result.pack(pady=8)

copy_button = ctk.CTkButton(app, text="📋 Copy to Clipboard", fg_color="blue", width=180, command=copy_to_clipboard)
copy_button.pack(pady=5)

app.mainloop()

