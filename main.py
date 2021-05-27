#!/usr/bin/env python3

import tkinter as tk
import platform, os, random

# General Purpose Variables
# =========================
# Colors
window_bg = "#3f6ff3"
button_bg = "#1afabb"
player_names_bg = ["#ff0000",
                    "#00ff00",
                    "#0000ff",
                    "#0fffff"]
text_bg = "#000000"

# Buttons text names
buttons_text = ["Back",
                 "Exit",
                 "Save",
                 "Add",
                 "Ok",
                 "New Game"]

# Windows' titles
window_title = ["Rummy Score",
                "Set player names",
                "Score"]

# Window sizes
# ============
# Root window (first)
root_window_size_x = "280"
root_window_size_y = "100"

# Name-Entry window (second)
name_entry_window_size_x = "400"
name_entry_window_size_y = "200"

# Score window (third)
score_window_size_x = "664"
score_window_size_y = "96"

# Entries and Labels
# ==================
# Name Entry labels for players
player_name_entry_labels = ["Player_1",
                             "Player_2",
                             "Player_3",
                             "Player_4"]

def main():
    # Root          (main - window)
    root = tk.Tk()
    root.geometry(str(root_window_size_x) + 'x' + str(root_window_size_y))
    root.title(window_title[0])
    root.configure(bg=window_bg)

    # Name-Entry    (toplevel - window)
    def new_game():
        global names
        names = []
        name_entry_top = tk.Toplevel(root)
        name_entry_top.geometry(str(name_entry_window_size_x) + 'x' + str(name_entry_window_size_y))
        name_entry_top.title(window_title[1])
        name_entry_top.configure(bg=window_bg)
        root.withdraw()

        # Name Entries Frame
        name_entry_frame = tk.Frame(name_entry_top)
        name_entry_frame.pack()

        # Name Entries
        # ============
        # Player-1 Entry
        player_one_entry = tk.Entry(name_entry_frame)
        player_one_entry.insert(0, player_name_entry_labels[0])
        #player_one_entry.configure(state=tk.DISABLED)
        player_one_entry.grid(row=0, column=1)

        def empty_p1_insert(event):
            #player_one_entry.configure(state=tk.NORMAL)
            player_one_entry.delete(first=0, last=len(player_name_entry_labels[0]))
            player_one_entry.insert(0, '')
            player_one_entry.grid(row=0, column=1)

        player_one_entry.bind("<Button-1>", empty_p1_insert)

        # Player-2 Entry
        player_two_entry = tk.Entry(name_entry_frame)
        player_two_entry.insert(0, player_name_entry_labels[1])
        #player_two_entry.configure(state=tk.DISABLED)
        player_two_entry.grid(row=1, column=1)

        def empty_p2_insert(event):
            #player_two_entry.configure(state=tk.NORMAL)
            player_two_entry.delete(first=0, last=len(player_name_entry_labels[1]))
            player_two_entry.insert(0, '')
            player_two_entry.grid(row=1, column=1)

        player_two_entry.bind("<Button-1>", empty_p2_insert)

        # Player-3 Entry
        player_three_entry = tk.Entry(name_entry_frame)
        player_three_entry.insert(0, player_name_entry_labels[2])
        #player_three_entry.configure(state=tk.DISABLED)
        player_three_entry.grid(row=2, column=1)

        def empty_p3_insert(event):
            #player_three_entry.configure(state=tk.NORMAL)
            player_three_entry.delete(first=0, last=len(player_name_entry_labels[2]))
            player_three_entry.insert(0, '')
            player_three_entry.grid(row=2, column=1)

        player_three_entry.bind("<Button-1>", empty_p3_insert)

        # Player-4 Entry
        player_four_entry = tk.Entry(name_entry_frame)
        player_four_entry.insert(0, player_name_entry_labels[3])
        #player_four_entry.configure(state=tk.DISABLED)
        player_four_entry.grid(row=3, column=1)

        def empty_p4_insert(event):
            #player_four_entry.configure(state=tk.NORMAL)
            player_four_entry.delete(first=0, last=len(player_name_entry_labels[3]))
            player_four_entry.insert(0, '')
            player_four_entry.grid(row=3, column=1)

        player_four_entry.bind("<Button-1>", empty_p4_insert)

        # Score-Display (toplevel - window)
        def ok():
            # ".get()" the names entered by the players
            player_one = player_one_entry.get()
            player_two = player_two_entry.get()
            player_three = player_three_entry.get()
            player_four = player_four_entry.get()

            all_p = [player_one, player_two, player_three, player_four]

            # This will make sure there are no duplicate file names
            rand_file_num = random.randint(0,99999)
            for file_name in range(len(all_p)):
                if all_p[file_name]+'.txt' in os.listdir():
                    all_p[file_name] = all_p[file_name] + f'_{rand_file_num}'
                else:
                    continue

            # 'player 1 file'
            f_1 = open(f"{all_p[0]}.txt", 'w')
            f_1.write('0')
            f_1.close()

            # 'player 2 file'
            f_2 = open(f"{all_p[1]}.txt", 'w')
            f_2.write('0')
            f_2.close()

            # 'player 3 file'
            f_3 = open(f'{all_p[2]}.txt', 'w')
            f_3.write('0')
            f_3.close()

            # 'player 4 file'
            f_4 = open(f'{all_p[3]}.txt', 'w')
            f_4.write('0')
            f_4.close()

            # Create Score (Toplevel - window)
            score_top = tk.Toplevel(root)
            score_top.geometry(str(score_window_size_x) + 'x' + str(score_window_size_y) )
            score_top.title(window_title[2])
            score_top.configure(bg=window_bg)

            # Destroy Name Entry (toplevel - window)
            name_entry_top.destroy()

            # Score Name Labels Frame
            p_name_frame = tk.Frame(score_top)
            p_name_frame.configure(bg = button_bg)
            p_name_frame.pack()

            # Name Labels (in Score toplevel-window in p_name_frame Frame)
            pl_1 = tk.Label(p_name_frame, text=all_p[0], bg=button_bg)
            pl_2 = tk.Label(p_name_frame, text=all_p[1], bg=button_bg)
            pl_3 = tk.Label(p_name_frame, text=all_p[2], bg=button_bg)
            pl_4 = tk.Label(p_name_frame, text=all_p[3], bg=button_bg)
            # Grid the Name Labels (in Score toplevel-window in p_name_frame Frame)
            pl_1.grid(row=0, column=0)
            pl_2.grid(row=0, column=1)
            pl_3.grid(row=0, column=2)
            pl_4.grid(row=0, column=3)

            # Score Entries (in Score toplevel-window in p_name_frame Frame)
            score_p_1 = tk.Entry(p_name_frame)
            score_p_2 = tk.Entry(p_name_frame)
            score_p_3 = tk.Entry(p_name_frame)
            score_p_4 = tk.Entry(p_name_frame)
            # Grid Score Entries (in Score toplevel-window in p_name_frame Frame)
            score_p_1.grid(row=1, column=0)
            score_p_2.grid(row=1, column=1)
            score_p_3.grid(row=1, column=2)
            score_p_4.grid(row=1, column=3)

            # Score Display Label
            score_display_1 = tk.Label(p_name_frame, text='0', bg = button_bg)
            score_display_2 = tk.Label(p_name_frame, text='0', bg = button_bg)
            score_display_3 = tk.Label(p_name_frame, text='0', bg = button_bg)
            score_display_4 = tk.Label(p_name_frame, text='0', bg = button_bg)
            # Grid Score Display (labels)
            score_display_1.grid(row=2, column=0)
            score_display_2.grid(row=2, column=1)
            score_display_3.grid(row=2, column=2)
            score_display_4.grid(row=2, column=3)

            # Functions for Buttons (in Score toplevel-window in score_buttons_frame Frame)
            # Calculate/Add Scores Button
            def calculate():
                '''
                1.1. '.get()' score from entry and write to file
                2.   if second-or-more score entered, '.get()' score from entry
                2.1. read last score from 'player_name.txt' and ADD it to the score entered
                2.2. write Total score to 'player_name.txt'
                3.   Add Label in Window with the new Total Score
                3.1. clear Score Entry slots
                '''

                # Get scores entered
                score_1 = score_p_1.get()
                score_2 = score_p_2.get()
                score_3 = score_p_3.get()
                score_4 = score_p_4.get()

                # Open score-files to Read last score
                f_1 = open(f'{all_p[0]}.txt', 'r')
                last_1 = f_1.read()
                f_1.close()

                f_2 = open(f'{all_p[1]}.txt', 'r')
                last_2 = f_2.read()
                f_2.close()

                f_3 = open(f'{all_p[2]}.txt', 'r')
                last_3 = f_3.read()
                f_3.close()

                f_4 = open(f'{all_p[3]}.txt', 'r')
                last_4 = f_4.read()
                f_4.close()

                # Add last score from file with the last score entered
                new_1 = int(score_1) + int(last_1)
                new_2 = int(score_2) + int(last_2)
                new_3 = int(score_3) + int(last_3)
                new_4 = int(score_4) + int(last_4)

                # Open score-files to Write new score
                f_1 = open(f'{all_p[0]}.txt', 'w')
                f_1.write(str(new_1))
                f_1.close()

                f_2 = open(f'{all_p[1]}.txt', 'w')
                f_2.write(str(new_2))
                f_2.close()

                f_3 = open(f'{all_p[2]}.txt', 'w')
                f_3.write(str(new_3))
                f_3.close()

                f_4 = open(f'{all_p[3]}.txt', 'w')
                f_4.write(str(new_4))
                f_4.close()

                # Delete last score-label-displays
                score_display_1.forget()
                score_display_2.forget()
                score_display_3.forget()
                score_display_4.forget()

                # Set new score-label-display text
                score_display_1['text'] = new_1
                score_display_2['text'] = new_2
                score_display_3['text'] = new_3
                score_display_4['text'] = new_4

                # Grid New Score Display (labels)
                score_display_1.grid(row=2, column=0)
                score_display_2.grid(row=2, column=1)
                score_display_3.grid(row=2, column=2)
                score_display_4.grid(row=2, column=3)

            # Exit program
            def exit_score():
                # Save to file window
                save_or_not = tk.Toplevel(score_top)
                save_or_not.title("Save scores?")
                save_or_not.geometry("280x70")
                save_or_not.configure(bg=window_bg)

                # Frame for Label & Buttons
                save_frame = tk.Frame(save_or_not, bg=window_bg)
                save_frame.pack()
                # "Do you want to save?" Label
                save_label = tk.Label(save_frame, text="Do you want to save the scores?", bg=window_bg)
                save_label.grid(row=0, column=0, columnspan=2)

                def yes_button():
                    root.destroy()

                def no_button():
                    c = 0
                    if "Windows" in platform.platform():
                        for file_name in all_p:
                            os.system(f"erase {all_p[c]}.txt")
                            c += 1
                    elif "Linux" in platform.platform():
                        for file_name in all_p:
                            os.system(f"rm {all_p[c]}.txt")
                            c += 1
                    root.destroy()

                # No/Yes Buttons
                yes_b = tk.Button(save_frame, text="Yes",bg=button_bg, command=yes_button)
                yes_b.grid(row=1, column=0)
                no_b = tk.Button(save_frame, text="No",bg=button_bg, command=no_button)
                no_b.grid(row=1, column=1)



            # Frame for Buttons (in Score toplevel-window)
            score_buttons_frame = tk.Frame(score_top, bg=window_bg)
            score_buttons_frame.pack()

            # Buttons (in Score toplevel-window in score_buttons_frame Frame)
            calculate_b = tk.Button(score_buttons_frame, text="Calculate", bg=button_bg, command=calculate)
            exit_b = tk.Button(score_buttons_frame, text="Exit", bg=button_bg, command=exit_score)
            calculate_b.grid(row=0, column=0)
            exit_b.grid(row=0, column=1)


        # Name Entry Window ( in name entry frame) buttons
        name_entry_buttons_frame = tk.Frame(name_entry_top)
        name_entry_buttons_frame.pack()
        ok_button = tk.Button(name_entry_buttons_frame, text="Ok", bg = button_bg, command=ok)
        ok_button.grid(row=0, column=2)
        exit_button = tk.Button(name_entry_buttons_frame, text="Exit", bg=button_bg, command=exit_app)
        exit_button.grid(row=0, column=1)

    def exit_app():
        root.destroy()
    # Root window buttons
    open_name_entry_top = tk.Button(root, text=buttons_text[-1], bg=button_bg, command=new_game)
    open_name_entry_top.pack()
    exit_program = tk.Button(root, text=buttons_text[1], bg=button_bg, command=exit_app)
    exit_program.pack()

    # Main Loop
    root.mainloop()

if __name__ == "__main__":
    main()
