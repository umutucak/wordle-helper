# Wordle Assist Script
My first five guesses on the January 14th, 2026 [Wordle](https://www.nytimes.com/games/wordle/index.html) were horrendous, so I wrote a script to narrow down the 6th guess. It was 50/50, I chose wrong, but my hatred is quenched.
## Dependencies
- It uses the [pyenchant](https://pypi.org/project/pyenchant/) `pip` package to check if the words its generating are real words before outputting them.
- Depending on your OS you also need to [download the actual Enchant library](https://pyenchant.github.io/pyenchant/install.html#installing-the-enchant-c-library). On Ubuntu you can `sudo apt install libenchant-2-dev`.
## Usage
You can give your progress by entering the **_greens, yellows, and grays_** you found, and where you found them:
- `a3 b2` if you have a green `a` on the 3rd slot, and a green `b` on the 2nd slot.
- `b1 b2 j3` if you have yellow `b`s in the 1st and 2nd, and a `j` in the 3rd slot.
- `a b c` if you have grayed out `a`, `b`, and `c`.
- All inputs are optional, can be given empty inputs (just press Enter).
## Output
It will eliminate all words in the American English dictionary that do not pass these feedbacks, and give a list of possible words:
```
$ python3 wordle_helper.py
Give your greens like this: 'a2 b4' for 'a' in the 2nd and 'b' in the 4th slot:
Give your yellows like this: 'c1 c2 d3' for 'c' not in the 1st or 2nd, and 'd' not in the 3rd slot: a4 i3 d1 a2 o2 i2 a3
Give your grays like this: `a b c` if these letters are gray: e r y p s j k l c n m
['audio', 'avoid']
```
