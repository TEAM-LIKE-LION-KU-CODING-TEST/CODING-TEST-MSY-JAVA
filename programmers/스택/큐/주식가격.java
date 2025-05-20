import java.util.*;

class Pair{
    private int price;
    private int time;
    
    public Pair(int price, int time){
        this.price = price;
        this.time = time;
    }
    
    public int getPrice(){
        return this.price;
    }
    
    public int getTime(){
        return this.time;
    }
}

class Solution {
    public int[] solution(int[] prices) {
        Stack<Pair>st = new Stack<>();
        int n = prices.length;
        int[] answer = new int[n];
        
        st.push(new Pair(prices[0], 0));
        for(int i = 1;i < n;i++){
            if(st.isEmpty()){
                st.push(new Pair(prices[i], i));
            } else if(st.peek().getPrice() <= prices[i]){
                st.push(new Pair(prices[i], i));
            } else if(st.peek().getPrice() > prices[i]){
                while(!st.isEmpty()){
                    if(st.peek().getPrice() <= prices[i])
                        break;
                    Pair p = st.pop();
                    answer[p.getTime()] = (i - p.getTime());
                }
                st.push(new Pair(prices[i], i));
            }
        }        
        
        while(!st.isEmpty()){
            Pair p = st.pop();
            answer[p.getTime()] = ((n - 1) - p.getTime());
        }
        
        return answer;
    }
}