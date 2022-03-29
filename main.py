from brain import Solver

# Read the list of potential words from text file, and setup lists for green/yellow letters
wordle = Solver()

# Guess's word and saves potential solutions to textfile
# loop repeats 5 times for the 5 free guesses within the game
# after loop ends (meaning word has not been solved and game is on its last guess) guess one final time
# only looping 5 times because after program saves data from 5th guess; no benefit to saving new data from 6th guess
# as the game would end regardless of whether word was correct or not
for _ in range(5):
    # write all potential solutions to a text file for debugging / testing purposes
    wordle.save_wordlist()

    # prints random word from list of potential solutions
    print(f"Guess: {wordle.guess_word()}")

    # asks for user input of which characters are green/yellow and saves those characters to a list/dict
    # filters remaining words based on those letters
    wordle.save_letters()

# final guess of game, outside loop as no reason to save data after called
print(f"Final Guess: {wordle.guess_word()}")

# todo potential double letters issues, index always chooses closes to front
# todo possible fix in ui ^ able to choose where letters go?
