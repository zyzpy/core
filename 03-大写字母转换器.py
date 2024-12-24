import tkinter as tk
from tkinter import ttk

def convert_to_uppercase():
    letter = input_entry.get().lower()
    if letter.isalpha() and len(letter) == 1:
        # 显示正在计算的提示文字
        result_label.config(text="请稍后，正在努力计算中...", font=("Arial", 14), fg="green")
        root.update_idletasks()  # 确保提示文字显示

        # 立即计算结果
        result = letter.upper()
        result_label.config(text=f"计算完成：{result}", font=("Arial", 14), fg="black")
    else:
        result_label.config(text="请输入一个有效的小写字母", font=("Arial", 14), fg="red")

def reset():
    input_entry.delete(0, tk.END)
    result_label.config(text="")
    progress_var.set(0)

# 创建主窗口
root = tk.Tk()
root.title("大写字母生成器")
root.geometry("400x250")
root.resizable(False, False)

# 让窗口居中
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = int((screen_width/2) - (400/2))
y_coordinate = int((screen_height/2) - (250/2))
root.geometry(f"400x250+{x_coordinate}+{y_coordinate}")

# 输入标签和文本框
input_label = tk.Label(root, text="请输入小写字母:", font=("Arial", 14))
input_label.pack(pady=10)

input_entry = tk.Entry(root, font=("Arial", 14))
input_entry.pack(pady=5)

# 结果显示标签
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

# 进度条
progress_var = tk.IntVar()
progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100)
progress_bar.pack(pady=10)

# 按钮
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

convert_button = tk.Button(button_frame, text="转换", command=convert_to_uppercase, width=12)
convert_button.pack(side="left", padx=10)

reset_button = tk.Button(button_frame, text="重置", command=reset, width=12)
reset_button.pack(side="right", padx=10)

root.mainloop()
