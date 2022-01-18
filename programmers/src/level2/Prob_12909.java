/*
 * 올바른 괄호
 * 스택
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
        Stack<Integer> st = new Stack<>(); // 스택
        
        // 문자열을 처음부터 순서대로 탐색
        for (int i=0; i<s.length(); i++) {
        	
        	// 열린 괄호는 스택에 넣기
        	if (s.charAt(i) == '(') {
        		st.add(1);
    		// 닫힌 괄호인데 스택에 열린 괄호가 있는 경우
        	} else if (!st.isEmpty() && st.get(st.size()-1)==1) {
        		st.pop(); // 스택에서 열린 괄호 제거
    		// 닫힌 괄호인데 스택이 비어있는 경우, 잘못된 괄호이므로 false 반환
        	} else return false;
        }
        
        // 모든 문자열을 탐색했을 때, 열린 괄호가 스택에 남아있으면 올바르지 않음
        // => 스택이 비어있는 경우 true, 아닌 경우 false 반환
        return st.isEmpty();
    }
}