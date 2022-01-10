/*
 * 최대공약수와 최소공배수
 * 수학, 정수론, 유클리드 호제법
 */

package baekjoon;

import java.util.Scanner;

public class Prob_2609 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		// 두 개의 자연수
		int num1 = sc.nextInt();
		int num2 = sc.nextInt();

		// gcd 함수에서 처리하기 용이하도록 둘 중 더 큰 값을 num1로 저장
		if (num2 > num1) {
			int temp = num1;
			num1 = num2;
			num2 = temp;
		}
		
		int gcd = gcd(num1,num2); // 최대공약수
		System.out.println(gcd);
		System.out.println(num1*num2/gcd); // 최소공배수 = 두 수의 곱을 최대공약수로 나눈 것
		
		sc.close();
	}
	
	// 최대공약수 구하기 : 유클리드 호제법 활용
	static int gcd(int a, int b) {
		if (b==0) return a; // a와 0의 최대공약수는 a
		if (b==1) return 1; // a와 1의 최대공약수는 1
		return gcd(b, a%b); // 작은 값과, 큰 값을 작은 값으로 나눈 나머지의 최대공약수와 같음
	}
}