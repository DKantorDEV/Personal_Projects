import random
import tkhotreload as tkhr
import tkinter as tk
from tkinter import scrolledtext

def magic_8_ball(text_area):

    # Random Number for if statements
    random_int = random.randint(1, 20)

    # If statements to be returned
    if random_int  == 1:
        answer = "I'm not sure how to respond to that."
    elif random_int == 2:
        answer = "That is above my pay grade."
    elif random_int == 3:
        answer = "Ask someone else more qualified."
    elif random_int == 4:
        answer = "I think that is a great idea!"
    elif random_int == 5:
        answer = "I don't think you should do that..."
    elif random_int == 6:
        answer = "I will tell you if you pay me."
    elif random_int == 7:
        answer = "Ask me again, I couldn't hear you."
    elif random_int == 8:
        answer = "I can't predict that far into the future."
    elif random_int == 9:
        answer = "I am unable to tell you why."
    elif random_int == 10:
        answer = "All your wishes will come true!"
    elif random_int == 11:
        answer = "You're overthinking it..."
    elif random_int == 12:
        answer = "I agree, you should do that."
    elif random_int == 13:
        answer = "This isn't ChatGPT."
    elif random_int == 14:
        answer = "You do know these answers are pre-written down right?"
    elif random_int == 15:
        answer = "ERROR"
    elif random_int == 16:
        answer = "WARNING: Overheating"
    elif random_int == 17:
        answer = "Hold on... let me ask ChatGPT"
    elif random_int == 18:
        answer = "Let me see if my dog knows the answer to that question."
    elif random_int == 19:
        answer = "My wife said no to your question."
    elif random_int == 20:
        answer = "I don't care."
    else:
        answer = "The spirits are silent.."

    # First - Clears old answer all the way from first line 0 column to the END.
    text_area.delete('1.0', tk.END)

    # Second - The new answer is inserted
    text_area.insert(tk.END, f"Thinking...\n\n8-Ball Says: {answer}")

def main(root):
    # --- GUI Setup ---
    root.wm_title("Magic 8 Ball - HOT RELOAD")
    root.geometry("1200x900")

    # --- Header ---
    tk.Label(root, text="🎱 Magic 8 Ball", font=("Ubuntu Mono", 20, "bold")).pack(pady=20)

    # --- Title Label ---
    title_label = tk.Label(root, text="Ask a Question", font=("Ubuntu Mono", 14, "bold"))
    title_label.pack(pady=10)

    # --- Text Area (Where answer appears) ---
    text_area = scrolledtext.ScrolledText(root, width=90, height=20)
    text_area.pack(padx=20, pady=20)

    # --- The Buttons ---
    start_button = tk.Button(root, text="ASK", command=lambda: magic_8_ball(text_area), bg="#3daee9", fg="yellow", font=("Ubuntu Mono", 12, "bold"))
    start_button.pack(padx=10, pady=10)

# Replacement of root.mainloop() since we have tkhr
if __name__ == "__main__":
    # watch_dir="." tells it to watch the current folder for changes
    tkhr.app(target=main, watch_dir=".")