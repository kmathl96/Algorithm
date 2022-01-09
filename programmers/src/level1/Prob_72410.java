/*
 * 신규 아이디 추천
 * 정규표현식
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
    	// 1. 소문자로 변환
        String answer = new_id.toLowerCase();
		
        // 2. 알파벳, 숫자, 빼기, 밑줄, 마침표를 제외한 모든 문자 제거 => 정규표현식 사용
        // ^ : 뒤의 문자들을 제외
        // a-z는 a부터 z까지, 0-9는 0부터 9까지의 문자들
        answer = answer.replaceAll("[^a-z0-9-_.]", "");
        
        // 3. 마침표가 2번 이상 연속된 부분을 하나의 마침표로 치환 => 정규표현식 사용
        // {n,(m)} : n번 이상 (m번 이하) 반복된 문자열
		answer = answer.replaceAll("[.]{2,}", ".");
		
		// 4. 마침표가 처음이나 끝에 위치한다면 제거
		if (!answer.isEmpty() && answer.charAt(0)=='.') answer = answer.substring(1);
		if (!answer.isEmpty() && answer.charAt(answer.length()-1)=='.') answer = answer.substring(0, answer.length()-1);

		// 5. 빈 문자열이라면 "a"를 대입
		if (answer.isEmpty()) answer = "a";
		
		// 6. 16자 이상이면, 첫 15개의 문자를 제외한 나머지는 제거
		// 제거 후 마침표가 끝에 위치한다면 제거
		if (answer.length() >= 16) answer = answer.substring(0,answer.charAt(14)=='.'?14:15);
		
		// 7. 길이가 2자 이하인 경우, 3자가 될 때까지 마지막 문자를 반복해 끝에 붙임
		while (answer.length() <= 2)
			answer += answer.charAt(answer.length()-1);
        
		return answer;
    }
}