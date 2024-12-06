from maze import *
from exception import *
from stack import *

class PacMan:
    #def __init__(self, grid : Maze) -> None:
        ## DO NOT MODIFY THIS FUNCTION
    #    self.navigator_maze = grid.grid_representation
    #def find_path(self, start : tuple[int, int], end : tuple[int, int]) -> list[tuple[int, int]]:
    
    def __init__(self, grid ):
        ## DO NOT MODIFY THIS FUNCTION
        self.navigator_maze = grid.grid_representation
    def find_path(self, start, end):

    
        # IMPLEMENT FUNCTION HERE
        #changes from here
        rows = len(self.navigator_maze)
        cols = len(self.navigator_maze[0])

        if self.navigator_maze[start[0]][start[1]] == 1 or self.navigator_maze[end[0]][end[1]] == 1:
            raise PathNotFoundException()

        stack = Stack()
        stack.push((start, [start]))

        visited = set()
        visited.add(start)

        while not stack.is_empty():
            (current_pos, path) = stack.pop()
            x, y = current_pos

            if current_pos == end:
                return path

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Up, Down, Left, Right
                new_x, new_y = x + dx, y + dy
                new_pos = (new_x, new_y)

                if (0 <= new_x < rows and 0 <= new_y < cols and
                        self.navigator_maze[new_x][new_y] == 0 and
                        new_pos not in visited):
                    visited.add(new_pos)
                    stack.push((new_pos, path + [new_pos]))
        
        
        raise PathNotFoundException
