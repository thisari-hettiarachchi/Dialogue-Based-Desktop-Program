import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Chat Support")
root.geometry("350x450")
root.configure(bg="#ffffff")

# Top frame with agent info
top_frame = tk.Frame(root, bg="#7b1fa2", height=60)
top_frame.pack(fill="x")
top_frame.pack_propagate(False)

profile_icon = tk.Label(top_frame, text="👤", font=("Arial", 14), bg="#7b1fa2")
profile_icon.pack(side="left", padx=10, pady=10)

title_label = tk.Label(top_frame, text="Chat support", font=("Arial", 12, "bold"), fg="white", bg="#7b1fa2")
title_label.pack(anchor="w", padx=40)

desc_label = tk.Label(top_frame, text="Hi. My name is Sam. How can I help you?", font=("Arial", 10), fg="white", bg="#7b1fa2")
desc_label.pack(anchor="w", padx=40)

# Chat display frame
chat_frame = tk.Frame(root, bg="#ffffff", height=300)
chat_frame.pack(fill="both", expand=True, padx=10, pady=5)

chat_box = tk.Text(chat_frame, bg="#f5f5f5", state="disabled", wrap="word")
chat_box.pack(fill="both", expand=True)

# Bottom input frame
bottom_frame = tk.Frame(root, bg="#7b1fa2", height=50)
bottom_frame.pack(fill="x", side="bottom")

entry = tk.Entry(bottom_frame, font=("Arial", 12), width=30, bg="#e0e0e0")
entry.pack(side="left", padx=10, pady=10, expand=True, fill="x")

send_button = tk.Button(bottom_frame, text="Send", font=("Arial", 12), bg="#4a0072", fg="white", padx=10)
send_button.pack(side="right", padx=10, pady=10)

root.mainloop()
