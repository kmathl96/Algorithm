/*
 * ������
 * ť
 */

package level2;

import java.util.LinkedList;
import java.util.Queue;

public class Prob_42587 {

	public static void main(String[] args) {
		Solution_42587 s = new Solution_42587();
		
		System.out.println(s.solution(new int[] {2,1,3,2},2)); // 1
		System.out.println(s.solution(new int[] {1,1,9,1,1,1},0));
	}

}

class Solution_42587 {
    public int solution(int[] priorities, int location) {
        int answer = 0; // �μ� Ƚ��
        
        // ť : {�߿䵵, ����}�� ���� ������� ����
        Queue<int[]> q = new LinkedList<int[]>();
        for (int i=0; i<priorities.length; i++) {
        	q.add(new int[] {priorities[i],i});
        }
        
        while (!q.isEmpty()) {
        	// 1. �μ� ������� ���� �տ� �ִ� ����(J)�� ����
        	int[] j = q.poll();
        	
        	// 2. ������ �μ� ������� ���� Ž��
        	boolean flag = true; // J�� �μ� ����
        	for (int[] node : q) {
        		// J���� �߿䵵�� ���� ������ �� ���� �ִ� ���
        		if (node[0] > j[0]) {
        			flag = false; // �μ����� ����
        			break;
        		}
        	}
        	
        	if (!flag) { // J�� �μ����� ���ϴ� ���
        		q.add(j); // J�� ������� ���� �������� ����
        	} else { // J�� �μ��ϴ� ���
        		answer++; // �μ� Ƚ�� ����
        		
        		// ���� ��û�� ������ ���, �� Ž���� �ʿ䰡 �����Ƿ� ����
        		if (j[1] == location) break;
        	}
        }
        return answer;
    }
}