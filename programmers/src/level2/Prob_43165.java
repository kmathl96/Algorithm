/*
 * Ÿ�� �ѹ�
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
        int answer = 0; // Ÿ�� �ѹ��� ����� ����� ��
        
        // ���� : {��� ��, ���� ������ ����}�� ���� ���̹Ƿ� {0,0}���� �ʱ�ȭ
        Stack<int[]> st = new Stack<>();
        st.add(new int[] {0,0});
        
        while (!st.isEmpty()) {
        	int[] cur = st.pop(); // ���� ��, ����� ������ ����
        	
        	// ��� ������ �� ��������� ���ÿ� ���� �ʰ� �Ѿ
        	if (cur[1] == numbers.length) {
        		if (cur[0] == target) answer++; // Ÿ�� �ѹ��� ������ answer ����
        		continue;
        	}
        	
        	// �ش� ������ ������ ���ϰ� �� ���� ���ÿ� ����
        	st.add(new int[] {cur[0]+numbers[cur[1]],cur[1]+1});
        	st.add(new int[] {cur[0]-numbers[cur[1]],cur[1]+1});
        }
        return answer;
    }
}