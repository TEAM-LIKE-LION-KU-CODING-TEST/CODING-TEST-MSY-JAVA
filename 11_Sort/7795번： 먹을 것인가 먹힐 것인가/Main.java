/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 7795                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/7795                           #+#        #+#      #+#    */
/*   Solved: 2024/11/08 15:03:53 by judemin       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
import java.io.*;
import java.util.*;

class Main{
    public static void main(String [] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int T = Integer.parseInt(br.readLine());
        for(int i = 0;i < T;i++){
            int cnt = 0;
            st = new StringTokenizer(br.readLine());
            
            // N개의 데이터에 대한 중복이 허용되기 때문에
            // 이전 데이터를 저장할 HashMap
            HashMap<Integer, Integer> hm = new HashMap<Integer, Integer>();

            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());

            int[] a = new int[N];
            int[] b = new int[M];

            st = new StringTokenizer(br.readLine());
            for(int j = 0;j < N;j++)
                a[j] = Integer.parseInt(st.nextToken());

            st = new StringTokenizer(br.readLine());
            for(int j = 0;j < M;j++)
                b[j] = Integer.parseInt(st.nextToken());

            // 오름차순으로 b 생명체 크기 정렬
            Arrays.sort(b);

            // 이진탐색 방식으로
            // 현재 a 크기보다 작은 b 생명체 값 구하기
            for(int j = 0;j < N;j++){
                int binResult;
                if(hm.containsKey(a[j])){
                    binResult = hm.get(a[j]);
                } else{
                    binResult = binarySearch(b, 0, M, a[j]);
                    // HashMap에 이전 결과 저장
                    hm.put(a[j], binResult);
                }

                if(binResult > 0){
                    // lower_bound를 찾았을 경우
                    // binResult값을 하나 빼줘야 한다
                    // 1 3 6 에서 1일때 binResult의 결과는 1
                    if(a[j] == b[binResult - 1])
                        binResult--;
                    cnt += binResult;
                }
                // System.out.println(a[j] + " " + binResult);
            }

            bw.write(cnt + "\n");
            bw.flush();
        }
    }

    static int binarySearch(int[] arr, int left, int right, int target){
        if(left >= right)
            return right;

        int mid = (left + right) / 2;
        if(arr[mid] < target){
            return binarySearch(arr, mid + 1, right, target);
        } else{
            // 반례: B의 집합에서 같은 값이 존재할 경우
            // 단순히 이진 탐색이 아니라 동일 값 중에서 가장 작은 인덱스 값을 찾아야 함
            // ... 12 13 14 ...
            // ... 8  8  8  ...
            // 위와 같은 상황이라고 할 때 12를 찾아서 return

            // lower_bound 문제
            // mid - 1이 아닌 mid까지 포함해서 다시 이분 탐색
            // https://12bme.tistory.com/120
            // https://velog.io/@junhok82/lowerbound-upperbound
            return binarySearch(arr, left, mid, target);
        }
    }
}