import random
from tkinter import *
from PIL import Image, ImageTk


class GUI:
    computer_win = 0
    player_win = 0
    games_times = 0
    tie_count = 0

    def __init__(self, window):

        self.user_img = Image.open("User.png")
        self.user_img = self.user_img.resize((160, 160), Image.ANTIALIAS)
        self.user = ImageTk.PhotoImage(self.user_img)

        self.paper_img_P = Image.open("Paper.jpg")
        self.paper_img_P = self.paper_img_P.resize((160, 160), Image.ANTIALIAS)
        self.paper = ImageTk.PhotoImage(self.paper_img_P)

        self.scissors_img_P = Image.open("Scissor.jpg")
        self.scissors_img_P = self.scissors_img_P.resize((160, 160), Image.ANTIALIAS)
        self.scissors = ImageTk.PhotoImage(self.scissors_img_P)

        self.rock_img = Image.open("Rock.jpg")
        self.rock_img = self.rock_img.resize((160, 160), Image.ANTIALIAS)
        self.rock = ImageTk.PhotoImage(self.rock_img)

        self.computer_img = Image.open("Computer.png")
        self.computer_img = self.computer_img.resize((160, 160), Image.ANTIALIAS)
        self.computer = ImageTk.PhotoImage(self.computer_img)

        self.paper_img_C = Image.open("PaperC.jpg")
        self.paper_img_C = self.paper_img_C.resize((160, 160), Image.ANTIALIAS)
        self.paper_C = ImageTk.PhotoImage(self.paper_img_C)

        self.scissors_img_C = Image.open("ScissorC.jpg")
        self.scissors_img_C = self.scissors_img_C.resize((160, 160), Image.ANTIALIAS)
        self.scissors_C = ImageTk.PhotoImage(self.scissors_img_C)

        self.rock_img_C = Image.open("RockC.png")
        self.rock_img_C = self.rock_img_C.resize((160, 160), Image.ANTIALIAS)
        self.rock_C = ImageTk.PhotoImage(self.rock_img_C)

        self.all_choices = [self.paper, self.scissors, self.rock]
        self.win_list = [[self.paper, self.rock], [self.rock, self.scissors], [self.scissors, self.paper]]

        self.window = window

        self.label_title = Label(self.window, text='ROCK, PAPER, SCISSORS', font='Arial， 20')
        self.label_title.place(x=210, y=20)

        self.label_user = Label(self.window, text='USER')
        self.label_user.place(x=100, y=100)

        self.label_computer = Label(self.window, text='COMPUTER')
        self.label_computer.place(x=450, y=100)

        self.label_score= Label(self.window, text=str(GUI.player_win) + ':' + str(GUI.computer_win), font='Arial， 35', bg='red')
        self.label_score.place(x=280, y=80)

        self.label_tieCount = Label(self.window, text=f'Tie: {GUI.tie_count}', font='Arial， 15', bg='white')
        self.label_tieCount.place(x=285, y=130)

        self.user_IMG = Label(self.window, image=self.user)
        self.user_IMG.place(x=50, y=140)

        self.computer_IMG = Label(self.window, image=self.computer)
        self.computer_IMG.place(x=410, y=140)

        self.combobox_label = Label(self.window, text='SELECT CHOICE')
        self.combobox_label.place(x=85, y=310)

        #self.combobox = ttk.Combobox(self.window, values=('Rock', 'Paper', 'Scissors'))
        #self.combobox.current(None)
        #self.combobox.place(x=55, y=330, width=160)

        self.radio_1 = StringVar()
        self.radio_1.set(NONE)
        self.radio_rock = Radiobutton(self.window, text='Rock', variable=self.radio_1, value='Rock', command=self.radio)
        self.radio_paper = Radiobutton(self.window, text='Paper', variable=self.radio_1, value='Paper', command=self.radio)
        self.radio_scissors = Radiobutton(self.window, text='Scissors', variable=self.radio_1, value='Scissors', command=self.radio)
        self.radio_rock.place(x=30, y=330)
        self.radio_paper.place(x=90, y=330)
        self.radio_scissors.place(x=150, y=330)

        self.label_VS = Label(self.window, text='VS', font='(Arial, 30')
        self.label_VS.place(x=280, y=200)

        self.button_play = Button(self.window, text='PLAY', font='Arial, 30', command=self.play)
        self.button_play['state'] = 'disabled'
        self.button_play.place(x=250, y=450)

        self.bottom_restart = Button(self.window, text='Try Again', font='Arial, 10', command=self.restart)
        self.bottom_restart.place(x=450, y=500)

        self.label_tie = Label(self.window, text=f'This round you TIE.')
        self.label_youWin = Label(self.window, text='This round you WIN.')
        self.label_computerWin = Label(self.window, text='This round computer WIN.')

        self.label_tipCwin = Label(self.window, text='Game Over. Computer win.')
        self.label_tipYwin = Label(self.window, text='Congratulation. You win.', fg='red')
        self.label_tipTie = Label(self.window, text=" Game Over. IT'S A TIE")

    def radio(self):
        self.button_play['state'] = 'normal'

    def play(self):

        all_choices = ['rock', 'paper', 'scissors']
        win_list = [['paper', 'rock'], ['rock', 'scissors'], ['scissors', 'paper']]

        computer_response = random.choice(all_choices)
        #computer_response = 'rock'
        if computer_response == 'rock':
            self.computer_IMG = Label(self.window, image=self.rock_C)
            self.computer_IMG.place(x=410, y=140)
        elif computer_response == 'paper':
            self.computer_IMG = Label(self.window, image=self.paper_C)
            self.computer_IMG.place(x=410, y=140)
        elif computer_response == 'scissors':
            self.computer_IMG = Label(self.window, image=self.scissors_C)
            self.computer_IMG.place(x=410, y=140)

        player_response = self.radio_1.get().lower().strip()
        if player_response == 'rock':
            self.user_IMG = Label(self.window, image=self.rock)
            self.user_IMG.place(x=50, y=140)
        elif player_response == 'scissors':
            self.user_IMG = Label(self.window, image=self.scissors)
            self.user_IMG.place(x=50, y=140)
        elif player_response == 'paper':
            self.user_IMG = Label(self.window, image=self.paper)
            self.user_IMG.place(x=50, y=140)

        if self.computer_IMG == Label(self.window, image=self.paper):
            computer_response = 'paper'
        elif self.computer_IMG == Label(self.window, image=self.rock):
            computer_response = 'rock'
        elif self.computer_IMG == Label(self.window, image=self.scissors):
            computer_response = 'scissors'

        player = player_response
        computer = computer_response

        while True:

            if player == computer:
                print('This Round is TIE.')

                self.label_youWin.place_forget()
                self.label_computerWin.place_forget()
                self.label_tipCwin.place_forget()
                self.label_tipYwin.place_forget()
                self.label_tipTie.place_forget()

                self.label_tie.place(x=250, y=350)
                GUI.tie_count += 1
                GUI.games_times += 1
                print(GUI.games_times)
                break

            if [player, computer] in win_list:
                print('This Round you WIN.')
                self.label_tipCwin.place_forget()
                self.label_tipYwin.place_forget()
                self.label_tipTie.place_forget()
                self.label_tie.place_forget()
                self.label_computerWin.place_forget()

                self.label_youWin.place(x=250, y=350)
                GUI.player_win += 1
                if GUI.player_win >= 2:
                    self.label_tipYwin.place(x=250, y=350)
                GUI.games_times += 1
                print(GUI.games_times)
                break

            if [computer, player] in win_list:
                print('This Round computer WIN.')
                self.label_tipCwin.place_forget()
                self.label_tipYwin.place_forget()
                self.label_tipTie.place_forget()
                self.label_tie.place_forget()
                self.label_youWin.place_forget()

                self.label_computerWin.place(x=250, y=350)
                GUI.computer_win += 1
                if GUI.computer_win >= 2:
                    self.label_tipCwin.place(x=250, y=350)
                    break
                GUI.games_times += 1
                print(GUI.games_times)
                break

        if GUI.games_times >= 3 or GUI.computer_win >= 2 or GUI.player_win >= 2:
            if GUI.computer_win > GUI.player_win:
                self.label_tipYwin.place_forget()
                self.label_tipTie.place_forget()

                self.label_tie.place_forget()
                self.label_youWin.place_forget()

                self.label_computerWin.place_forget()
                self.label_tipCwin.place(x=250, y=350)
                print('GAME OVER - COMPUTER WINS')
            elif GUI.computer_win < GUI.player_win:
                self.label_tipCwin.place_forget()
                self.label_tipTie.place_forget()

                self.label_tie.place_forget()
                self.label_youWin.place_forget()
                self.label_computerWin.place_forget()

                self.label_tipYwin.place(x=250, y=350)
                print("Game Over. You win.")
            else:
                self.label_tipCwin.place_forget()
                self.label_tipYwin.place_forget()

                self.label_tie.place_forget()
                self.label_youWin.place_forget()

                self.label_computerWin.place_forget()
                self.label_tipTie.place(x=250, y=350)
                print("Game Over. IT'S A TIE")

            self.button_play['state'] = 'disabled'

        self.label_tieCount = Label(self.window, text=f'Tie: {GUI.tie_count}', font='Arial， 15', bg='white')
        self.label_tieCount.place(x=285, y=130)

        self.label_score= Label(self.window, text=str(GUI.player_win) + ':' + str(GUI.computer_win), font='Arial， 35', bg='red')
        self.label_score.place(x=280, y=80)

        self.radio_1.set(NONE)
        self.button_play['state'] = 'disabled'

    def restart(self):
        GUI.computer_win = 0
        GUI.player_win = 0
        GUI.games_times = 0
        GUI.tie_count = 0

        self.button_play['state'] = 'disabled'

        self.user_IMG = Label(self.window, image=self.user)
        self.user_IMG.place(x=50, y=140)

        self.computer_IMG = Label(self.window, image=self.computer)
        self.computer_IMG.place(x=410, y=140)
        self.label_score = Label(self.window, text='0:0', font='Arial， 35', bg='red')
        self.label_score.place(x=280, y=80)
        self.label_tieCount = Label(self.window, text='Tie: 0', font='Arial， 15', bg='white')
        self.label_tieCount.place(x=285, y=130)

        self.radio_1.set(NONE)

        self.label_tipCwin.place_forget()
        self.label_tipYwin.place_forget()
        self.label_tipTie.place_forget()

        self.label_tie.place_forget()
        self.label_youWin.place_forget()
        self.label_computerWin.place_forget()

