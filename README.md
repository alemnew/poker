# poker

A simplified version of [poker](https://en.wikipedia.org/wiki/Poker) game. Given two poker hands determine which one wins. The program assumes that the cards don't have suits and there are no flushes, straights, and straight flushes. A hand wins if it has a more valuable combination than the other or if they have the same combination but the cards of one are higher than the cards of the other.

# Code structure 

- [poker.py](poker.py) contains the main program of the poker game. 
- [lib_poker.py](lib_poker.py) contains supporting utility functions for the poker game. 
- [test_poker.py](test_poker.py) contains test cases for the poker game. 

# How run it? 
The program is developed for python version 3.  If your system does not have python3 installed, please install it from [python3](https://www.python.org/downloads/). 
To run the poker game follow these stepts:
1. Clone the code to your machine
    - `git clone https://gitlab.com/alemnew/poker.git`
2. Change your working directory to the folder "poker".
3. Run it using 
    - `./poker.py {hand_1} {hand_2}` where `hand_1` and `hand_2` contain a string of five characters, where each character is one of `23456789TJQKA`. 
4. Output
    - Unpon a sucessful execution of the program, it answers `First hand wins!`, `Second hand wins!` or `It's a tie!`. If the user inputs illegal set of cards, that is, any character other that `23456789TJQKA`, the program prints error message and stops execution. 
5. Examples: 
    - `./poker.py AAAQQ QQQAA` answers `First hand wins!`
    - `./poker.py QQQAA AAAQQ` answers `Second hand wins!`
    - `./poker.py AAAQQ QQAAA` answers `It's a tie!`

    

