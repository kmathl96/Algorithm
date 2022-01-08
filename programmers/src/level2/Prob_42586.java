/*
 * ��ɰ���
 * ����/ť
 */

package level2;

import java.util.LinkedList;
import java.util.Queue;

public class Prob_42586 {
	public static void main(String[] args) {
		Solution_42586 s = new Solution_42586();
		System.out.println(s.solution(new int[] {93,30,55}, new int[] {1,30,5})); // [2,1]
		System.out.println(s.solution(new int[] {95,90,99,99,80,99}, new int[] {1,1,1,1,1,1})); // [1,3,2]
		
		System.out.println(s.solution(new int[] {96,99,98,97}, new int[] {1,1,1,1})); // [4]
	}
}

class Solution_42586 {
	public int[] solution(int[] progresses, int[] speeds) {
		// �� ���� ����� �����Ǵ���
		// �켱 ����� ������ �ʱ�ȭ�Ͽ� ������ ��, answer �迭�� ���� �ٽ� ������ ��
        int[] cnts = new int[progresses.length];
        
        // ť : �� �۾��� �Ϸ�Ǵ� �� �ɸ��� �Ⱓ
        Queue<Integer> q = new LinkedList<Integer>();
        for (int i=0; i<progresses.length; i++) {
        	q.add((99-progresses[i])/speeds[i]+1);
        }
        
        int idx = 0; // (idx+1)��° ����
        while (!q.isEmpty()) {
        	int cnt = 1; // ������ ����� ����
        	int cur = q.poll(); // ���� �������� ���� ��� �� ���� �տ� �ִ� ��
        	
        	// ť�� ���̸� �̸� ������ �� for���� ����ؾ� ��� ��ҵ��� �� Ž���� �� ����
        	// �׷��� ������, poll�� ������� ��� ť�� ���̰� ª������ �� ��ȸ���� ���ϰ� for���� �����
        	int len = q.size();
        	for (int i=0; i<len; i++) {
        		if (q.peek() > cur) break; // �տ� �ִ� ��ɺ��� �۾��� �ʰ� �Ϸ�ȴٸ� ����
        		
        		// �ش� ��ɵ� �� ��ɰ� ���� ������
        		cnt++; // ��� ���� ����
        		q.poll(); // ť���� ����
        	}
        	
        	// ������ ��� ���� ���� �� idx �� ����
        	cnts[idx++] = cnt;
        }
        
        // answer�� ���� Ƚ���� �°� �ʱ�ȭ�� ��, cnts �� �����ϰ� ��ȯ
        int[] answer = new int[idx];
        for (int i=0; i<idx; i++) {
        	answer[i] = cnts[i];
        }
        return answer;
    }
}