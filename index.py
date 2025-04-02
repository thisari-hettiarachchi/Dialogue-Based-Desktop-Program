import tkinter as tk
from tkinter import scrolledtext
import random
import json
from PIL import Image, ImageTk  # Importing Pillow

root = tk.Tk()
root.title("Programming Tutor")
root.geometry("350x450")
root.configure(bg="#ffffff")

top_frame = tk.Frame(root, bg="#7b1fa2", height=60)
top_frame.pack(fill="x")
top_frame.pack_propagate(False)

# Open the image using Pillow
image = Image.open("profile.png")

# Resize the image to fit a smaller size (e.g., 40x40)
image = image.resize((40, 40))

profile_image = ImageTk.PhotoImage(image)

profile_icon = tk.Label(top_frame, image=profile_image, bg="#7b1fa2")
profile_icon.pack(side="left", padx=10, pady=10)

title_label = tk.Label(top_frame, text="Chat support", font=("Arial", 12, "bold"), fg="white", bg="#7b1fa2")
title_label.pack(anchor="w", padx=40)

desc_label = tk.Label(top_frame, text="Hi. How can I help you?", font=("Arial", 10), fg="white", bg="#7b1fa2")
desc_label.pack(anchor="w", padx=40)

chat_frame = tk.Frame(root, bg="#ffffff", height=300)
chat_frame.pack(fill="both", expand=True, padx=10, pady=5)

chat_box = tk.Text(chat_frame, bg="#f5f5f5", state="disabled", wrap="word")
chat_box.pack(fill="both", expand=True)

bottom_frame = tk.Frame(root, bg="#7b1fa2", height=50)
bottom_frame.pack(fill="x", side="bottom")

entry = tk.Entry(bottom_frame, font=("Arial", 12), width=30, bg="#e0e0e0")
entry.pack(side="left", padx=10, pady=10, expand=True, fill="x")

send_button = tk.Button(bottom_frame, text="Send", font=("Arial", 12), bg="#4a0072", fg="white", padx=10)
send_button.pack(side="right", padx=10, pady=10)

# Placeholder for the previous chatbot code
def tokenize(sentence):
    return sentence.split()

def stem(word):
    return word.lower()

def bag_of_words(tokenized_sentence, words):
    sentence_words = [stem(word) for word in tokenized_sentence]
    bag = [1 if w in sentence_words else 0 for w in words]
    return bag

# Load intents
with open('intents.json', 'r') as f:
    intents = json.load(f)

all_words = []
tags = []
x_data = []
y_data = []

for intent in intents['intents']:
    for pattern in intent['patterns']:
        tokenized_words = tokenize(pattern)
        all_words.extend(tokenized_words)
        x_data.append(tokenized_words)
        y_data.append(intent['tag'])

    if intent['tag'] not in tags:
        tags.append(intent['tag'])

ignore_words = ['?', '!', '.', ',']
all_words = [stem(w) for w in all_words if w not in ignore_words]
all_words = sorted(set(all_words))
tags = sorted(set(tags))

x_train = []
y_train = []

for sentence in x_data:
    bag = bag_of_words(sentence, all_words)
    x_train.append(bag)
    label = tags.index(y_data[x_data.index(sentence)])
    y_train.append(label)

# Mock NeuralNet class
class NeuralNet:
    def __init__(self, input_size, hidden_size, output_size):
        pass

    def forward(self, x):
        return [0.5] * len(tags)

# Chatbot interaction
def respond():
    sentence = entry.get()
    if sentence.lower() == "quit":
        root.quit()
        return
    tokenized_sentence = tokenize(sentence)
    bag = bag_of_words(tokenized_sentence, all_words)

    output = model.forward(bag)
    predicted = max(output)
    tag = tags[output.index(predicted)]

    response = ""
    for intent in intents['intents']:
        if intent['tag'] == tag:
            response = random.choice(intent['responses'])
            break

    # Display user message (right side) and bot response (left side)
    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, f"\nYou: {sentence}", 'user')
    chat_box.insert(tk.END, f"\nBot: {response}", 'bot')
    chat_box.config(state=tk.DISABLED)
    chat_box.yview(tk.END)
    entry.delete(0, tk.END)

# Define tags for user and bot messages
chat_box.tag_configure('user', foreground='blue', justify='right')  # User message style (right side)
chat_box.tag_configure('bot', foreground='green', justify='left')   # Bot message style (left side)

# Mock Neural Network initialization
input_size = len(x_train[0])
hidden_size = 8
output_size = len(tags)
model = NeuralNet(input_size, hidden_size, output_size)

# Send button command
send_button.config(command=respond)

# Start the main Tkinter loop
root.mainloop()
