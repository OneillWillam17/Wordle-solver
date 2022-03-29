from brain import Solver

wordle = Solver()

for i in range(5):
    wordle.save_wordlist()

    print(f"Guess: {wordle.guess_word()}")

    wordle.save_letters()


# final guess
print(f"Final Guess: {wordle.guess_word()}")



# # todo wiser - all wrong, next word was wharf. Removed letters list??
# # todo f, u, n, potential word, next suggest word was fishy
# # todo potential word list clears after each guess
# # todo double letters issues
# # todo duplicates in potential word
# # todo if y to correct letters, but not correct letter itself - reomve