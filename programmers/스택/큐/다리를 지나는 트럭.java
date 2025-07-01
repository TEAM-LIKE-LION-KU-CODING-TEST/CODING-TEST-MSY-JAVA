import java.util.*;

class Pair{
    public int startTime;
    public int weight;
    
    public Pair(int startTime, int weight){
        this.startTime = startTime;
        this.weight = weight;
    }
}

class Solution {
    Queue<Pair>q = new LinkedList<>();
    int curTrucks = 0;
    int curWeight = 0;
    // 1번쨰 트럭이 진입하는 시간을 1
    // 그 다음 검사와 트럭 진입을 위한 시점을 1로 잡아야 함
    int time = 2;
    
    private void printQ(){
        if(q.isEmpty())
            return;
        Pair head = q.peek();
        System.out.printf("Head: [%d, %d], Time: %d, Trucks: %d, Weight: %d\n"
                          , head.startTime, head.weight, time, curTrucks, curWeight);
    }
    
    public void addTruck(int truck_weights, int bridge_length){
        q.add(new Pair(time, truck_weights));
        curTrucks++;
        curWeight+=truck_weights;
        printQ();
        time++;
        deleteOverTimedTruck(bridge_length);
    }
    
    private void deleteOverTimedTruck(int bridge_length){
        while(!q.isEmpty()){
            Pair head = q.peek();
            // time - head.startTime
            // 현재까지 흐른 시간 - 트럭이 진입한 시간
            // = 해당 트럭이 현재까지 다리 위에 있던 시간
            int timeOnBridge = time - head.startTime;
            if(timeOnBridge > bridge_length){
                q.poll();
                curTrucks--;
                curWeight-=head.weight;
            }else{
                break;
            }
        }
    }
    
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int N = truck_weights.length;  
        
        q.add(new Pair(1, truck_weights[0]));
        curTrucks++;
        curWeight+=truck_weights[0];
        for(int i = 1;i < N;i++){
            // 다음 트럭이 진입할 수 있는지 여부를 검사
            // 미리 이를 추가하고 검사하는 방식은 X
            if(curWeight + truck_weights[i] <= weight && curTrucks + 1 <= bridge_length){
                addTruck(truck_weights[i], bridge_length);
            }else{  // 현재 다리에 더 이상 다른 트럭이 진입할 수 없을 때
                // 다리에 다른 트럭이 진입할 수 있을때까지
                while(!q.isEmpty() && (curWeight + truck_weights[i] > weight || curTrucks + 1 > bridge_length)){
                    printQ();
                    Pair head = q.poll();
                    curTrucks--;
                    curWeight-=head.weight;
                    // 맨 앞에 있는 트럭이 다리를 건널 수 있을때까지의 시간
                    int timeNeeded =  bridge_length - (time - head.startTime);
                    // 임의로 다리를 건널 수 있을때까지 시간을 추가
                    time += timeNeeded;
                }
                // 대기중인 트럭을 다리에 올린다
                addTruck(truck_weights[i], bridge_length);
            }
        }
        
        // 마지막 대기 트럭들이 다리에 있을 때 flush
        while(!q.isEmpty()){
            printQ();
            Pair head = q.poll();
            // 맨 앞에 있는 트럭이 다리를 건널 수 있을때까지의 시간
            int timeNeeded =  bridge_length - (time - head.startTime);
            // 임의로 다리를 건널 수 있을때까지 시간을 추가
            time += timeNeeded;
        }
        
        return time;
    }
}