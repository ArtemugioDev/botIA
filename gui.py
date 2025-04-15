import tkinter as tk
import requests
import pyttsx3

def send_message():
    user_input = entry.get()
    response = requests.post("http://localhost:5000/chat", json={"message": user_input}).json()
    chat_history.insert(tk.END, f"Tú: {user_input}\nBot: {response['reply']}\n\n")
    engine = pyttsx3.init()
    engine.say(response["reply"])
    engine.runAndWait()

root = tk.Tk()
root.title("Chatbot IA")

chat_history = tk.Text(root, width=50, height=20)
chat_history.pack()

entry = tk.Entry(root, width=50)
entry.pack()

send_button = tk.Button(root, text="Enviar", command=send_message)
send_button.pack()

root.mainloop()