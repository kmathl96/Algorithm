/*
 * ���� ���� �� �����ϱ�
 */

package level1;

public class Prob_12935 {
	public static void main(String[] args) {
		Solution_12935 s = new Solution_12935();
		System.out.println(s.solution(new int[] {4,3,2,1})); // [4,3,2]
		System.out.println(s.solution(new int[] {10})); // [-1]
	}
}

class Solution_12935 {
	public int[] solution(int[] arr) {
        int len = arr.length;
        if (len == 1) return new int[] {-1}; // �迭�� ���Ұ� �ϳ��̸� [-1] ��ȯ
        int[] answer = new int[len-1]; // ��ȯ�� �迭
        int min = arr[0]; // �ּڰ�
        int min_idx = 0; // �ּڰ��� index ��
        for (int i=1; i<len; i++) { // index 1���� ��
        	if (min > arr[i]) { // ���� �ּڰ����� ���� ���
        		min = arr[i]; // �ּڰ� ����
        		min_idx = i; // �ּڰ� index ����
        	}
        }
        int idx = 0; // answer�� ä�� index ��
        for (int i=0; i<len; i++) { // arr ��ȸ
        	if (i==min_idx) continue; // �ּڰ��� index�̸� �Ѿ
        	answer[idx++] = arr[i]; // answer[idx]�� ���� �����ϰ� idx ���� ������Ŵ
        }
        return answer;
    }
}