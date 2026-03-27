#без предустановки файлом setup.exe, launcher НЕ ФУНКЦИОНИРУЕТ
import tkinter as tk
import subprocess

def start_app(path):
    subprocess.Popen(path)

root = tk.Tk()
root.title("Resurrect Windows 7 manager")
root.geometry("600x400")

# Общий контейнер для текста и кнопок (чтобы всё было по центру)
main_container = tk.Frame(root)
main_container.place(relx=0.5, rely=0.5, anchor="center")

# Текст в самом начале
label = tk.Label(main_container, text="Resurrect Windows 7 manager", font=("Arial", 24))
label.pack(pady=20)

# Контейнер только для кнопок (чтобы они были в ряд)
button_frame = tk.Frame(main_container)
button_frame.pack()

# Загрузка картинок
img1 = tk.PhotoImage(file="cmd.png")
img2 = tk.PhotoImage(file="int.png")
img3 = tk.PhotoImage(file="upd.png")

# Кнопки
tk.Button(button_frame, image=img1, command=lambda: start_app("kex.exe"), borderwidth=0).pack(side="left", padx=10)
tk.Button(button_frame, image=img2, command=lambda: start_app("C:\Program Files\Supermium\chrome.exe"), borderwidth=0).pack(side="left", padx=10)
tk.Button(button_frame, image=img3, command=lambda: start_app("upd.exe"), borderwidth=0).pack(side="left", padx=10)

root.mainloop()
