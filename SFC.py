import cv2
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from ttkthemes import ThemedStyle

def encrypt_image():
    img_path = filedialog.askopenfilename(title="new.jpg")
    img = cv2.imread(img_path)

    msg = entry_msg.get()
    password = entry_password.get()

    d = {chr(i): i for i in range(255)}
    c = {i: chr(i) for i in range(255)}

    m, n, z = 0, 0, 0

    for i in range(len(msg)):
        img[n, m, z] = d[msg[i]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3

    cv2.imwrite("Encryptedmsg.jpg", img)
    os.system("start Encryptedmsg.jpg")

def decrypt_image():
    img_path = filedialog.askopenfilename(title="Select Encrypted Image File")
    img = cv2.imread(img_path)

    message = ""
    n, m, z = 0, 0, 0

    pas = entry_passcode.get()

    if password == pas:
        for i in range(len(msg)):
            message = message + c[img[n, m, z]]
            n = n + 1
            m = m + 1
            z = (z + 1) % 3
        result_label.config(text="Decryption message: " + message)
    else:
        result_label.config(text="Not a valid key")

root = tk.Tk()
root.title("Image Encryption/Decryption")
root.geometry("500x400")

style = ThemedStyle(root)
style.set_theme("plastik")

label_title = ttk.Label(root, text="Image Encryption/Decryption", font=("Helvetica", 16))
label_title.pack(pady=10)

frame_encrypt = ttk.Frame(root)
frame_encrypt.pack(pady=10)

label_msg = ttk.Label(frame_encrypt, text="Enter secret message:")
label_msg.grid(row=0, column=0, padx=10)

entry_msg = ttk.Entry(frame_encrypt, width=30)
entry_msg.grid(row=0, column=1, padx=10)

label_password = ttk.Label(frame_encrypt, text="Enter password:")
label_password.grid(row=1, column=0, padx=10)

entry_password = ttk.Entry(frame_encrypt, show="*", width=30)
entry_password.grid(row=1, column=1, padx=10)

encrypt_button = ttk.Button(root, text="Encrypt Image", command=encrypt_image, style="Accent.TButton", image=tk.PhotoImage(file=os.path.join(os.path.dirname(__file__), "padlock.png")))
encrypt_button.pack(pady=10)

frame_decrypt = ttk.Frame(root)
frame_decrypt.pack(pady=10)

label_passcode = ttk.Label(frame_decrypt, text="Enter passcode for Decryption:")
label_passcode.grid(row=0, column=0, padx=10)

entry_passcode = ttk.Entry(frame_decrypt, show="*", width=30)
entry_passcode.grid(row=0, column=1, padx=10)

decrypt_button = ttk.Button(root, text="Decrypt Image", command=decrypt_image, style="Danger.TButton", image=tk.PhotoImage(file="unlocked.png"))
decrypt_button.pack(pady=10)

result_label = ttk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=10)

root.mainloop()
