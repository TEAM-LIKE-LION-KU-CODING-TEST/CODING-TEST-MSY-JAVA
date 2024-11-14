/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 2170                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/2170                           #+#        #+#      #+#    */
/*   Solved: 2024/11/14 15:01:25 by judemin       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
import java.io.*;
import java.util.*;

class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        ArrayList<Location> locList = new ArrayList<>();
        long result = 0;

        int N = Integer.parseInt(br.readLine());
        Location[] locations = new Location[N];
        for(int i = 0;i < N;i++){
            st = new StringTokenizer(br.readLine());
            locations[i] = new Location(
                Long.parseLong(st.nextToken()),
                Long.parseLong(st.nextToken())
            );
        }

        // x를 기준으로 오름차순 정렬
        // x가 같다면 y를 기준으로 오름차순 정렬
        Arrays.sort(locations, comp);

        Location nowLoc = locations[0];
        for(int i = 1;i < N;i++){
            // x2 <= y1
            if(locations[i].getX() <= nowLoc.getY()){
                // obj1 = (x1, MAX(y1, y2))
                nowLoc.setY(Max(locations[i].getY(), nowLoc.getY()));
            }else{
                locList.add(nowLoc);
                nowLoc = locations[i];
            }
        }
        locList.add(nowLoc);

        Iterator iter = locList.iterator();
        while(iter.hasNext()){
            Location tmp = (Location) iter.next();
            result += tmp.getY() - tmp.getX();
        }

        System.out.println(result);
    }

    static long Max(long a, long b){
        if(a > b)
            return a;
        return b;
    }

    static Comparator<Location> comp = new Comparator<Location>() {
        // Long.compare()를 사용해 Comparator의 일관성을 유지 정렬 과정에서의 IllegalArgumentException을 방지
        // 직접 비교 연산자를 사용하면 비교 과정에서 오버플로우나 예기치 않은 결과로 인해 Comparator의 일관성이 깨질 수 있음
        // 반면 Long.compare()는 모든 long 값에 대해 올바른 비교를 보장하여 안정적이고 일관된 결과를 제공
        @Override
        public int compare(Location o1, Location o2) {
            int cmpX = Long.compare(o1.getX(), o2.getX());
            if (cmpX != 0) {
                return cmpX;
            } else {
                return Long.compare(o1.getY(), o2.getY());
            }
        }
    };
}

// 범위가 10억이기 때문에 long으로 계산
class Location{
    long x;
    long y;

    public Location(long x, long y){
        this.x = x;
        this.y = y;
    }

    public Long getX(){
        return x;
    }

    public Long getY(){
        return y;
    }

    public void setX(long x){
        this.x = x;
    }

    public void setY(long y){
        this.y = y;
    }
}

/*
// 정렬 테스트
5
4 4
4 1
4 7
1 2
3 2

3
-100 -50
-80 0
100 200

200

2
-1000000000 -100
0 100

1000000000


3
1 6
2 3
4 5

5
*/