/*
 * �������� ���� ����
 */

package level1;

import java.util.Arrays;

public class Prob_42576 {

	public static void main(String[] args) {
		Solution_42576 s = new Solution_42576();

		// example
		System.out.println(s.solution(new String[] {"leo","kiki","eden"}, new String[] {"eden","kiki"})); // "leo"
		System.out.println(s.solution(new String[] {"marina","josipa","nikola","vinko","filipa"}, new String[] {"josipa","filipa","marina","nikola"})); // "vinko"
		System.out.println(s.solution(new String[] {"mislav","stanko","mislav","ana"}, new String[] {"stanko","ana","mislav"})); // "mislav"
	}

}

class Solution_42576 {
    public String solution(String[] participant, String[] completion) {
        // �� �迭 ����
    	Arrays.sort(participant);
        Arrays.sort(completion);
        for (int i=0; i<completion.length; i++) {
        	// �� �� ������� ��
        	// ���� ������ �����ڰ� ������ ��Ͽ� ���� ���̹Ƿ� �ش� ������ ��ȯ
        	if (!participant[i].equals(completion[i])) return participant[i];
        }
        // ���������� 2��° �����ڱ��� ���� ������ ��Ͽ� �����Ƿ� ������ �����ڰ� �������� ����
        return participant[participant.length-1];
    }
}