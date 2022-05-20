/*
 * 전광판
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Prob_624 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine()); // 테스트 케이스의 수
		int[] answers = new int[T]; // 각 테스트 케이스의 답을 저장할 배열
		
		// 전구 0~7은 2^0~2^7의 값을 가짐
		// => 각 숫자는 각 자리마다 켜진 전구의 값의 합으로 표현
		// ex) 1의 경우, 2,5번째 전구가 켜짐 => 2^2 + 2^5 = 36
		//	   7의 경우, 0,1,2,5번째 전구가 켜짐 => 2^0 + 2^1 + 2^2 + 2^5 = 39
		int[] bulbs = {119,36,93,109,46,107,123,39,127,111};
		
		for (int i=0; i<T; i++) {
			int answer = 0; // 스위치를 눌러야 하는 횟수
			String s[] = br.readLine().split(" "); // 입력된 두 숫자
			int A = Integer.parseInt(s[0]); // 숫자 A
			int B = Integer.parseInt(s[1]); // 숫자 B
			
			// 오른쪽 자리에서부터 순서대로 자리 수 비교
			for (int j=0; j<5; j++) {
				
				// 해당 자리의 숫자에서 켜지는 전구의 값
				int bulbA = bulbs[A%10];
				int bulbB = bulbs[B%10];
				
				// 전구로 표시되는 0이 아닌 경우 (= 전구가 다 꺼진 0)
				if (A==0) bulbA = 0;
				if (B==0) bulbB = 0;
				
				// 전구의 켜져있는지 여부가 다른 것의 개수 구하기
				String diff = Integer.toBinaryString((bulbA)^(bulbB));
				for (int k=0; k<diff.length(); k++) {
					if (diff.charAt(k)=='1') {
						answer++;
					}
				}
				
				// 그다음 자리의 수를 판단하기 위해 1의 자리 수를 제거
				A = A/10;
				B = B/10;
			}
			answers[i] = answer; // 답 저장
		}
		
		// 각 테스트 케이스의 답을 순서대로 출력
		for (int answer : answers) {
			System.out.println(answer);
		}
	}

}
