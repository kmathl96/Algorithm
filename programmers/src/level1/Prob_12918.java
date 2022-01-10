/*
 * ���ڿ� �ٷ�� �⺻
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
    	// ���ڿ��� ���̰� 4 Ȥ�� 6�� �ƴϸ� false
        if (s.length() != 4 && s.length() != 6) return false;
        
        // ���ڰ� �ƴ� ���ڰ� �ִ� ��� false
        for (int i=0; i<s.length(); i++) {
        	if (!Character.isDigit(s.charAt(i))) return false;
        }
        
        return true;
    }
}