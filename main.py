import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import ImageTk, Image


def generate_qr():
    data = entry.get()
    if not data:
        messagebox.showwarning("Uyarı", "Lütfen QR kod için bir metin girin.")
        return

    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save("qr_code.png")

    display_qr("qr_code.png")


def display_qr(img_path):
    img = Image.open(img_path)
    img = img.resize((250, 250))  
    img_tk = ImageTk.PhotoImage(img)

    for widget in frame.winfo_children():
        widget.destroy()

    label = tk.Label(frame, image=img_tk)
    label.image = img_tk  
    label.pack()



root = tk.Tk()
root.title("QR Kod Oluşturucu")
root.geometry("300x350")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

generate_button = tk.Button(root, text="QR Kod Oluştur", command=generate_qr)
generate_button.pack(pady=5)

frame = tk.Frame(root)
frame.pack(pady=10)

root.mainloop()
