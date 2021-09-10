/*
Bagels, a deductive logic game.

I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say:
    * Pico -> One digit is correct but in the wrong position.
    * Fermi -> One digit is correct and in the right position.
    * Bagels -> No digit is correct.

I have thought up a number.
You have 10 guesses to get it.
*/
#include <iostream>
#include <cstdlib>
#include <time.h>


const bool ask(const std::string msg){
  while (true){
    std::cout << msg << " [y/n]: ";
    std::string input;
    std::cin >> input;

    if (input == "y"){
      return true;
    }
    else if (input == "n"){
      return false;
    }
    else{
      std::cout << "Input was invalid\n";
      continue;
    }
  }
}


int randint(int min, int max) {
  return min + ( std::rand() % max );
}


int main(){
  std::cout << "Hello World!\n";
  std::cout << randint(1, 100);
  return 0;
}
