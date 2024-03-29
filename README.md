# :christmas_tree: :snake: :sparkles: Maja's Advent of Code 2021 :sparkles: :snake: :christmas_tree:

Ho, ho, ho, welcome to my 2021 Advent of Code repository!
This year, my goals are:

1. complete first 10 puzzles :white_check_mark:
2. collect at least 25 stars :white_check_mark:

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
[Day 12: Passage Pathing](https://adventofcode.com/2021/day/12) | [Python](python/12.py) | Recursive DFS I found on [Stack Exchange](https://stackoverflow.com/a/2606671) and modified to work with puzzle requirements. I still want to clean this up.
[Day 13: Transparent Origami](https://adventofcode.com/2021/day/13) | [Python](python/13.py) | Very fun puzzle! Sets and printing from sets (added a new helper here).
[Day 14: Extended Polymerization](https://adventofcode.com/2021/day/14) | [Python](python/14.py) | I hate polymers.
[Day 15: Chiton](https://adventofcode.com/2021/day/15) | [Python](python/15.py) | [Dijkstra algorithm from Red blob games](https://www.redblobgames.com/pathfinding/a-star/introduction.html), mostly. Added some helpers for neighbors in a grid.
[Day 18: Snailfish](https://adventofcode.com/2021/day/18) | [Python](python/18.py) | This was my [Sea Monster](https://adventofcode.com/2020/day/20) of year 2021! I could not figure out the recursion/tree necessary to treat the numbers correctly so I just did string (list) manipulation instead. But then, I didn't know how to do magnitude calculation without recursion and correct structure so I reformatted the strings back to nested lists and... Ugh- :hammer: :ambulance: :pray: :fire: :cry: :cold_sweat:
[Day 19: Beacon Scanner](https://adventofcode.com/2021/day/19) | [Python](python/19.py) | I am very satisfied about using a generator for trying out different 3D rotations of the beacons.
[Day 20: Trench Map](https://adventofcode.com/2021/day/20) | [Python](python/20.py) | The trick with the input data was that the infinity switches between on and off and I had issues figuring out what is the _right_ amount of padding to be added to the map for it to work properly.
[Day 21: Dirac Dice](https://adventofcode.com/2021/day/21) | [Python](python/21.py) | The trick for solving part 2 was realizing that some permutations result in the same sum of dice numbers which was key for solving it.
[Day 22: Reactor Reboot](https://adventofcode.com/2021/day/22) | [Python](python/22.py) | Cuboids! Given a bunch of coordinates it was impossible to work with sets here to figure out the intersections. I defined a `Cuboid` class which is defined by its borders. I defined intersection operations and then played a bit to figure out how to implement the [Inclusion-exclusion principle](https://en.wikipedia.org/wiki/Inclusion%E2%80%93exclusion_principle). This trick `intersection.switch = not first.switch` made it so much more elegant (I didn't think of that one myself, I saw it in one of the Reddit solutions).
[Day 23: Amphipod](https://adventofcode.com/2021/day/23) | pen and paper | Solved both parts by hand. I would like to solve this using [A* algorithm](https://www.redblobgames.com/pathfinding/a-star/introduction.html).
[Day 24: Arithmetic Logic Unit](https://adventofcode.com/2021/day/24) | pen and paper | Solved by hand using the condition that z always has to be divisible by zero (I couldn't figure this one completely on my own so looked on Reddit for hints).
[Day 25: Sea Cucumber](https://adventofcode.com/2021/day/25) | [Python](python/25.py) | Sets for each cucumber herd. Straightforward.
