# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

import random
import string

class Game:
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        #self.grid = ['O','Q','U','W','R','B','A','Z','E']
        self.grid = [random.choice(string.ascii_uppercase) for _ in range(9)]

        #self.grid = []
        #for _ in range(9):
        #    self.grid.append(random.choice(string.ascii_uppercase))

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        '''
        (wrong)
        grid_copy = self.grid.copy()  # Create a copy of the grid to track used letters
        for letter in word:
            if letter in grid_copy:
                grid_copy.remove(letter)
            else:
                return False  # Letter is not available in the grid
        return True  # All letters in the word are valid and present in the grid
        '''
        if not word:
            return False
        letters = self.grid.copy() # Consume letters from the grid
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
        return True

if __name__ == "__main__":
    game = Game()
    print(game.grid) # --> OQUWRBAZE
    my_word = "BAROQUE"
    print(game.is_valid(my_word)) # --> True
    '''
    new_game = Game()
    new_game.grid = list('KWIENFUQW')
    print(new_game.is_valid('FEUN'))
    # => true
    '''
