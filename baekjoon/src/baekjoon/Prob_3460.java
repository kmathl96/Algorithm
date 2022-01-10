/*
 * ������
 * ����, ����
 */

package baekjoon;

import java.util.Scanner;

public class Prob_3460 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt(); // �׽�Ʈ ���̽��� ����
		
		for (int i=0; i<T; i++) {
			int n = sc.nextInt(); // ���� ���� n
			int idx = 0; // ���� ��Ʈ�� ��ġ
			while (n > 0) {
				// �������� 1�� ���, �ش� ��Ʈ�� 1�� ��Ÿ�Ƿ� ��ġ ���
				if (n%2>0) System.out.print(idx + " ");
				
				idx++; // ��ġ �̵�
				n /= 2; // n ����
			}
			System.out.println();
		}
		sc.close();
	}
}