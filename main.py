from brain import Solver
from gui import Gui
from itertools import count

# Read the list of potential words from text file, and setup lists for green/yellow letters
wordle = Solver()
gui = Gui()

count = (count(start=0, step=1))


def count_row(_count):
    """Simple counter from itertools, used in the get_new_word function to keep track of which row the user is on"""
    return next(_count)


def get_new_word(event):
    """This function does the main brunt of the work regarding interaction between the UI and the backend"""
    # keeps track of which row the UI is on, allows the other functions to modify the correct set of buttons/words etc
    row = count_row(count)

    # passes the return green and yellow dict functions to a different function that filters the remaining words
    # based of if they contained/didn't contain the correct letters.
    wordle.get_gui_letters(
        green=gui.return_green_dict(row - 1),
        yellow=gui.return_yellow_dict(row - 1),
    )

    word = wordle.guess_word()
    print(f'Guess: {word}')

    # disables the previous row's buttons so user cannot change them after next word appears
    gui.disable_buttons(row - 1)

    # write all potential solutions to a text file for debugging / testing purposes
    wordle.save_wordlist()

    # writes the latest guess to the next row of buttons on the GUI
    gui.update_buttons(word=word, row=row)


# binds the above function to whenever the user presses enter
# on press, it filters remain words by whatever the user marked as yellow or green
# and then generates the next word and fills it
gui.window.bind('<KeyPress-Return>', get_new_word)

# add first word to UI before we launch app
gui.update_buttons(word=wordle.guess_word(), row=count_row(_count=count))

# calls the mainloop function (effectively starts the UI)
gui.run()
