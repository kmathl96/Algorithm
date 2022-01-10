/*
 * 이진수
 * 수학, 구현
 */

package baekjoon;

import java.util.Scanner;

public class Prob_3460 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt(); // 테스트 케이스의 개수
		
		for (int i=0; i<T; i++) {
			int n = sc.nextInt(); // 양의 정수 n
			int idx = 0; // 현재 비트의 위치
			while (n > 0) {
				// 나머지가 1인 경우, 해당 비트를 1로 나타므로 위치 출력
				if (n%2>0) System.out.print(idx + " ");
				
				idx++; // 위치 이동
				n /= 2; // n 갱신
			}
			System.out.println();
		}
		sc.close();
	}
}