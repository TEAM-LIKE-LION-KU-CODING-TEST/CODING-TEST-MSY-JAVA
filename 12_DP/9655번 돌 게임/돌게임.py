import sys
# 빠른 출력을 위해 기본 print 함수 대신
# sys.stdout.write를 사용하도록 덮어씌우기기
print = sys.stdout.write

def main():
    # 빠른 입력을 위해 input 대신 sys.stdin.readline 함수를 사용
    N = int(sys.stdin.readline().rstrip())
    dp = []

    # 돌이 1개일 경우 : 1회, SK 승리
    # 돌이 2개일 경우 : 1->1, 2회, CY 승리
    dp.append(0)
    dp.append(1)
    dp.append(2)

    # 두 사람이 완벽하게 게임을 한다
    # = 최소의 횟수만을 가지고 게임을 진행한다
    for i in range(3, N + 1):
        nowVal = min(dp[i - 1] + 1, dp[i - 3] + 1)
        dp.append(nowVal)
    
    # SK : 홀수 횟수의 게임에서 승리
    # CY : 짝수 횟수의 게임에서 승리
    if(dp[N] % 2 == 1):
        print('SK\n')
    else:
        print('CY\n')

if __name__ == "__main__":
    main()