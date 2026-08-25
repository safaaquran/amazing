from maze import MazeGenerator
from Collection import deque

def Finding_shortest_path(grid: list[list[MazeGenerator.Cell]], entry: tuple[int, int], exit_: tuple[int, int]):
    q: deque = deque()
    visited: list[tuple[int, int]] = []
    visited.append(entry)

    q.append(entry)
    neighbor: tuple[int, int]

    while q:
        row, column = q.popleft()
        current = grid[row][column]

        if (row, column) == exit_:
            break

        if not current.Top:
            neighbor = (row - 1, column)
            if neighbor not in visited and not grid[neighbor[0]][neighbor[1]].Lock:
                visited.append(neighbor)
                q.append(neighbor)

        if not current.Left:
            neighbor = (row, column - 1)
            if neighbor not in visited and not grid[neighbor[0]][neighbor[1]].Lock:
                visited.append(neighbor)
                q.append(neighbor)

        if not current.Bottom:
            neighbor = (row + 1, column)
            if neighbor not in visited and not grid[neighbor[0]][neighbor[1]].Lock:
                visited.append(neighbor)
                q.append(neighbor)

        if not current.Right:
            neighbor = (row, column + 1)
            if neighbor not in visited and not grid[neighbor[0]][neighbor[1]].Lock:
                visited.append(neighbor)
                q.append(neighbor)
