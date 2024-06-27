import tkinter as tk
from tkinter import messagebox
import instaloader
import threading
import os
from PIL import Image, ImageTk

def download_and_show_profile_pic():
    username = username_entry.get()
    if not username:
        messagebox.showerror("Error", "Please enter a username")
        return

    status_label.config(text="Downloading...")
    download_button.config(state="disabled")

    def download_thread():
        try:
            ig = instaloader.Instaloader()
            ig.download_profile(username, profile_pic_only=True)
            
        
            folder_path = os.path.join(os.getcwd(), username)
            for file in os.listdir(folder_path):
                if file.endswith(".jpg") and "profile_pic" in file:
                    image_path = os.path.join(folder_path, file)
                    break
            else:
                raise Exception("Downloaded image not found")

            
            image = Image.open(image_path)
            show_image(image)

            status_label.config(text="Profile picture downloaded and displayed")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            status_label.config(text="")
        finally:
            download_button.config(state="normal")

    threading.Thread(target=download_thread, daemon=True).start()

def show_image(image):
    
    max_size = (400, 400)
    image.thumbnail(max_size)

    
    photo = ImageTk.PhotoImage(image)

    
    image_label.config(image=photo)
    image_label.image = photo  
    
    
    image_label.pack(pady=10)

    
    root.geometry("400x550")


root = tk.Tk()
root.title("Instagram Profile Picture Downloader")
root.geometry("350x150")  


username_label = tk.Label(root, text="Enter Instagram username:")
username_label.pack(pady=5)

username_entry = tk.Entry(root, width=30)
username_entry.pack(pady=5)

download_button = tk.Button(root, text="Download and Show Profile Picture", command=download_and_show_profile_pic)
download_button.pack(pady=10)

status_label = tk.Label(root, text="")
status_label.pack(pady=5)


image_label = tk.Label(root)


root.mainloop()