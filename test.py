from stack import *
from navigator import *

grid = Maze(5,6)
a = PacMan(grid)
print(a.find_path((0,0), (2,2)))

