import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import os
import threading
import time

KEY = 123  # XOR key

# === File encoding/decoding ===

def encode_to_imoge(image_path, output_path, progress_callback):
    with open(image_path, "rb") as f:
        img_data = bytearray(f.read())

    for i in range(len(img_data)):
        img_data[i] ^= KEY
        if i % 10000 == 0:
            progress_callback(i / len(img_data) * 100)

    with open(output_path, "wb") as f:
        f.write(b"IMOGEv1\n")
        f.write(img_data)
        f.write(b"\nEOF_IMOGE")

    progress_callback(100)

def decode_imoge(file_path, output_path, progress_callback):
    with open(file_path, "rb") as f:
        content = f.read()

    if not (content.startswith(b"IMOGEv1\n") and content.endswith(b"\nEOF_IMOGE")):
        raise ValueError("Invalid .imoge file.")

    data = bytearray(content[len(b"IMOGEv1\n"):-len(b"\nEOF_IMOGE")])

    for i in range(len(data)):
        data[i] ^= KEY
        if i % 10000 == 0:
            progress_callback(i / len(data) * 100)

    with open(output_path, "wb") as f:
        f.write(data)

    progress_callback(100)

# === GUI functions ===

def update_progress_bar(value):
    progress["value"] = value
    root.update_idletasks()

def threaded(func, *args):
    def run():
        try:
            func(*args)
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            update_progress_bar(0)
    threading.Thread(target=run).start()

def convert_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
    if file_path:
        out_path = filedialog.asksaveasfilename(defaultextension=".imoge", filetypes=[("Imoge Files", "*.imoge")])
        if out_path:
            threaded(encode_to_imoge, file_path, out_path, update_progress_bar)
            messagebox.showinfo("Done", f"Converted to .imoge:\n{out_path}")

def view_imoge():
    file_path = filedialog.askopenfilename(filetypes=[("Imoge Files", "*.imoge")])
    if file_path:
        temp_output = "temp_imoge_output.png"
        def task():
            decode_imoge(file_path, temp_output, update_progress_bar)
            show_image(temp_output)
            os.remove(temp_output)
        threaded(task)

def convert_imoge_to_image():
    file_path = filedialog.askopenfilename(filetypes=[("Imoge Files", "*.imoge")])
    if file_path:
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[
            ("PNG Image", "*.png"),
            ("JPG Image", "*.jpg"),
            ("JPEG Image", "*.jpeg")
        ])
        if save_path:
            threaded(decode_imoge, file_path, save_path, update_progress_bar)
            messagebox.showinfo("Done", f".imoge saved as:\n{save_path}")

def show_image(path):
    win = tk.Toplevel()
    win.title("Imoge Viewer")
    img = Image.open(path)
    img = img.resize((400, 400))
    tk_img = ImageTk.PhotoImage(img)
    lbl = tk.Label(win, image=tk_img)
    lbl.image = tk_img
    lbl.pack()

# === GUI ===

root = tk.Tk()
root.title("🖼️ Imoge Converter & Viewer")
root.geometry("400x300")
root.resizable(False, False)
root.configure(bg="#f5f5f5")

# Title
title = tk.Label(root, text="🖼️ Imoge Converter & Viewer", font=("Segoe UI", 16, "bold"), bg="#f5f5f5", fg="#333")
title.pack(pady=15)

# Buttons
button_style = {"width": 35, "height": 2, "font": ("Segoe UI", 10, "bold")}

tk.Button(root, text="🖼️ Convert PNG/JPG to .imoge", command=convert_image, bg="#4CAF50", fg="white", **button_style).pack(pady=5)
tk.Button(root, text="👁️ View .imoge File", command=view_imoge, bg="#2196F3", fg="white", **button_style).pack(pady=5)
tk.Button(root, text="🔄 Convert .imoge to PNG/JPG", command=convert_imoge_to_image, bg="#FF9800", fg="white", **button_style).pack(pady=5)

# Progress Bar
progress = ttk.Progressbar(root, length=300, mode='determinate')
progress.pack(pady=20)

root.mainloop()
