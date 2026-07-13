import sys
from collections import deque
input = sys.stdin.readline

def get_start_positions(N, maze):
    start_r = start_g = start_b = None
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 'R': start_r = (i, j)
            elif maze[i][j] == 'G': start_g = (i, j)
            elif maze[i][j] == 'B': start_b = (i, j)
    return start_r, start_g, start_b

def is_valid(r, c, N, maze):
    return 0 <= r < N and 0 <= c < N and maze[r][c] != '#'

def precompute_bfs(N, maze, start_r, start_g, start_b):
    dr = [-1, 1, 0, 0, 0]
    dc = [0, 0, -1, 1, 0]

    queue = deque()
    initial_state = (*start_r, *start_g, *start_b, 0) 
    visited = {initial_state: 0}
    queue.append(initial_state)

    while queue:
        rr, rc, gr, gc, br, bc, _ = queue.popleft()
        current_turns = visited[(rr, rc, gr, gc, br, bc, _)]

        nxt_t = current_turns + 1
        mover = nxt_t % 3  

        for d in range(5):
            n_rr, n_rc = rr, rc
            n_gr, n_gc = gr, gc
            n_br, n_bc = br, bc

            if mover == 1:
                n_rr, n_rc = rr + dr[d], rc + dc[d]
                if not is_valid(n_rr, n_rc, N, maze): continue
            elif mover == 2:
                n_gr, n_gc = gr + dr[d], gc + dc[d]
                if not is_valid(n_gr, n_gc, N, maze): continue
            else:
                n_br, n_bc = br + dr[d], bc + dc[d]
                if not is_valid(n_br, n_bc, N, maze): continue

            if (n_rr, n_rc) == (n_gr, n_gc) or \
               (n_gr, n_gc) == (n_br, n_bc) or \
               (n_br, n_bc) == (n_rr, n_rc):
                continue

            nxt_state = (n_rr, n_rc, n_gr, n_gc, n_br, n_bc, nxt_t % 3)
            
            if nxt_state not in visited:
                visited[nxt_state] = nxt_t
                queue.append(nxt_state)

    return visited

def solve_queries(rc_queries, visited):
    for query in rc_queries:
        tr, tc, tg, tgc, tb, tbc = query
        
        tar_r = (tr - 1, tc - 1)
        tar_g = (tg - 1, tgc - 1)
        tar_b = (tb - 1, tbc - 1)

        min_turns = float('inf')
        
        for mod in range(3):
            state = (*tar_r, *tar_g, *tar_b, mod)
            if state in visited:
                min_turns = min(min_turns, visited[state])

        if min_turns == float('inf'):
            print(-1)
        else:
            print(min_turns)

N, Q = map(int, input().split())

maze = [input().strip() for _ in range(N)] 
rc = [list(map(int, input().split())) for _ in range(Q)]

start_r, start_g, start_b = get_start_positions(N, maze)
visited_states = precompute_bfs(N, maze, start_r, start_g, start_b)
solve_queries(rc, visited_states)