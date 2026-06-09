import java.io.*;

// ASCII a : 97, z : 122
public class boj1919 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out);
        int [] arr1 = new int[27];
        int ans = 0;
        int i;

        String st1 = br.readLine();
        String st2 = br.readLine();

        for(i = 0;i < st1.length();i++){
            char now = st1.charAt(i);
            arr1[now - 'a']++;
        }

        for(i = 0;i < st2.length();i++){
            char now = st2.charAt(i);
            arr1[now - 'a']--;
        }

        for(i = 0;i < 27;i++){
            int now = arr1[i];
            if(now < 0)
                now *= -1;
            
            ans += now;
        }

        pw.println(ans);
        pw.flush();
    }
}
