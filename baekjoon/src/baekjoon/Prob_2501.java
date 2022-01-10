/*
 * 약수 구하기
 * 수학, 브루트포스 	
 */

package baekjoon;

import java.util.Scanner;

public class Prob_2501 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in); // 입력을 받기 위한 Scanner
		
		// N의 약수들 중 K번째로 작은 수 구하기
		int N = sc.nextInt();
		int K = sc.nextInt();
		
		int answer = 0;
		while (answer < N && K > 0) {
			answer++; // 1부터 N까지 확인
			
			// answer이 약수이면 K 감소
			if (N%answer == 0) K--;
		}
		
		// K번째로 작은 약수를 찾지 못한 경우는 0 출력
		System.out.println(K==0? answer:0);
		
		sc.close();
	}

}