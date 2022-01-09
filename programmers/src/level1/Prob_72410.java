/*
 * �ű� ���̵� ��õ
 * ����ǥ����
 */

package level1;

public class Prob_72410 {

	public static void main(String[] args) {
		Solution_72410 s = new Solution_72410();
		
		// example
		System.out.println(s.solution("...!@BaT#*..y.abcdefghijklm")); // "bat.y.abcdefghi"
		System.out.println(s.solution("z-+.^.")); // "z--"
		System.out.println(s.solution("=.=")); // "aaa"
		System.out.println(s.solution("123_.def")); // "123_.def"
		System.out.println(s.solution("abcdefghijklmn.p")); // "abcdefghijklmn"
	}

}

class Solution_72410 {
    public String solution(String new_id) {
    	// 1. �ҹ��ڷ� ��ȯ
        String answer = new_id.toLowerCase();
		
        // 2. ���ĺ�, ����, ����, ����, ��ħǥ�� ������ ��� ���� ���� => ����ǥ���� ���
        // ^ : ���� ���ڵ��� ����
        // a-z�� a���� z����, 0-9�� 0���� 9������ ���ڵ�
        answer = answer.replaceAll("[^a-z0-9-_.]", "");
        
        // 3. ��ħǥ�� 2�� �̻� ���ӵ� �κ��� �ϳ��� ��ħǥ�� ġȯ => ����ǥ���� ���
        // {n,(m)} : n�� �̻� (m�� ����) �ݺ��� ���ڿ�
		answer = answer.replaceAll("[.]{2,}", ".");
		
		// 4. ��ħǥ�� ó���̳� ���� ��ġ�Ѵٸ� ����
		if (!answer.isEmpty() && answer.charAt(0)=='.') answer = answer.substring(1);
		if (!answer.isEmpty() && answer.charAt(answer.length()-1)=='.') answer = answer.substring(0, answer.length()-1);

		// 5. �� ���ڿ��̶�� "a"�� ����
		if (answer.isEmpty()) answer = "a";
		
		// 6. 16�� �̻��̸�, ù 15���� ���ڸ� ������ �������� ����
		// ���� �� ��ħǥ�� ���� ��ġ�Ѵٸ� ����
		if (answer.length() >= 16) answer = answer.substring(0,answer.charAt(14)=='.'?14:15);
		
		// 7. ���̰� 2�� ������ ���, 3�ڰ� �� ������ ������ ���ڸ� �ݺ��� ���� ����
		while (answer.length() <= 2)
			answer += answer.charAt(answer.length()-1);
        
		return answer;
    }
}