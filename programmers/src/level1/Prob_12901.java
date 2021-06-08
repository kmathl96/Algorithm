/*
 * 2016��
 */

package level1;

public class Prob_12901 {
	public static void main(String[] args) {
		Solution_12901 s = new Solution_12901();
		System.out.println(s.solution(5, 24)); // "TUE"
	}
}

class Solution_12901 {
	int[] month = {31,29,31,30,31,30,31,31,30,31,30,31}; // �� ���� ��¥ ��
	String[] week = {"THU","FRI","SAT","SUN","MON","TUE","WED"}; // 2016/1/1�� FRI�̱� ������ THU���� ����
	
	public String solution(int a, int b) {
		int days = b; // �� ��¥�� - �Է°��� �� ��(b)�� �ʱ�ȭ
		for (int i=0; i<a-1; i++) {
			days += month[i]; // (a-1)�������� ��¥ ���ϱ�
		}
		return week[days%7]; // �ش��ϴ� ���� ���
	}
}