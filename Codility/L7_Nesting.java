import java.util.*;

class Solution {
    public int solution(String S) {
        Stack<Character> st = new Stack();
        int N = S.length();

        for(int i = 0;i < N;i++){
            char now = S.charAt(i);
            if(st.isEmpty() && now == ')')
                return 0;
            else if(!st.isEmpty() && now == ')')
                st.pop();
            else
                st.push(now);
        }
        if(!st.isEmpty())
            return 0;

        return 1;
    }
}
