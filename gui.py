import tkinter as tk
from tkinter import messagebox
from analyzer import rate_password, recommendations, calculate_entropy

def analyze_password():
    password = entry.get()
    if not password:
        messagebox.showwarning("Input Error", "Please enter a password!")
        return

    strength = rate_password(password)
    entropy = calculate_entropy(password)
    tips = recommendations(password)

    result_text = f"Password Strength: {strength}\nEntropy: {entropy} bits\n\nRecommendations:\n"
    if tips:
        for tip in tips:
            result_text += f"- {tip}\n"
    else:
        result_text += "Your password is strong! 👍"

    result_label.config(text=result_text)

# GUI window
root = tk.Tk()
root.title("Password Analyzer")
root.geometry("500x400")

tk.Label(root, text="Enter your password:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, width=40, font=("Arial", 12), show="*")
entry.pack(pady=5)

tk.Button(root, text="Analyze", command=analyze_password, font=("Arial", 12)).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 11), justify="left")
result_label.pack(pady=10)

root.mainloop()
