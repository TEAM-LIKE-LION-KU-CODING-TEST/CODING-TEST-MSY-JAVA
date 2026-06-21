n = int(input())

A = 1
for i in range(1, n + 1):
	A *= i

while (A // 10) != 0:
	tmpA = A
	B = 0
	while tmpA != 0:
		B += (tmpA % 10)
		tmpA = tmpA // 10
	A = B

print(A)