answer = []

N = int(input())
for i in range(N):
	A = list(map(int, input().split()))[1:]
	B = list(map(int, input().split()))[1:]
	A_dict = {}
	B_dict = {}
	for a in A:
		A_dict[a] = A_dict.get(a, 0) + 1
	for b in B:
		B_dict[b] = B_dict.get(b, 0) + 1
	flag = False
	for j in range(4, 0, -1):
		if A_dict.get(j, 0) > B_dict.get(j, 0):
			answer.append('A')
			flag = True
			break
		if A_dict.get(j, 0) < B_dict.get(j, 0):
			answer.append('B')
			flag = True
			break
	if not flag:
		answer.append('D')

for ans in answer:
	print(ans)	