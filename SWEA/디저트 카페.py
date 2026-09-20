# 출발점 기준으로 오른쪽, 왼쪽 대각선으로 움직이는 경로
directions = [[[1, 1], [1, -1], [-1, -1], [-1, 1]], [[1, -1], [1, 1], [-1, 1], [-1, -1]]]

def is_out(y, x, N):
    if y < 0 or y >= N or x < 0 or x >= N:
        return True
    return False

def find_cafe(y, x, N, cafes):
    answer = -1
    max_height = max(y + 1, N - (y + 1))
    max_width = max(x + 1, N - (x + 1))

    for h in range(1, max_height + 1):
        for w in range(1, max_width + 1):
            for d in directions:
                nh, nw, pos = 0, 0, 0
                ny, nx = y, x
                cur_cafe = set([])
                while True:
                    if ny == y and nx == x and pos == 3:
                        answer = max(answer, len(cur_cafe))
                        break
                    ny += d[pos][0]
                    nx += d[pos][1]
                    if is_out(ny, nx, N) or (cafes[ny][nx] in cur_cafe):
                        break
                    cur_cafe.add(cafes[ny][nx])
                    if pos == 0:
                        nw += 1
                        if nw == w:
                            pos += 1
                        continue
                    if pos == 1:
                        nh += 1
                        if nh == h:
                            pos += 1
                        continue
                    if pos == 2:
                        nw += 1
                        if nw == w * 2:
                            pos += 1
    return answer

T = int(input())
for i in range(T):
    answer = -1
    N = int(input())
    cafes = []
    for _ in range(N):
        cafes.append(list(map(int, input().split())))
    
    for y in range(N):
        for x in range(N):
            answer = max(answer, find_cafe(y, x, N, cafes))

    print("#" + str(i + 1), answer)
