/*
 * ��� ���� ��������
 */

package level1;

public class Prob_12903 {
	public static void main(String[] args) {
		Solution_12903 s = new Solution_12903();
		System.out.println(s.solution("abcde")); // "c"
		System.out.println(s.solution("qwer")); // "we"
	}
}

class Solution_12903 {
	public String solution(String s) {
        int len = s.length(); // �ܾ��� ����
        int idx = (int)(len+1)/2-1; // ��� ���� index ��
        return s.substring(idx,idx+2-len%2); // ¦���̸� �� ���� ��ȯ
    }
}