/*
 * ������
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Prob_624 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine()); // �׽�Ʈ ���̽��� ��
		int[] answers = new int[T]; // �� �׽�Ʈ ���̽��� ���� ������ �迭
		
		// ���� 0~7�� 2^0~2^7�� ���� ����
		// => �� ���ڴ� �� �ڸ����� ���� ������ ���� ������ ǥ��
		// ex) 1�� ���, 2,5��° ������ ���� => 2^2 + 2^5 = 36
		//	   7�� ���, 0,1,2,5��° ������ ���� => 2^0 + 2^1 + 2^2 + 2^5 = 39
		int[] bulbs = {119,36,93,109,46,107,123,39,127,111};
		
		for (int i=0; i<T; i++) {
			int answer = 0; // ����ġ�� ������ �ϴ� Ƚ��
			String s[] = br.readLine().split(" "); // �Էµ� �� ����
			int A = Integer.parseInt(s[0]); // ���� A
			int B = Integer.parseInt(s[1]); // ���� B
			
			// ������ �ڸ��������� ������� �ڸ� �� ��
			for (int j=0; j<5; j++) {
				
				// �ش� �ڸ��� ���ڿ��� ������ ������ ��
				int bulbA = bulbs[A%10];
				int bulbB = bulbs[B%10];
				
				// ������ ǥ�õǴ� 0�� �ƴ� ��� (= ������ �� ���� 0)
				if (A==0) bulbA = 0;
				if (B==0) bulbB = 0;
				
				// ������ �����ִ��� ���ΰ� �ٸ� ���� ���� ���ϱ�
				String diff = Integer.toBinaryString((bulbA)^(bulbB));
				for (int k=0; k<diff.length(); k++) {
					if (diff.charAt(k)=='1') {
						answer++;
					}
				}
				
				// �״��� �ڸ��� ���� �Ǵ��ϱ� ���� 1�� �ڸ� ���� ����
				A = A/10;
				B = B/10;
			}
			answers[i] = answer; // �� ����
		}
		
		// �� �׽�Ʈ ���̽��� ���� ������� ���
		for (int answer : answers) {
			System.out.println(answer);
		}
	}

}
