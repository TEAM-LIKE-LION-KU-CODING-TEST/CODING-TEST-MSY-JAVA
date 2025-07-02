import java.util.*;

class Job{
    // 작업번호, 요청시점, 소요시간
    public int jobN;
    public int requestT;
    public int processT;
    
    public Job(int jobN, int requestT, int processT){
        this.jobN = jobN;
        this.requestT = requestT;
        this.processT = processT;
    }
}

// 우선순위 큐를 이용
class Solution {
    int N;
    PriorityQueue<Job> pq;
    Job[]job;
    
    private int addSameTime(int idx){
        // 현재 인덱스의 Job의 요청시간
        // 해당 요청시간과 동일한 요청시간을 가진 Job은 모두 추가
        int requestT = job[idx].requestT;
        while(idx < N && requestT == job[idx].requestT){
            pq.add(job[idx]);
            idx++;
        }
        return idx;
    }
    
    public int solution(int[][] jobs) {
        int answer = 0;
        N = jobs.length;
        job = new Job[N];
        
        for(int i = 0;i < N;i++)
            job[i] = new Job(i + 1, jobs[i][0], jobs[i][1]);
        // requestT 기준 오름차순 정렬
        Arrays.sort(job, comp);
        
        pq = new PriorityQueue<>((j1, j2) -> {
            if (j1.processT > j2.processT) return  1;
            if (j1.processT < j2.processT) return -1;
            // processT 같을 때
            if (j1.requestT > j2.requestT) return  1;
            if (j1.requestT < j2.requestT) return -1;
            // requestT도 같을 때
            if (j1.jobN > j2.jobN) return  1;
            if (j1.jobN < j2.jobN) return -1;
            // jobN까지 같을 때 (실제로는 발생하지 않음)
            // Comparator 규약상 “두 객체가 동등(equal)할 때는 0을 반환”해야 함
            // return 0 을 제거하면 모든 비교에서 -1 또는 1만 반환하게 되어,
            // 동등성이 사라지고 비교 로직이 일관성을 잃어 정렬/우선순위 큐 내부 알고리즘이 예측 불가능하게 동작
            return 0;
        });
        
        // 0번째 Job과 요청시각이 동일한 Job을 모두 pq에 추가
        // ex. 0ms 시점의 작업이 3개인 경우
        int idx = addSameTime(0);
        int time = pq.peek().requestT;
        // 처음 while문에 진입했을 때 pq는 비어있지 않음
        while(idx < N){
            Job head = pq.poll();
            // 소요시간 만큼 time 증가
            time += head.processT;
            // turnaround time 계산 후 누적
            answer += (time - head.requestT);
        
            // 현재시간보다 요청시각이 작은 job을 pq에 모두 추가
            while(idx < N && job[idx].requestT < time){
                pq.add(job[idx]);
                idx++;
            }
            
            // 만약 pq가 비어있다면 (중간에 대기시간이 존재하는 경우)
            if(pq.isEmpty()){
                // 다음 idx의 같은 시점의 작업을 pq에 모두 추가
                idx = addSameTime(idx);
                // 현재 시각을 pq의 head의 요청시간으로 설정
                time = pq.peek().requestT;
            }
        }
        
        // flush
        while(!pq.isEmpty()){
            Job head = pq.poll();
            // 소요시간 만큼 time 증가
            time += head.processT;
            // turnaround time 계산 후 누적
            answer += (time - head.requestT);
        }
        
        // 반환시간의 평균
        return (int)(answer / N);
    }
    
    static Comparator<Job>comp = new Comparator<Job>(){
        @Override
        public int compare(Job j1, Job j2){
            // 1, 0, -1을 리턴하는 조건을 모두 주어야 한다
            if(j1.requestT > j2.requestT)
                return 1;
            else if(j1.requestT == j2.requestT)
                return 0;
            return -1;
        }
    };
}