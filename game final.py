from tkinter import *
import random

root = Tk()
root.geometry("600x600")
root.title("Rock Paper Scissor Game")
root.configure(bg="lightgray")

computer_value = {
    "0": "Rock",
    "1": "Paper",
    "2": "Scissor"
}

player_score = 0
computer_score = 0
draw_count = 0
round_number = 1
total_rounds = random.randint(5, 9)
player_name = StringVar()  # Define player_name variable

def reset_game():
    global player_score, computer_score, draw_count, round_number, total_rounds
    player_score = 0
    computer_score = 0
    draw_count = 0
    round_number = 1
    total_rounds = random.randint(5, 9)
    update_score()
    l1.config(text="")
    l3.config(text="Computer: ")
    l4.config(text="")
    l6.config(text="")
    b1["state"] = "disabled"
    b2["state"] = "disabled"
    b3["state"] = "disabled"
    submit_button.config(state="active")  # Set submit button to active state
    name_entry.config(state="normal")  # Enable name entry field after reset

def button_disable():
    b1["state"] = "disabled"
    b2["state"] = "disabled"
    b3["state"] = "disabled"

def show_computer_input(computer_choice):
    l3.config(text=f"\tComputer: {computer_choice}")

def update_score():
    l5.config(text=f"{player_name.get()} Score: {player_score}\nComputer: {computer_score}\nDraw: {draw_count}\nRounds: {total_rounds}")

def end_game():
    global player_score, computer_score
    if player_score > computer_score:
        game_result = f"{player_name.get()} Win!"
    elif player_score < computer_score:
        game_result = "Computer wins!"
    else:
        game_result = "It's a tie!"
    l6.config(text=game_result)
    button_disable()

def isrock():
    global player_score, computer_score, draw_count, round_number
    computer_choice = computer_value[str(random.randint(0, 2))]
    show_computer_input(computer_choice)
    if computer_choice == "Rock":
        match_result = "Match Draw"
        draw_count += 1
    elif computer_choice == "Scissor":
        match_result = f"{player_name.get()} Win"
        player_score += 1
    else:
        match_result = "Computer Win"
        computer_score += 1
    l4.config(text=match_result)
    l1.config(text=f"{player_name.get()} - Rock \n")
    update_score()
    round_number += 1
    if round_number > total_rounds:
        end_game()

def ispaper():
    global player_score, computer_score, draw_count, round_number
    computer_choice = computer_value[str(random.randint(0, 2))]
    show_computer_input(computer_choice)
    if computer_choice == "Paper":
        match_result = "Match Draw"
        draw_count += 1
    elif computer_choice == "Scissor":
        match_result = "Computer Win"
        computer_score += 1
    else:
        match_result = f"{player_name.get()} Win"
        player_score += 1
    l4.config(text=match_result)
    l1.config(text=f"{player_name.get()} - Paper \n")
    update_score()
    round_number += 1
    if round_number > total_rounds:
        end_game()

def isscissor():
    global player_score, computer_score, draw_count, round_number
    computer_choice = computer_value[str(random.randint(0, 2))]
    show_computer_input(computer_choice)
    if computer_choice == "Rock":
        match_result = "Computer Win"
        computer_score += 1
    elif computer_choice == "Scissor":
        match_result = "Match Draw"
        draw_count += 1
    else:
        match_result = f"{player_name.get()} Win"
        player_score += 1
    l4.config(text=match_result)
    l1.config(text=f"{player_name.get()} - Scissor\n")
    update_score()
    round_number += 1
    if round_number > total_rounds:
        end_game()

def submit_name():
    name = player_name.get().strip()
    if name:
        submit_button.config(state="disabled")
        l1.config(text=f"{player_name.get()}' VS ")
        b1.config(state="active")
        b2.config(state="active")
        b3.config(state="active")
        root.title(f"Live {player_name.get()} vs Computer")
        name_entry.config(state="disabled")  # Disable name entry field after submission
    else:
        messagebox.showerror("Error", "Please enter your name.")

def button_hover(event):
    event.widget.config(bg="darkgray")

def button_leave(event):
    event.widget.config(bg="lightgray")

# UI elements
Label(root, text="Rock Paper Scissor", font="normal 20 bold", fg="blue", bg="lightgray").pack(pady=20)

frame = Frame(root, bg="lightgray")
frame.pack()

l1 = Label(frame, text=f"{player_name.get()}", font=10, bg="lightgray")
l3 = Label(frame, text="Computer:  ", font=10, bg="lightgray")
l1.pack(side=LEFT, pady=5)
l3.pack(pady=5)



l4 = Label(root, text="", font="normal 20 bold", bg="white", width=15, borderwidth=2, relief="solid")
l4.pack(pady=20)

l5 = Label(root, text="", font="normal 12 bold", bg="lightgray")
l5.pack()

l6 = Label(root, text="", font="normal 16 bold", fg="red", bg="lightgray")
l6.pack()

frame1 = Frame(root, bg="lightgray")
frame1.pack()

b1 = Button(frame1, text="Rock", font=10, width=7, command=isrock, state="disabled", bg="gray")
b2 = Button(frame1, text="Paper", font=10, width=7, command=ispaper, state="disabled", bg="gray")
b3 = Button(frame1, text="Scissor", font=10, width=7, command=isscissor, state="disabled", bg="gray")
b1.pack(side=LEFT, padx=10)
b2.pack(side=LEFT, padx=10)
b3.pack(padx=10)

Label(root, text="Enter Player Name:", font="normal 10 bold", bg="lightgray").pack()
name_entry = Entry(root, textvariable=player_name, bg="white")  # Bind player_name variable to Entry widget
name_entry.pack()

submit_button = Button(root, text="Submit", font=10, fg="blue", command=submit_name, bg="gray")
submit_button.pack(pady=10)

Button(root, text="Reset Game", font=10, fg="red", bg="black", command=reset_game).pack(pady=20)

root.mainloop()
