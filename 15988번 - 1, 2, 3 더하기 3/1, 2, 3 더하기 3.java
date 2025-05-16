import java.io.*;

class Main{
    static int MAX = 1000002;
    static long MODULAR = 1000000009;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        long [] dp = new long[MAX];
        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 4;
        for(int i = 4;i <= MAX - 1;i++)
            dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % MODULAR;

        int T = Integer.parseInt(br.readLine());
        for(int i = 0;i < T;i++){
            int n = Integer.parseInt(br.readLine());
            bw.write("" + (dp[n] % MODULAR) + "\n");
        }
        // flush()를 마지막에 하여 Timeout 방지
        bw.flush();
    }
}

// 테스트 케이스 개수 T개

// n을 1, 2, 3으로 나타내는 방법의 수
// 0 < n < 1,000,000
// 1,000,000,009으로 나눈 나머지 출력력