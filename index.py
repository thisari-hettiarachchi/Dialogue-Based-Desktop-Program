import tkinter as tk
from tkinter import scrolledtext
import random
import json
from PIL import Image, ImageTk  
from fuzzywuzzy import process 

root = tk.Tk()
root.title("Programming Tutor")
root.geometry("400x500")
root.configure(bg="#ffffff")

user_img = Image.open("assets/user.png").resize((30, 30))
user_icon = ImageTk.PhotoImage(user_img)

bot_img = Image.open("assets/bot.png").resize((30, 30))
bot_icon = ImageTk.PhotoImage(bot_img)

top_frame = tk.Frame(root, bg="#7b1fa2", height=60)
top_frame.pack(fill="x")
top_frame.pack_propagate(False)

title_label = tk.Label(top_frame, text="Hi. How can I help you?", font=("Arial", 12), fg="white", bg="#7b1fa2")
title_label.pack(pady=10)

chat_frame = tk.Frame(root, bg="#ffffff")
chat_frame.pack(fill="both", expand=True, padx=10, pady=5)

canvas = tk.Canvas(chat_frame, bg="#ffffff")
scrollbar = tk.Scrollbar(chat_frame, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="#ffffff")

scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

bottom_frame = tk.Frame(root, bg="#7b1fa2", height=50)
bottom_frame.pack(fill="x", side="bottom")

entry = tk.Entry(bottom_frame, font=("Arial", 12), width=30, bg="#e0e0e0")
entry.pack(side="left", padx=10, pady=10, expand=True, fill="x")

send_button = tk.Button(bottom_frame, text="Send", font=("Arial", 12), bg="#4a0072", fg="white", padx=10)
send_button.pack(side="right", padx=10, pady=10)

with open('intents.json', 'r', encoding='utf-8') as f:
    intents = json.load(f)

def respond():
    sentence = entry.get().strip()
    if not sentence:
        return
    entry.delete(0, tk.END)
    
    user_frame = tk.Frame(scrollable_frame, bg="#ffffff")
    user_frame.pack(anchor="e", pady=2, padx=(2, 20))  

    tk.Label(user_frame, image=user_icon, bg="#ffffff").pack(side="right", padx=(2, 2)) 
    tk.Label(user_frame, text=sentence, font=("Arial", 10), fg="blue", bg="#f0f0f0", padx=4, pady=4).pack(side="right")

    patterns = {p: intent for intent in intents['intents'] for p in intent['patterns']}
    best_match, confidence = process.extractOne(sentence, patterns.keys(), score_cutoff=60)  
    
    if best_match:
        best_intent = patterns[best_match]
        response = random.choice(best_intent['responses'])
    else:
        response = "Sorry, I don't understand. Please ask another question."
    
    bot_frame = tk.Frame(scrollable_frame, bg="#ffffff")
    bot_frame.pack(anchor="w", pady=2, padx=5)
    
    tk.Label(bot_frame, image=bot_icon, bg="#ffffff").pack(side="left")
    tk.Label(bot_frame, text=response, font=("Arial", 10), fg="green", bg="#e0f7fa", padx=8, pady=5, wraplength=1350, justify="left").pack(side="left")

    
    canvas.update_idletasks()
    canvas.yview_moveto(1)


send_button.config(command=respond)
root.mainloop()
entry.bind("<Return>", lambda event: respond())

