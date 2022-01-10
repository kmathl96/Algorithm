/*
 * �ִ������� �ּҰ����
 * ����, ������, ��Ŭ���� ȣ����
 */

package baekjoon;

import java.util.Scanner;

public class Prob_2609 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		// �� ���� �ڿ���
		int num1 = sc.nextInt();
		int num2 = sc.nextInt();

		// gcd �Լ����� ó���ϱ� �����ϵ��� �� �� �� ū ���� num1�� ����
		if (num2 > num1) {
			int temp = num1;
			num1 = num2;
			num2 = temp;
		}
		
		int gcd = gcd(num1,num2); // �ִ�����
		System.out.println(gcd);
		System.out.println(num1*num2/gcd); // �ּҰ���� = �� ���� ���� �ִ������� ���� ��
		
		sc.close();
	}
	
	// �ִ����� ���ϱ� : ��Ŭ���� ȣ���� Ȱ��
	static int gcd(int a, int b) {
		if (b==0) return a; // a�� 0�� �ִ������� a
		if (b==1) return 1; // a�� 1�� �ִ������� 1
		return gcd(b, a%b); // ���� ����, ū ���� ���� ������ ���� �������� �ִ������� ����
	}
}