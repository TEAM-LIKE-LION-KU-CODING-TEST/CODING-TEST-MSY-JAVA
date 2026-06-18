check = {}
stack = []
direction = {"R" : [1, 0], "L" : [-1, 0],"U" : [0, 1],"D" : [0, -1]}

n = int(input())
cmd = input()
scores = list(map(int, input().split()))

nowX = 0
nowY = 0
check["0,0"] = True
stack.append([0,0,1])
for i in range(n):
	nowX += direction[cmd[i]][0]
	nowY += direction[cmd[i]][1]
	pos_str = f"{nowX},{nowY}"
	while stack and check.get(pos_str, False):
		poped = stack.pop()
		check[f"{poped[0]},{poped[1]}"] = False
	check[pos_str] = True
	stack.append([nowX,nowY,scores[i]])

answer = 0
for st in stack:
	answer += st[2]
print(answer)