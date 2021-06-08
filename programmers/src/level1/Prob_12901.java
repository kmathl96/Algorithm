/*
 * 2016년
 */

package level1;

public class Prob_12901 {
	public static void main(String[] args) {
		Solution_12901 s = new Solution_12901();
		System.out.println(s.solution(5, 24)); // "TUE"
	}
}

class Solution_12901 {
	int[] month = {31,29,31,30,31,30,31,31,30,31,30,31}; // 각 달의 날짜 수
	String[] week = {"THU","FRI","SAT","SUN","MON","TUE","WED"}; // 2016/1/1는 FRI이기 때문에 THU부터 시작
	
	public String solution(int a, int b) {
		int days = b; // 총 날짜수 - 입력값의 일 수(b)로 초기화
		for (int i=0; i<a-1; i++) {
			days += month[i]; // (a-1)월까지의 날짜 더하기
		}
		return week[days%7]; // 해당하는 요일 출력
	}
}