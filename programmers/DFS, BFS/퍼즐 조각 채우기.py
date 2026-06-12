from collections import deque

def get_normalized(coords):
    coords.sort()
    min_r, min_c = coords[0][0], coords[0][1]
    return [(r - min_r, c - min_c) for r, c in coords]

def rotate(coords):
    return get_normalized([(c, -r) for r, c in coords])

def solution(game_board, table):
    answer = 0
    n = len(game_board)
    
    def get_pieces(board, is_table):
        pieces = []
        visited = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if (is_table and board[i][j] == 1 and not visited[i][j]) or \
                   (not is_table and board[i][j] == 0 and not visited[i][j]):
                    coords = []
                    q = deque([(i, j)])
                    visited[i][j] = True
                    while q:
                        r, c = q.popleft()
                        coords.append((r, c))
                        for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                                if (is_table and board[nr][nc] == 1) or \
                                   (not is_table and board[nr][nc] == 0):
                                    visited[nr][nc] = True
                                    q.append((nr, nc))
                    pieces.append(get_normalized(coords))
        return pieces

    puzzles = get_pieces(table, True)
    blanks = get_pieces(game_board, False)
    
    used_puzzles = [False] * len(puzzles)
    for blank in blanks:
        for i, puzzle in enumerate(puzzles):
            if used_puzzles[i] or len(blank) != len(puzzle):
                continue
            
            curr_puzzle = puzzle
            for _ in range(4):
                if blank == curr_puzzle:
                    answer += len(blank)
                    used_puzzles[i] = True
                    break
                curr_puzzle = rotate(curr_puzzle)
            if used_puzzles[i]:
                break
                
    return answer