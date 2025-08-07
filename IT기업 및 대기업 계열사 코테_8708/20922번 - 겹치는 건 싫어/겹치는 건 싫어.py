#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 20922                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/20922                          #+#        #+#      #+#     #
#    Solved: 2025/08/07 21:21:14 by judemin       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
read = sys.stdin.readline
write = sys.stdout.write

# Quque, HashMap
def main():
    N, K = map(int, read().rstrip().rsplit())
    max = 0
    queue = []
    num_dict = {}
    nums = list(map(int, read().rstrip().rsplit()))
    for num in nums:
        if num in num_dict and num_dict[num] + 1 > K:
            if max < len(queue):
                max = len(queue)
            
            while num_dict[num] + 1 > K:
                poped = queue.pop(0)
                num_dict[poped] -= 1
        
        queue.append(num)
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1
    
    if max < len(queue):
        max = len(queue)
    write(f"{max}\n")

if __name__ == "__main__":
    main()