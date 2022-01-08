/*
 * 문자열 내 p와 y의 개수
 */

package level1;

public class Prob_12916 {
	public static void main(String[] args) {
		Solution_12916 s = new Solution_12916();
		System.out.println(s.solution("pPoooyY")); // true
		System.out.println(s.solution("Pyy")); // false
	}
}

class Solution_12916 {
	boolean solution(String s) {
        int cnt = 0;
        for (int i=0; i<s.length(); i++) {
        	String str = s.substring(i,i+1);
        	if (str.equals("P") || str.equals("p")) {
        		cnt++;
        	} else if (str.equals("Y") || str.equals("y")) {
        		cnt--;
        	}
        }
        return cnt==0;
    }
}