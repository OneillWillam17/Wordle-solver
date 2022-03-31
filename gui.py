from tkinter import *


class Gui:

    def __init__(self):
        self.window = Tk()
        self.window.geometry('307x430')  # 307 is width, 430 is height
        self.window.title("Wordle Solver by William O'Neill")
        self.window.config(background='black')

        self.row_0_letter0 = Button(self.window, text=' ', width=7, height=4)
        self.row_0_letter1 = Button(self.window, text=' ', width=7, height=4)
        self.row_0_letter2 = Button(self.window, text=' ', width=7, height=4)
        self.row_0_letter3 = Button(self.window, text=' ', width=7, height=4)
        self.row_0_letter4 = Button(self.window, text=' ', width=7, height=4)
        self.first_row = [self.row_0_letter0, self.row_0_letter1, self.row_0_letter2,
                          self.row_0_letter3, self.row_0_letter4]

        self.row_1_letter0 = Button(self.window, text=' ', width=7, height=4)
        self.row_1_letter1 = Button(self.window, text=' ', width=7, height=4)
        self.row_1_letter2 = Button(self.window, text=' ', width=7, height=4)
        self.row_1_letter3 = Button(self.window, text=' ', width=7, height=4)
        self.row_1_letter4 = Button(self.window, text=' ', width=7, height=4)
        self.second_row = [self.row_1_letter0, self.row_1_letter1, self.row_1_letter2,
                           self.row_1_letter3, self.row_1_letter4]

        self.row_2_letter0 = Button(self.window, text=' ', width=7, height=4)
        self.row_2_letter1 = Button(self.window, text=' ', width=7, height=4)
        self.row_2_letter2 = Button(self.window, text=' ', width=7, height=4)
        self.row_2_letter3 = Button(self.window, text=' ', width=7, height=4)
        self.row_2_letter4 = Button(self.window, text=' ', width=7, height=4)
        self.third_row = [self.row_2_letter0, self.row_2_letter1, self.row_2_letter2,
                          self.row_2_letter3, self.row_2_letter4]

        self.row_3_letter0 = Button(self.window, text=' ', width=7, height=4)
        self.row_3_letter1 = Button(self.window, text=' ', width=7, height=4)
        self.row_3_letter2 = Button(self.window, text=' ', width=7, height=4)
        self.row_3_letter3 = Button(self.window, text=' ', width=7, height=4)
        self.row_3_letter4 = Button(self.window, text=' ', width=7, height=4)
        self.fourth_row = [self.row_3_letter0, self.row_3_letter1, self.row_3_letter2,
                           self.row_3_letter3, self.row_3_letter4]

        self.row_4_letter0 = Button(self.window, text=' ', width=7, height=4)
        self.row_4_letter1 = Button(self.window, text=' ', width=7, height=4)
        self.row_4_letter2 = Button(self.window, text=' ', width=7, height=4)
        self.row_4_letter3 = Button(self.window, text=' ', width=7, height=4)
        self.row_4_letter4 = Button(self.window, text=' ', width=7, height=4)
        self.fifth_row = [self.row_4_letter0, self.row_4_letter1, self.row_4_letter2,
                          self.row_4_letter3, self.row_4_letter4]

        self.row_5_letter0 = Button(self.window, text=' ', width=7, height=4)
        self.row_5_letter1 = Button(self.window, text=' ', width=7, height=4)
        self.row_5_letter2 = Button(self.window, text=' ', width=7, height=4)
        self.row_5_letter3 = Button(self.window, text=' ', width=7, height=4)
        self.row_5_letter4 = Button(self.window, text=' ', width=7, height=4)
        self.sixth_row = [self.row_5_letter0, self.row_5_letter1, self.row_5_letter2,
                          self.row_5_letter3, self.row_5_letter4]

        self.rows = [self.first_row, self.second_row, self.third_row, self.fourth_row, self.fifth_row, self.sixth_row]

        # we use a dictionary to keep track of which button is currently on which color
        # dict is organized by row first, then variable within that row : color currently on that button
        # SystemButtonFace is the default color for tkinter buttons
        self.button_color = {
            0: {
                self.row_0_letter0: 'SystemButtonFace',
                self.row_0_letter1: 'SystemButtonFace',
                self.row_0_letter2: 'SystemButtonFace',
                self.row_0_letter3: 'SystemButtonFace',
                self.row_0_letter4: 'SystemButtonFace',
            },
            1: {
                self.row_1_letter0: 'SystemButtonFace',
                self.row_1_letter1: 'SystemButtonFace',
                self.row_1_letter2: 'SystemButtonFace',
                self.row_1_letter3: 'SystemButtonFace',
                self.row_1_letter4: 'SystemButtonFace',
            },
            2: {
                self.row_2_letter0: 'SystemButtonFace',
                self.row_2_letter1: 'SystemButtonFace',
                self.row_2_letter2: 'SystemButtonFace',
                self.row_2_letter3: 'SystemButtonFace',
                self.row_2_letter4: 'SystemButtonFace',
            },
            3: {
                self.row_3_letter0: 'SystemButtonFace',
                self.row_3_letter1: 'SystemButtonFace',
                self.row_3_letter2: 'SystemButtonFace',
                self.row_3_letter3: 'SystemButtonFace',
                self.row_3_letter4: 'SystemButtonFace',
            },
            4: {
                self.row_4_letter0: 'SystemButtonFace',
                self.row_4_letter1: 'SystemButtonFace',
                self.row_4_letter2: 'SystemButtonFace',
                self.row_4_letter3: 'SystemButtonFace',
                self.row_4_letter4: 'SystemButtonFace',
            },
            5: {
                self.row_5_letter0: 'SystemButtonFace',
                self.row_5_letter1: 'SystemButtonFace',
                self.row_5_letter2: 'SystemButtonFace',
                self.row_5_letter3: 'SystemButtonFace',
                self.row_5_letter4: 'SystemButtonFace',
            }
        }

        # place buttons on UI, maintain position in list by using the index location as the same column
        for row in self.rows:
            for index, buttons in enumerate(row):
                buttons.grid(row=self.rows.index(row), column=index, padx=1)
        # adds mouse button binding for all buttons to allow them to change colors
        for row in self.rows:
            for btn in row:
                self.bind_button(button=btn, row=self.rows.index(row))

    def bind_button(self, button, row):
        """Binds the single and double click inputs to changing the button colors between yellow and green"""
        print(f"Binding button: {button}")
        button.bind('<Button-1>', lambda x: self.change_color(event=x, button=button, row=row))

    def change_color(self, event, button, row):
        """Rotates button color through white, yellow, green to mark buttons"""
        print(button.info)
        print(row)

        if button['background'] == 'SystemButtonFace':
            button['background'] = 'yellow'
            self.button_color[row][button] = 'yellow'
            print(f"self.button_color: {self.button_color[row][button]}")

        elif button['background'] == 'yellow':
            button['background'] = 'green'
            self.button_color[row][button] = 'green'
            print(f"self.button_color: {self.button_color[row][button]}")

        elif button['background'] == 'yellow' or button['background'] == 'green':
            button['background'] = 'SystemButtonFace'
            self.button_color[row][button] = 'SystemButtonFace'
            print(f"self.button_color: {self.button_color[row][button]}")

        print(f"Color Change: {button['background']}")

    def update_buttons(self, word, row):
        """Adds the latest guess from brain.py to buttons based on index"""
        for index, btn in enumerate(self.rows[row]):
            btn.config(text=word[index])

    def return_green_dict(self, row) -> dict:
        """Read over the button color dictionary and return which letters were selected as green from the list"""
        green_letter_dict = {
            0: False,
            1: False,
            2: False,
            3: False,
            4: False,
        }
        for index, color in enumerate(self.button_color[row].values()):
            # check if there is a green letter present at that location
            # print(f'entire green dict: {self.button_color[row]}')
            # print(f'index green button: {index}')
            # print(f"green button color: {color}")
            if color == 'green':
                green_letter_dict[index] = True
            else:
                pass

        return green_letter_dict

    def return_yellow_dict(self, row) -> dict:
        """Returns a dict that contains 0-4 : and True/False to mark if there is a yellow letter
         at the corresponding location"""
        yellow_letter_dict = {
            0: False,
            1: False,
            2: False,
            3: False,
            4: False,
        }
        for index, color in enumerate(self.button_color[row].values()):
            # Check for 'yellow' in button color dictionary
            print(f"yellow button color: {color}")
            if color == 'yellow':
                yellow_letter_dict[index] = True
            else:
                pass

            return yellow_letter_dict

    def disable_buttons(self, row):
        """Disables buttons by row to prevent changing them after next word appears"""
        for button in self.rows[row]:
            button.unbind('<Button-1>')

    def run(self):
        """Calls the mainloop function from tkinter to run UI"""
        self.window.mainloop()

