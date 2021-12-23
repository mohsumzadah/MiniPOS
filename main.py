from tkinter import *
import tkinter.messagebox


# GLOBAL SETTINGS
FONT = ('Arial', 30)
MONEY_ICON = "$"
TOTAL_MONEY = 0


# DEF
def money_to_total():
    global TOTAL_MONEY
    try:
        taken_money = float(money_entry.get())
    except ValueError:
        tkinter.messagebox.showwarning(title="WARNING", message="Wrong type!")
    else:
        TOTAL_MONEY += taken_money
        total_lbl.configure(text=f"Total: {TOTAL_MONEY}{MONEY_ICON}")


def clear_total_money():
    global TOTAL_MONEY
    if tkinter.messagebox.askyesnocancel(title="Warning", message="Do you want to clear total money?"):
        TOTAL_MONEY = 0
        total_lbl.configure(text=f"Total: {TOTAL_MONEY}{MONEY_ICON}")


# ROOT SETTINGS
root = Tk()
root.title(string="MiniPOS v1")
root.config(padx=150, pady=50)

# WIDGETS SETTINGS
total_lbl = Label(root, text=f"Total: 0{MONEY_ICON}", font=FONT)
total_lbl.grid(row=0, column=2)

total_t_lbl = Label(root, text="Sold:", font=FONT)
total_t_lbl.grid(row=1, column=0, pady=40)

money_entry = Entry(root, width=15, font=FONT)
money_entry.grid(row=1, column=1)

money_icon_lbl = Label(root, text=f"{MONEY_ICON}", font=FONT)
money_icon_lbl.grid(row=1, column=2)

to_total_btn = Button(root, text="ADD", font=FONT, command=money_to_total)
to_total_btn.grid(row=2, column=1)

clear_total_btn = Button(root, text="CLEAR TOTAL MONEY", font=FONT, command=clear_total_money)
clear_total_btn.grid(row=3, column=1, pady=60)


root.mainloop()
