/*
 * 가운데 글자 가져오기
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
        int len = s.length(); // 단어의 길이
        int idx = (int)(len+1)/2-1; // 가운데 글자 index 값
        return s.substring(idx,idx+2-len%2); // 짝수이면 두 글자 반환
    }
}