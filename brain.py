from random import choice


class Solver:

    def __init__(self):

        # format word list
        with open('wordle-nyt-answers-alphabetical.txt') as file:
            self.wordlist = [line.strip('\n') for line in file]

        # green letters is a dict to allow us to save index and value
        self.green_letters = {
            0: None,
            1: None,
            2: None,
            3: None,
            4: None,
        }
        self.yellow_letters = []
        self.wrong_letters = []

        # stores any words already guessed by program
        self.already_guessed = []

        # used in self.guess_word() to display any potential words the letters may show
        self.potential_word = []

        # latest guess from self.guess_word()
        self.guess = None

    def save_letters(self):
        """For use in the manual version of this program, prompts the user to enter which letters from the guess are
        'green' (green letter means it is the correct letter AND its in the correct location in the word"""
        # before saving new letters remove old ones from list
        self.clear_letters()

        correct_letters = input("Were there any correct letters, Y or N: ").lower()

        if correct_letters == 'n':
            # all letters in the guess were incorrect, meaning they cannot be in the correct word
            for char in self.guess:
                self.wrong_letters.append(char)
        else:
            # Green letters
            green_input = input('Enter green letters:, leave blank if none: ').lower()

            # if all character are green, meaning we found word and win game
            if green_input == self.guess:
                print("Yay we got it!")

            for char in self.guess:

                if char in green_input:
                    # character is in both user input and the programs guess
                    # means the character is confirmed in the correct spot within the guess
                    index = self.guess.index(char)
                    self.green_letters[index] = char

            # Yellow letters
            yellow_input = input('Enter yellow letters: leave blank if none: ').lower()

            for char in yellow_input:
                # these letters are confirmed in the word, but not in a guaranteed spot.
                self.yellow_letters.append(char)

            # add letters from guess but not yellow to wrong_letters
            for letter in self.guess:
                if letter not in yellow_input and letter not in green_input:
                    self.wrong_letters.append(letter)
                    print(f"self.wrong_letter added: {letter}")

            # add self.guess to list, so we don't guess same word twice
            self.already_guessed.append(self.guess)

    def guess_word(self):
        """Returns a word based on any green letters or yellow letters saved, if neither (ie first guess) returns
        a word from the list at random"""

        for char in self.green_letters.values():

            # print(f"self.green_letters char: {char}")

            if char is None:
                pass  # We don't know the corresponding character for this location

            else:
                self.potential_word += char

        if len(self.yellow_letters) > 0:
            # we know some letters but not their locations within the word

            for char in self.yellow_letters:
                self.potential_word += char

        # remove duplicates in potential_word
        self.potential_word = list(set(self.potential_word))

        print(f"Potential_word: {self.potential_word}")

        # removes incorrect words from list
        self.update_wordlist()

        # saves possible solutions to txt file, mainly testing purposes
        self.save_wordlist()

        # picks a word at random from remaining words
        self.guess = choice(self.wordlist)

        # prints the dict, helpful to see which green letter is located where
        print(f"Green letter dict: {self.green_letters}")

        return self.guess

    def update_wordlist(self):
        """iterates through self.wordlist removes any words that don't contain letters in
        self.yellow_letters and self.green_letters. Also removes words that contain letters from self.wrong_letters"""

        # using copy of list to not mess up indexing while removing things from list
        for word in self.wordlist[:]:

            # remove any words we have already guessed previously
            for used_word in self.already_guessed[:]:
                print(f'used_word: {used_word}')

                # so the program doesn't try to remove the word several times per loop
                print(f"Removing word: {word}, reason: self.already_guessed")
                self.already_guessed.remove(used_word)

                self.wordlist.remove(used_word)

            for char in self.wrong_letters:

                if char in word:  # word contains a letter we know isn't in the solution, remove word from list

                    try:
                        self.wordlist.remove(word)
                        print(f"Removing word: {word}, reason: self.wrong_letters")
                    except ValueError:
                        pass

            # yellow letters
            for char in self.yellow_letters:

                if char not in word:

                    # we remove these words since they don't contain a letter we have already confirmed in the word
                    try:
                        self.wordlist.remove(word)
                        print(f"Removing word: {word}, reason: self.yellow_letters")
                    except ValueError:  # word may have already been removed from either loop above
                        pass

            # green letters
            for key, char in self.green_letters.items():

                # checks characters within green_letter dict to see if they are assigned (aka not none)
                if char is not None:
                    # means there is a character stored in the dict

                    if char not in word:
                        # we remove these words since they don't contain a letter we have already confirmed in the word
                        try:
                            self.wordlist.remove(word)
                            print(f"Removing word: {word}, reason: self.green_letters.items()")
                        except ValueError:  # word may have already been removed from either loop above
                            pass

                    for letter in word:

                        if word[key] != char:  # The word contains the letter but in the wrong location

                            try:
                                self.wordlist.remove(word)
                                print(f"Removing word: {word}, reason: word[key] != char")

                            except ValueError:
                                pass
                        else:
                            pass  # word contains both the character, and in the correct location

    def clear_letters(self):
        """Resets the green and yellow letter lists, called before saving new guess"""

        self.green_letters = {
            0: None,
            1: None,
            2: None,
            3: None,
            4: None,
        }

        self.yellow_letters = []

    def save_wordlist(self):
        """for testing. saves all remaining words to new text file"""
        with open('Remaining Wordlist.txt', 'w') as file:
            file.writelines(f"{self.wordlist}\n")
