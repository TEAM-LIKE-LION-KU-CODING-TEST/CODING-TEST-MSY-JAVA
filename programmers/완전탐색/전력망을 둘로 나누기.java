// Tree 형태 : Cycle이 존재하지 않는다

class Solution {
    int abs(int a){
        if(a < 0)
            return a * -1;
        return a;
    }
    
    int proc(int[][]map, int[]check, int now, int n){
        int cnt = 1;
        for(int i = 1;i <= n;i++){
            if(map[now][i] == 1 && check[i] != 1){
                check[i] = 1;
                cnt += proc(map, check, i, n);
            }
        }
        return cnt;
    }
    
    public int solution(int n, int[][] wires) {
        int N = wires.length;
        int answer = 987654321;
        
        int[][]map = new int[n + 10][n + 10];
        for(int i = 0;i < N;i++){
            map[wires[i][0]][wires[i][1]] = 1;
            map[wires[i][1]][wires[i][0]] = 1;
        }
        
        for(int i = 0;i < N;i++){
            int[]check = new int[n + 10];
            map[wires[i][0]][wires[i][1]] = 0;
            map[wires[i][1]][wires[i][0]] = 0;
            
            int now = wires[i][0];
            check[now] = 1;
            
            int cnt = proc(map, check, now, n);
            int leftOver = n - cnt;
            
            answer = Math.min(answer, abs(leftOver - cnt));
            
            map[wires[i][0]][wires[i][1]] = 1;
            map[wires[i][1]][wires[i][0]] = 1;
        }
        
        return answer;
    }
}