/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 11651                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/11651                          #+#        #+#      #+#    */
/*   Solved: 2024/11/02 14:37:30 by judemin       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
import java.io.*;
import java.util.*;

class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        Coordinate [] arr = new Coordinate[N];

        StringTokenizer st;
        for(int i = 0;i < N;i++){
            st = new StringTokenizer(br.readLine());
            arr[i] = new Coordinate(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
        }

        Arrays.sort(arr, comp);

        for(int i = 0;i < N;i++)
            bw.write(arr[i].getX() + " " + arr[i].getY() + "\n");
        bw.flush();
    }

    // 두 개의 Class를 비교하는 것이기 때문에 Comparator 사용
    static Comparator<Coordinate> comp = new Comparator<Coordinate>() {
		// getY() - getY()의 경우
        // 계산 결과가 INT 범위를 벗어날 수도 있기 때문에
        // 이를 주의해야 한다
		@Override
		public int compare(Coordinate o1, Coordinate o2) {
			if(o1.getY() > o2.getY()){
                return 1;
            }else if(o1.getY() == o2.getY()){
                if(o1.getX() > o2.getX())
                    return 1;
                else if(o1.getX() == o2.getX())
                    return 0;
                else
                    return -1;
            }else{
                return -1;
            }
		}
	};
}

class Coordinate{
    int x;
    int y;

    public Coordinate(int x, int y){
        this.x = x;
        this.y = y;
    }

    public int getX(){
        return x;
    }

    public int getY(){
        return y;
    }
}