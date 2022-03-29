from random import choice


class Solver:

    def __init__(self):
        # format word list
        with open('wordle-nyt-answers-alphabetical.txt') as file:
            self.wordlist = [line.strip('\n') for line in file]

        self.correct_location_and_letters = {
            0: None,
            1: None,
            2: None,
            3: None,
            4: None,
        }
        self.yellow_letters = []
        self.wrong_letters = []
        self.already_guessed_words = []
        self.confirmed_letters = []
        self.latest_guess = None

    def save_letters(self):
        """For use in the manual version of this program, prompts the user to enter which letters from the guess are
        'green' (green letter means it is the correct letter AND its in the correct location in the word) or yellow
        (meaning correct letter but wrong location)
        """
        # remove letters from previous guess
        self.clear_letters()

        correct_letters = input("Were there any correct letters, Y or N: ").lower()
        if correct_letters == 'n':
            # all letters in the guess were incorrect, meaning they cannot be in the correct word
            for char in self.latest_guess:
                self.wrong_letters.append(char)
        else:
            # Correct letters in the correct location
            green_input = input('Enter green letters:, leave blank if none: ').lower()

            # if all letters are green, we found word and win game
            if green_input == self.latest_guess:
                print("Word solved!")

            for char in self.latest_guess:
                if char in green_input:
                    # character is in both user input and the programs guess
                    # means the character is confirmed in the correct spot within the guess
                    index = self.latest_guess.index(char)  # todo issue here for double letters
                    self.correct_location_and_letters[index] = char

            # Yellow letters
            yellow_input = input('Enter yellow letters: leave blank if none: ').lower()
            for char in yellow_input:
                # these letters are confirmed in the word, but not in a guaranteed spot.
                self.yellow_letters.append(char)

            # letters in self.guess that weren't added to yellow/green list; word cannot contain letter
            for letter in self.latest_guess:
                if letter not in yellow_input and letter not in green_input:
                    self.wrong_letters.append(letter)
                    print(f"self.wrong_letter added: {letter}")

            self.already_guessed_words.append(self.latest_guess)

    def guess_word(self):
        """Returns a word based on any green letters or yellow letters saved, if neither (ie first guess) returns
        a word from the list at random"""
        for char in self.correct_location_and_letters.values():  # we know letters AND their location within the word
            if char is None:
                pass                                       # We don't know the corresponding character for this location
            else:
                self.confirmed_letters += char
        if len(self.yellow_letters) > 0:                  # we know some letters but not their locations within the word
            for char in self.yellow_letters:
                self.confirmed_letters += char

        self.confirmed_letters = list(set(self.confirmed_letters))  # remove duplicates within confirmed_letters
        self.update_wordlist()                                      # removes incorrect words from list
        self.save_wordlist()                                        # saves possible solutions to txt file
        self.latest_guess = choice(self.wordlist)                   # picks a word at random from remaining words

        print(f"Green letter dict: {self.correct_location_and_letters}")
        print(f"Confirmed_letters: {self.confirmed_letters}")       # displays list of characters found within word

        return self.latest_guess

    def update_wordlist(self):
        """iterates through self.wordlist removes any words that don't contain letters in
        self.yellow_letters and self.green_letters. Also removes words that contain letters from self.wrong_letters"""

        # using copy of list to not mess up indexing while removing things from list
        for word in self.wordlist[:]:
            # remove any words we have already guessed previously
            for used_word in self.already_guessed_words[:]:
                print(f'used_word: {used_word}')
                print(f"Removing word: {word}, reason: self.already_guessed")
                # so the program doesn't attempt to remove the word several times per loop
                self.already_guessed_words.remove(used_word)
                self.wordlist.remove(used_word)

            # if word contains a letter we know isn't in the solution, remove word from list
            for char in self.wrong_letters:
                if char in word:
                    print(f"Removing word: {word}, reason: self.wrong_letters")
                    self.try_remove_word(word)

            # remove these words since they don't contain a letter we already know is in the word
            for char in self.yellow_letters:
                if char not in word:
                    print(f"Removing word: {word}, reason: self.yellow_letters")
                    self.try_remove_word(word)

            for key, char in self.correct_location_and_letters.items():
                # checks characters within correct loc and letter dict to see if they are assigned (aka not None)
                if char is not None:
                    if char not in word:
                        # remove these words since they don't contain a letter we have already confirmed in the word
                        print(f"Removing word: {word}, reason: self.green_letters.items()")
                        self.try_remove_word(word)

                    for _ in word:
                        if word[key] != char:
                            # The word contains the letter but in the wrong location
                            print(f"Removing word: {word}, reason: word[key] != char")
                            self.try_remove_word(word)
                        else:
                            # word contains both the character, and in the correct location
                            pass

    def clear_letters(self):
        """Resets the green and yellow letter lists, called before saving new guess"""
        self.yellow_letters = []
        self.correct_location_and_letters = {
            0: None,
            1: None,
            2: None,
            3: None,
            4: None,
        }

    def save_wordlist(self):
        """for testing. saves all remaining words to new text file"""
        with open('Remaining Wordlist.txt', 'w') as file:
            file.writelines(f"{self.wordlist}\n")

    def try_remove_word(self, word):
        """Simple method that removes a word from the wordlist while also ignoring any ValueError that may occur;
        ValueError was caused due to method trying to remove word that was no longer in the wordlist"""
        try:
            self.wordlist.remove(word)
        except ValueError:
            pass
