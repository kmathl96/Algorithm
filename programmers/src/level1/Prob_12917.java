/*
 * 문자열 내림차순으로 배치하기
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
        String[] strArr = s.split(""); // 배열로 만듦
        Arrays.sort(strArr, Collections.reverseOrder()); // 내림차순 정렬
        for (String str : strArr) {
        	answer += str; // answer의 뒤에 붙이기
        }
        return answer;

//		toCharArray 이용
//        char[] charArr = s.toCharArray();
//        Arrays.sort(charArr); // 오름차순 정렬
//        for (char ch : charArr) {
//        	answer = ch + answer; // answer의 앞에 붙이기
//        }
//        return answer;
    }
}