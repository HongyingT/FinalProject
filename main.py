from GUI import *


def main():

    window = Tk()
    window.title('Final Project')
    window.geometry('630x600')
    window.resizable(False, False)

    widgets = GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()
