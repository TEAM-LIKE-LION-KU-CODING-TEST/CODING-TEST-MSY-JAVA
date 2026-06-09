#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1446                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1446                           #+#        #+#      #+#     #
#    Solved: 2025/08/09 13:32:58 by judemin       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import heapq
import sys
read = sys.stdin.readline
write = sys.stdout.write

# 정수 무한대 상수
INT_INF = int(1e9)

# 다익스트라
def dijkstra(start, graph, distance):
    q = []
    heapq.heappush(q,(0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        # 힙큐에서 pop한 요소가 now까지 가는데 최소비용이 아닌 경우
        if dist > distance[now]:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))

# 지름길 도착 지점이 k라면 k번째에서 시작하는 다음 지름길 이용 가능
def main():
    N,D = map(int,read().rstrip().rsplit())

    graph = [[] for _ in range(D+1)]
    distance = [INT_INF] * (D+1)

    # 일단 거리 1로 초기화
    for i in range(D):
        graph[i].append((i+1, 1))
    
    for _ in range(N):
        s, e, l = map(int, read().rstrip().rsplit())
        # 정확히 D만큼만 가야한다, 더 가면 안됨
        if e > D:
            continue
        # 도착 위치, 지름길의 길이
        graph[s].append((e, l))
    
    dijkstra(0, graph, distance)
    write(str(distance[D]))


if __name__ == "__main__":
    main()