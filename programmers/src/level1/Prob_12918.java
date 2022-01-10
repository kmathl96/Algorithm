/*
 * 문자열 다루기 기본
 */

package level1;

public class Prob_12918 {

	public static void main(String[] args) {
		Solution_12918 s = new Solution_12918();
		
		System.out.println(s.solution("a234")); // false
		System.out.println(s.solution("1234")); // true
	}

}

class Solution_12918 {
    public boolean solution(String s) {
    	// 문자열의 길이가 4 혹은 6이 아니면 false
        if (s.length() != 4 && s.length() != 6) return false;
        
        // 숫자가 아닌 문자가 있는 경우 false
        for (int i=0; i<s.length(); i++) {
        	if (!Character.isDigit(s.charAt(i))) return false;
        }
        
        return true;
    }
}