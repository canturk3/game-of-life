# game-of-life
Basic implementation of game of life in Python with pygame

A JavaScript version using HTML Canvas is also provided in `index.html` and `game-of-life.js`. Open `index.html` in a browser to try it out.

-----
**Rules:**
* Any live cell with 0 or 1 live neighbors becomes dead, because of underpopulation
* Any live cell with 2 or 3 live neighbors stays alive, because its neighborhood is just right
* Any live cell with more than 3 live neighbors becomes dead, because of overpopulation
* Any dead cell with exactly 3 live neighbors becomes alive, by reproduction
