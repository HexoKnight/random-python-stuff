# random-python-stuff
all from my repl.it

## note
some of these use getch, which isn't supported on windows, so on windows you must replace `from getch import getch` with `from msvcrt import getch` (usually near the start of the file)

## [0s-and-Xs](0s-and-Xs) - Mar 5, 2021
a few implementations of naughts and crosses, including a one-liner and one with ai using the minimax algorithm with alpha-beta pruning

## [1-line-while](1-line-while) - Mar 26, 2021
I was obsessed with trying to code golf my python programs into one-liners and this was a common situation that I had to re-figure out every time so a made a dedicated repl for it

## [Console-Stuffs](Console-Stuffs) - Nov 7, 2020
has some useful ANSI code things for interacting with the cursor and changing colours

## [Encryption](Encryption) - Dec 2, 2020
an implementation of Shamir's secret sharing (my fav ecryption sorta thing) that I later rewrote in c#, which can be found [here](https://github.com/HexoKnight/Encryption)

## [Fractal-Thing](Fractal-Thing) - Dec 16, 2020
essentially just a demonstation of [this](https://en.wikipedia.org/wiki/Chaos_game)

## [Guesthouse-problem](Guesthouse-problem) - Sep 30, 2020
'a guesthouse wants electronic/keycode locks on rooms doors that guests can use to access their rooms only for the duration of their stay, but their locks will be tamper proof so can only accept input via the RFID/keypad.'
I implemented a solution involving the locks being preprogrammed with some seed values to be able to psuedo randomly generate numbers and if the next number is entered the lock replaces the current number with the new number and generates another.

## [Maybe-3D](Maybe-3D) - Dec 11, 2020
it is in fact 3D :) (despite some performance and console outputting issues)

## [Test-Ul](Test-Ul) - Oct 15, 2020
some nice selection related functions

## [Tools](Tools) - Nov 7, 2020
some useful functions (including the early stages of [Test-Ul](#Test-UI))
