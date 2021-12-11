# :christmas_tree: :snake: :sparkles: Maja's Advent of Code 2021 :sparkles: :snake: :christmas_tree:

Ho, ho, ho, welcome to my 2021 Advent of Code repository!
This year, my goals are:

1. complete first 10 puzzles :white_check_mark:
2. collect at least 25 stars

My AoC repositories: [2015](https://github.com/mimikrija/AdventOfCode2015), [2016](https://github.com/mimikrija/AdventOfCode2016), [2017](https://github.com/mimikrija/AdventOfCode2017), [2018](https://github.com/mimikrija/AdventOfCode2018), [2019](https://github.com/mimikrija/AdventOfCode2019), [2020](https://github.com/mimikrija/AdventOfCode2020)

## What I learned, what I still don't know

Legend:

:ambulance: - I don't fully understand either the logic or the implementation - HALP!

:hourglass_flowing_sand: - I think this could or should run faster, but I don't know how to optimize it!

:hammer: - Not completely satisfied with solution, but I know how (and plan to) fix it.

Puzzle | Solution(s) | Remarks |
---    |---    |----
[Day 1: Sonar Sweep](https://adventofcode.com/2021/day/1) | [Python](python/01.py) | Here's a [very cringey video](https://youtu.be/-MHDfcas4zo) (in Croatian) of my 6AM thought/solution process. Afterwards I [refactored](https://youtu.be/kGzPefiVyAU) it.. |
[Day 2: Dive!](https://adventofcode.com/2021/day/2) | [Python](python/02.py) | [initial solution video](https://youtu.be/nUwS8rRacR4) |
[Day 3: Binary Diagnostic](https://adventofcode.com/2021/day/3) | [Python](python/03.py) | [part 1 solution video](https://youtu.be/gUCD1leNNE8) - part 2 got me so tired that I didn't record it |
[Day 4: Giant Squid](https://adventofcode.com/2021/day/4) | [Python](python/04.py) | I LOVED THIS PUZZLE. Unfortunately no video because I was not very talkative this morning but I recorded a [walk-through](https://youtu.be/ylToOHi-eLE) later. WELCOME GIANT SQUID!! |
[Day 5: Hydrothermal Venture](https://adventofcode.com/2021/day/5) | [Python](python/05.py) | :hammer: TO DO create some sort of custom `range` which can go backwards depending on input into `santas_little_helpers`. It took me a WHILE to figure out why I was not getting all the diagonals... |
[Day 6: Lanternfish](https://adventofcode.com/2021/day/6) | [Python](python/06.py) | I knew part two was going to be unsolvable with part 1 approach but I did it anyway. Took me a while to figure out that we only need to keep track of how many fish have the same status. |
[Day 7: The Treachery of Whales](https://adventofcode.com/2021/day/7) | [Python](python/07.py) | In the first go I went through all positions in the range, but then realized that we could find candidates for best positions by using the most common position for part 1 and the midpoint for part 2.
[Day 8: Seven Segment Search](https://adventofcode.com/2021/day/8) | [Python](python/08.py) | I tried two similar approaches for figuring out the digits. Not very satisfied with my code for today...
[Day 9: Smoke Basin](https://adventofcode.com/2021/day/9) | [Python](python/09.py) | BFS, very slow :hourglass_flowing_sand: probably due to using `dict` and `complex`...
[Day 10: Syntax Scoring](https://adventofcode.com/2021/day/10) | [Python](python/10.py) | When I figured that I could run the `autocomplete` function only once, I decided to (mis)use `isinstance` to distinguish between the data for part 1 and part 2 of the puzzle.
[Day 11: Dumbo Octopus](https://adventofcode.com/2021/day/11) | [Python](python/11.py) | Variation of a game of life. I wonder about the right approach to keep track of energy levels. Is it ok to modify a calling parameter without returning it?
