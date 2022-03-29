from brain import Solver

wordle = Solver()

for i in range(5):
    wordle.save_wordlist()

    print(f"Guess: {wordle.guess_word()}")

    wordle.save_letters()

# final guess
print(f"Final Guess: {wordle.guess_word()}")

# todo potential double letters issues, index always chooses closes to front
# todo possible fix in ui ^ able to choose where letters go?
