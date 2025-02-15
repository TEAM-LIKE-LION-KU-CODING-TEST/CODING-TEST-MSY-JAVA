import java.util.*;

class Solution {
    public int solution(int[] A) {
        int N = A.length;

        // 배열의 길이가 0일때는 dominator가 없고
        // 배열의 길이가 1일때는 dominator가 무조건 존재한다
        if(N == 0)
            return -1;
        if(N == 1)
            return 0;

        Pair[] pair = new Pair[N];
        for(int i = 0;i < N;i++)
            pair[i] = new Pair(A[i], i);

        // num, 즉 A[i]를 기준으로 정렬
        Arrays.sort(pair, comp);
        
        // 전체를 순회하면서 같은 수 카운트
        int cnt = 1;
        Pair nowPair = pair[0];
        for(int i = 1;i < N;i++){
            // 현재까지 카운트하고 있던 Num과 다르다면
            // 해당 Num이 dominator인지 판단하고 값 초기화
            if(nowPair.getNum() != pair[i].getNum()){
                if(cnt > (N / 2))
                    return nowPair.getIdx();
                nowPair = pair[i];
                cnt = 1;
            }else{
                cnt ++;
            }
        }
        // 만약 모든 루프를 다 돌았을 경우
        // 혹시나 마지막으로 저장된 수가 dominator일 경우 검사
        if(cnt > (N / 2))
            return nowPair.getIdx();

        return -1;
    }

    Comparator<Pair> comp = new Comparator<Pair>(){
        public int compare(Pair p1, Pair p2){
            if(p1.getNum() > p2.getNum()){
                return 1;
            }else if(p1.getNum() == p2.getNum()){
                if(p1.getIdx() > p2.getIdx())
                    return 1;
                else if(p1.getIdx() == p2.getIdx())
                    return 0;
                else
                    return -1;
            }else{
                return -1;
            }
        }
    };
}

class Pair{
    int num;
    int idx;

    public Pair(int num, int idx){
        this.num = num;
        this.idx = idx;
    }

    public int getNum(){
        return num;
    }

    public int getIdx(){
        return idx;
    }

    @Override
    public String toString(){
        return "(" + num + "," + idx + ")";
    }
}