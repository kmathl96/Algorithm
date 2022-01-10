/*
 * ��� ���ϱ�
 * ����, ���Ʈ���� 	
 */

package baekjoon;

import java.util.Scanner;

public class Prob_2501 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in); // �Է��� �ޱ� ���� Scanner
		
		// N�� ����� �� K��°�� ���� �� ���ϱ�
		int N = sc.nextInt();
		int K = sc.nextInt();
		
		int answer = 0;
		while (answer < N && K > 0) {
			answer++; // 1���� N���� Ȯ��
			
			// answer�� ����̸� K ����
			if (N%answer == 0) K--;
		}
		
		// K��°�� ���� ����� ã�� ���� ���� 0 ���
		System.out.println(K==0? answer:0);
		
		sc.close();
	}

}