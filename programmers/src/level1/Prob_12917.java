/*
 * ���ڿ� ������������ ��ġ�ϱ�
 */

package level1;

import java.util.Arrays;
import java.util.Collections;

public class Prob_12917 {

	public static void main(String[] args) {
		Solution_12917 s = new Solution_12917();
		
		// example
		System.out.println(s.solution("Zbcdefg")); // "gfedcbZ"
	}

}

class Solution_12917 {
    public String solution(String s) {
        String answer = "";
        String[] strArr = s.split(""); // �迭�� ����
        Arrays.sort(strArr, Collections.reverseOrder()); // �������� ����
        for (String str : strArr) {
        	answer += str; // answer�� �ڿ� ���̱�
        }
        return answer;

//		toCharArray �̿�
//        char[] charArr = s.toCharArray();
//        Arrays.sort(charArr); // �������� ����
//        for (char ch : charArr) {
//        	answer = ch + answer; // answer�� �տ� ���̱�
//        }
//        return answer;
    }
}