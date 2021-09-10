"""
Bagels, a deductive logic game.

I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say:
    * Pico -> One digit is correct but in the wrong position.
    * Fermi -> One digit is correct and in the right position.
    * Bagels -> No digit is correct.

I have thought up a number.
You have 10 guesses to get it.
"""
from __future__ import annotations
import random


def ask(msg: str) -> bool:
    while True:
        answer = input(msg)
        if answer == 'y':
            return True
        elif answer == 'n':
            return False
        else:
            continue


class Bagels(object):

    _tries_count: int

    def __init__(self) -> None:
        self._tries_count = 10


    @staticmethod
    def get_secret_number() -> int: return random.randint(100, 1000)

    @staticmethod
    def get_valid_guess_input(msg: str) -> str:
        while True:

            guess = input(msg)

            try:
                int_guess = int(guess)
            except ValueError:
                print("Input is not valid")
                continue

            len_guess = len(guess)

            if len_guess != 3 or guess[0] == "0":
                print("Input is not valid")
                continue

            return guess


    def start(self) -> None:
        print(__doc__)

        while True:
            current_tries_count = self._tries_count
            secret = str(self.get_secret_number())
            is_running = True
            while is_running:

                if current_tries_count <= 0:
                    print("You loss!")
                    is_running = False
                    continue

                guess = self.get_valid_guess_input(f"Guess [{self._tries_count - current_tries_count + 1} / {self._tries_count}]: ")

                if guess == secret:
                    print("You got it!")
                    is_running = False
                elif any([n in secret for n in guess]):
                    response = ""
                    for i, n in enumerate(guess):
                        if n in secret:
                            if n == secret[i]:
                                response += "Fermi "
                            else:
                                response += "Pico "
                    print(response)
                else:
                    print("Bagels")

                current_tries_count -= 1

            if not ask("Do you wanna try again? [y/n]: "):
                break


def main() -> None:
    b = Bagels()
    b.start()


if __name__ == '__main__':
    main()
