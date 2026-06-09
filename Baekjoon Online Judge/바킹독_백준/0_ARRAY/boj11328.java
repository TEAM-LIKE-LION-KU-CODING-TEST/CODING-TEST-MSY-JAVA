import java.io.*;
import java.util.*;

public class boj11328 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int num = Integer.parseInt(br.readLine());

        for(int i = 0;i < num;i++){
            int arr[] = new int[27];
            boolean flag = true;

            StringTokenizer st = new StringTokenizer(br.readLine());
            String st1 = st.nextToken();
            String st2 = st.nextToken();
            
            if(st1.length() != st2.length()){
                bw.write("Impossible\n");
                continue;
            }

            for(int j = 0;j < st1.length();j++){
                arr[st1.charAt(j) - 'a']++;
                arr[st2.charAt(j) - 'a']--;
            }

            for(int j = 0;j < 27;j++){
                if(arr[j] != 0){
                    bw.write("Impossible\n");
                    flag = false;
                    break;
                }
            }

            if(flag)
                bw.write("Possible\n");
        }

        br.close();
        bw.close();
    }
}
