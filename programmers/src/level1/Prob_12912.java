/*
 * 두 정수 사이의 합
 */

package level1;

public class Prob_12912 {
	public static void main(String[] args) {
		Solution_12912 s = new Solution_12912();
		System.out.println(s.solution(3,5)); // 12
		System.out.println(s.solution(3,3)); // 3
		System.out.println(s.solution(5,3)); // 12
	}
}

class Solution_12912 {
	public long solution(int a, int b) {
        long answer = 0;
        if (b<a) {        	
        	int temp = a;
        	a = b;
        	b = temp;
        }
        for (int i=a; i<=b; i++) {
        	answer += i;
        }
        return answer;
    }
}