# wordle-solver
First iteration at an automated wordle solver, This is a BETA version but i'm looking forward to revamping it and making it cleaner and more efficient!

# main.py
For now just calls the methods from brain.py, in a later update will be used for a UI or a self sustaining version of the program (aka picking its own word at random and solving for it without user input) 

# brain.py
Main processing goes on in this file. Interesting note; it uses a dictionary to store 'green' characters to keep track of the character's position within the word itself. Includes multiple method's that are used to write remaining words to a new text file, save which letters are potentially in the word, remove words that dont fit criteria, and return a 'guess' from the remaining words.

# gui.py
A simple user interface made with tkinter, consists mainly of buttons that change their background and can be accessed later on to determine which letters are green / yellow. Those are then converted to dictionaries which store both the location of the letter (the index) and whether or something was located there (by using a bool). The boolean dictionaries are then passed into a function in brain.py that checks what letter it is based on the key/index, completly solving the issue of using index to search while have double letters in the solution.

# text files
wordle-nyt-answers is what the name suggests, its a list of the 'potential' answers for the wordle game, remaining wordlist.txt gets written to during several of the brain.py methods, it gets updated by removing words that aren't a possible solution. Mainly for testing purposes to check what the computer can choose from. 

# issues i've come across while making this project
Outside of the normal few typo and logic issues there's been a few interesting problems that I have had to deal with making this project so far. The one I most recently solved was an issue which caused words that contained a 'yellow' letter in a specific spot (ie the first letter in the word) to continue trying words with that same letter in the same spot. I solved this by creating a new dictionary that contained a list for each of the indexes of a guessed word. In short, if a letter is guessed and found to be within the word, but not at that location. It gets added to the list inside that dictionary. Which then removes any words that consist of that letter in that location.
