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
        self.correct_letter_wrong_location = {
            0: None,
            1: None,
            2: None,
            3: None,
            4: None,
        }
        self.wrong_letters = []
        self.already_guessed_words = []
        self.confirmed_letters = []
        self.latest_guess = None

    def manually_input_letters(self):
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
                # these letters are confirmed in the word, but not in the spot that was tried.
                index = self.latest_guess.index(char)
                if self.correct_letter_wrong_location[index] is None:
                    # replaces None with list, so we can keep track of which guesses cannot go in which location
                    self.correct_letter_wrong_location[index] = []
                self.correct_letter_wrong_location[index] += char

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
            if char is not None:
                self.confirmed_letters += char

        for list_ in self.correct_letter_wrong_location.values():
            # contains a list which holds letters that are correct but not at that index
            if list_ is not None:
                for char in list_:
                    self.confirmed_letters += char

        self.confirmed_letters = list(set(self.confirmed_letters))  # remove duplicates within confirmed_letters
        self.update_wordlist()                                      # removes incorrect words from list
        self.save_wordlist()                                        # saves possible solutions to txt file
        self.latest_guess = choice(self.wordlist)                   # picks a word at random from remaining words

        print(f"Green letter dict: {self.correct_location_and_letters}")
        print(f"Yellow letter dict: {self.correct_letter_wrong_location}")
        print(f"Confirmed_letters: {self.confirmed_letters}")       # displays list of characters found within word

        return self.latest_guess.upper()

    def get_gui_letters(self, green: dict, yellow: dict):
        """Gets green letter and yellow letter dictionary from GUI, adds corresponding letters to
        correct_location_and_letters and correct_letter_wrong_location"""
        # Hold letters that may be incorrect, but still have not been run through the dict
        possible_wrong_letters = []

        print(f"Green dict from gui: {green}")
        print(f"Yellow dict from gui: {yellow}")

        # check if any of the values in the green or yellow dictionary are True
        # if so then there is a letter at that location that we need to add to its respective dict
        for key, boolean in enumerate(green.values()):
            if boolean is True:
                # means there is a green letter at that key's location
                letter = self.latest_guess[key]
                print(f"key/bool green letter: {letter}")
                self.correct_location_and_letters[key] = letter
            else:
                # letter at this location is not a green letter
                letter = self.latest_guess[key]
                possible_wrong_letters += letter

        for key, boolean in enumerate(yellow.values()):
            if boolean is True:
                # means there is a yellow character at that key's location
                letter = self.latest_guess[key]
                print(f"key/bool yellow letter: {letter}")
                self.correct_letter_wrong_location[key] += letter
            else:
                # letter at this location is not a yellow letter
                letter = self.latest_guess[key]
                possible_wrong_letters += letter

        # go through the characters and check if either of them are in the either of the two dictionaries.
        for char in possible_wrong_letters[:]:
            if char in self.correct_location_and_letters.values() or char in self.correct_letter_wrong_location.values():
                # The letter is already known to be in the word
                # we need to remove the character from possible wrong letters
                possible_wrong_letters.remove(char)

        print(f"Possible_wrong_letters: {possible_wrong_letters}")

        # now that all letters are filtered
        # add remaining letters to wrong_letters
        for char in possible_wrong_letters:
            self.wrong_letters += char

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

            for key, list_ in self.correct_letter_wrong_location.items():
                # list contains correct letters but not located at that key's location
                if list_ is not None:
                    for char in list_:
                        if char not in word:
                            print(f"Removing word: {word}, reason: self.yellow_letters; not in word")

                    for _ in word:
                        for char in list_:
                            if word[key] == char:
                                # contains letter at location we already know cannot be there
                                self.try_remove_word(word)
                                print(f"Removing word: {word}, reason: self.yellow_letters; word[key] == char")

            # backup check for above statement, words not containing yellow letters were still in wordlist
            for char in self.confirmed_letters:
                if char not in word:
                    self.try_remove_word(word)
                    print(f"Removing word: {word}, Reason: Backup check for confirmed letters")

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
                            # print(f"Removing word: {word}, reason: self.green_letters; word[key] != char")
                            self.try_remove_word(word)
                        else:
                            # word contains both the character, and in the correct location
                            pass

    def clear_letters(self):
        """Resets the green letter lists, called before saving new guess"""
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
