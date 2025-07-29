#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 20006                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/20006                          #+#        #+#      #+#     #
#    Solved: 2025/07/29 13:18:05 by judemin       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
read = sys.stdin.readline
write = sys.stdout.write

def main():
    p, m = map(int,read().rstrip().rsplit())

    rooms = {}
    for _ in range(p):
        l, n = map(str,read().rstrip().rsplit())
        l = int(l)

        has_room = False
        for key in rooms:
            if len(rooms[key]) == m:
                continue

            cur_level = int(rooms[key][0][0])
            if cur_level - 10 <= l and l <= cur_level + 10:
                rooms[key].append((l, n))
                has_room = True
                break

        if has_room is False:
            rooms[n] = [(l, n)]

    for key in rooms:
        if len(rooms[key]) == m:
            write("Started!\n")
        else:
            write("Waiting!\n")

        cur_room_list = rooms[key]
        sorted(cur_room_list, key = lambda x:(x[1]))
        for l, n in cur_room_list:
            write(f"{l} {n}\n")

if __name__ == "__main__":
    main()