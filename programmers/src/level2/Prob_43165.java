/*
 * 타겟 넘버
 * DFS
 */

package level2;

import java.util.Stack;

public class Prob_43165 {

	public static void main(String[] args) {
		Solution_43165 s = new Solution_43165();
		
		System.out.println(s.solution(new int[] {1,1,1,1,1}, 3)); // 5
	}

}

class Solution_43165 {
    public int solution(int[] numbers, int target) {
        int answer = 0; // 타겟 넘버를 만드는 방법의 수
        
        // 스택 : {계산 값, 계산된 정수의 개수}를 넣을 것이므로 {0,0}으로 초기화
        Stack<int[]> st = new Stack<>();
        st.add(new int[] {0,0});
        
        while (!st.isEmpty()) {
        	int[] cur = st.pop(); // 현재 값, 계산한 정수의 개수
        	
        	// 모든 정수를 다 계산했으면 스택에 넣지 않고 넘어감
        	if (cur[1] == numbers.length) {
        		if (cur[0] == target) answer++; // 타겟 넘버와 같으면 answer 증가
        		continue;
        	}
        	
        	// 해당 순서의 정수를 더하고 뺀 값을 스택에 넣음
        	st.add(new int[] {cur[0]+numbers[cur[1]],cur[1]+1});
        	st.add(new int[] {cur[0]-numbers[cur[1]],cur[1]+1});
        }
        return answer;
    }
}