/*
 * ���� ���ڴ� �Ⱦ�
 */

package level1;

import java.util.ArrayList;

public class Prob_12906 {
	public static void main(String[] args) {
		Solution_12906 s = new Solution_12906();
		System.out.println(s.solution(new int[] {1,1,3,3,0,1,1})); // [1,3,0,1]
		System.out.println(s.solution(new int[] {4,4,4,3,3})); // [4,3]
	}
}

class Solution_12906 {
	public int[] solution(int []arr) {
        ArrayList<Integer> num = new ArrayList<>();
        int pre = arr[0]; // ���� ���ڸ� arr�� �� ó�� ���ڷ� �ʱ�ȭ
        num.add(pre); // num�� ���ڸ� ����
        for (int i=1; i<arr.length; i++) {
        	if (pre != arr[i]) { // �ش� ���� ���� ���� �ٸ� ���
        		pre = arr[i]; // ���� ���� ����
        		num.add(pre); // �ش� ���� num�� �ֱ�
        	}
        }
        // ��ȯ�� answer �迭�� num�� ��ҵ��� ������� �ֱ�
        int[] answer = new int[num.size()];
        for (int j=0; j<num.size(); j++) {
        	answer[j] = num.get(j);
        }
        return answer;
    }
}