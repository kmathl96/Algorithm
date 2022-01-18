/*
 * �ùٸ� ��ȣ
 * ����
 */

package level2;

import java.util.Stack;

public class Prob_12909 {

	public static void main(String[] args) {
		Solution_12909 s = new Solution_12909();
		
		// example
		System.out.println(s.solution("()()")); // true
		System.out.println(s.solution("(())()")); // true
		System.out.println(s.solution(")()(")); // false
		System.out.println(s.solution("(()(")); // false
	}

}

class Solution_12909 {
    boolean solution(String s) {
        Stack<Integer> st = new Stack<>(); // ����
        
        // ���ڿ��� ó������ ������� Ž��
        for (int i=0; i<s.length(); i++) {
        	
        	// ���� ��ȣ�� ���ÿ� �ֱ�
        	if (s.charAt(i) == '(') {
        		st.add(1);
    		// ���� ��ȣ�ε� ���ÿ� ���� ��ȣ�� �ִ� ���
        	} else if (!st.isEmpty() && st.get(st.size()-1)==1) {
        		st.pop(); // ���ÿ��� ���� ��ȣ ����
    		// ���� ��ȣ�ε� ������ ����ִ� ���, �߸��� ��ȣ�̹Ƿ� false ��ȯ
        	} else return false;
        }
        
        // ��� ���ڿ��� Ž������ ��, ���� ��ȣ�� ���ÿ� ���������� �ùٸ��� ����
        // => ������ ����ִ� ��� true, �ƴ� ��� false ��ȯ
        return st.isEmpty();
    }
}