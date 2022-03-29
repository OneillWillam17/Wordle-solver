# wordle-solver
First iteration at an automated wordle solver, This is a BETA version but i'm looking forward to revamping it and making it cleaner and more efficient!

# main.py
For now just calls the methods from brain.py, in a later update will be used for a UI or a self sustaining version of the program (aka picking its own word at random and solving for it without user input) 

# brain.py
Main processing goes on in this file. Interesting note; it uses a dictionary to store 'green' characters to keep track of the character's position within the word itself. Includes multiple method's that are used to write remaining words to a new text file, save which letters are potentially in the word, remove words that dont fit criteria, and return a 'guess' from the remaining words.

# text files
wordle-nyt-answers is what the name suggests, its a list of the 'potential' answers for the wordle game, remaining wordlist.txt gets written to during several of the brain.py methods, it gets updated by removing words that aren't a possible solution. Mainly for testing purposes to check what the computer can choose from. 
