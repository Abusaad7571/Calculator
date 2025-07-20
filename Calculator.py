from tkinter import *

def buttonClick(number):
    global operator
    operator += str(number)
    input_value.set(operator)

def buttonClear():
    global operator
    operator = ""
    input_value.set("")

def buttonEqual():
    global operator
    try:
        result = str(eval(operator))
        input_value.set(result)
        operator = ""
    except:
        input_value.set("Error")
        operator = ""

def buttonBackspace():
    global operator
    operator = operator[:-1]
    input_value.set(operator)

def on_enter(event, btn, glow):
    btn['bg'] = glow
def on_leave(event, btn, old_bg):
    btn['bg'] = old_bg

def createButton(text, row, col, bg, fg="white", colspan=1, command=None, font_size=19, glow="#00fff7"):
    btn = Button(main,
        text=text,
        padx=12,
        pady=13,
        bd=0,
        fg=fg,
        bg=bg,
        font=("Orbitron", font_size, "bold"),    # Try this modern font, otherwise fallback is below
        activebackground=glow,
        activeforeground="#fff",
        relief="flat",
        cursor="hand2",
        highlightthickness=4,
        highlightcolor=glow,
        highlightbackground=bg,
    )
    # For fallback font:
    try:
        btn.config(font=("Orbitron", font_size, "bold"))
    except:
        btn.config(font=("Consolas", font_size, "bold"))

    btn.config(command=command or (lambda: buttonClick(text)))
    btn.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=5, pady=6)
    btn.bind("<Enter>", lambda event: on_enter(event, btn, glow))
    btn.bind("<Leave>", lambda event: on_leave(event, btn, bg))

main = Tk()
main.title("Neo Calculator")
main.configure(bg="#181b24")

for i in range(6):
    main.rowconfigure(i, weight=1)
for j in range(4):
    main.columnconfigure(j, weight=1)

operator = ""
input_value = StringVar()
# Enhanced Entry style
display_text = Entry(
    main,
    font=("Orbitron", 24, "bold"),
    textvariable=input_value,
    bd=0,
    insertwidth=4,
    bg="#222532",
    fg="#06ffb3",
    insertbackground="#06ffb3",
    justify=RIGHT,
    highlightthickness=4,
    highlightcolor="#7000ff",
    highlightbackground="#181b24",
    relief=FLAT,
)
display_text.grid(row=0, column=0, columnspan=4, pady=12, padx=12, sticky="nsew")

# Neon color palette
neon_purple = "#bb6aff"
neon_blue = "#00e4ff"
neon_green = "#1fff66"
neon_pink = "#ff1fff"
neon_red = "#ff4e71"
neon_yellow = "#ffe100"
dark_btn = "#272c35"
numbers_glow = "#13f0e8"  # cyan glow
ops_glow = "#6a71ff"      # blue-violet glow
clear_glow = "#ff39e6"
eq_glow = "#00ff67"
back_glow = "#ff5050"

# Buttons layout -- (text, row, col, bg, [hover_glow], [command], [font_size], [colspan])
buttons = [
    ("7", 1, 0, dark_btn, numbers_glow),
    ("8", 1, 1, dark_btn, numbers_glow),
    ("9", 1, 2, dark_btn, numbers_glow),
    ("⌫", 1, 3, neon_red, back_glow, lambda: buttonBackspace(), 19),

    ("4", 2, 0, dark_btn, numbers_glow),
    ("5", 2, 1, dark_btn, numbers_glow),
    ("6", 2, 2, dark_btn, numbers_glow),
    ("+", 2, 3, neon_purple, ops_glow),

    ("1", 3, 0, dark_btn, numbers_glow),
    ("2", 3, 1, dark_btn, numbers_glow),
    ("3", 3, 2, dark_btn, numbers_glow),
    ("-", 3, 3, neon_blue, ops_glow),

    (".", 4, 0, dark_btn, numbers_glow),
    ("0", 4, 1, dark_btn, numbers_glow),
    ("/", 4, 2, neon_pink, ops_glow),
    ("*", 4, 3, neon_yellow, ops_glow, None, 19),

    ("C", 5, 0, neon_pink, clear_glow, lambda: buttonClear(), 18, 2),
    ("=", 5, 2, neon_green, eq_glow, lambda: buttonEqual(), 18, 2),
]

for item in buttons:
    text, row, col = item[0], item[1], item[2]
    bg = item[3]
    glow = item[4] if len(item) > 4 else "#00fff7"
    command = item[5] if len(item) > 5 else None
    font_size = item[6] if len(item) > 6 else 19
    colspan = item[7] if len(item) > 7 else 1
    createButton(text, row, col, bg, "white", colspan, command, font_size, glow)

main.mainloop()
