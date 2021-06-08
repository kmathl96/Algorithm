/*
 * 제일 작은 수 제거하기
 */

package level1;

public class Prob_12935 {
	public static void main(String[] args) {
		Solution_12935 s = new Solution_12935();
		System.out.println(s.solution(new int[] {4,3,2,1})); // [4,3,2]
		System.out.println(s.solution(new int[] {10})); // [-1]
	}
}

class Solution_12935 {
	public int[] solution(int[] arr) {
        int len = arr.length;
        if (len == 1) return new int[] {-1}; // 배열의 원소가 하나이면 [-1] 반환
        int[] answer = new int[len-1]; // 반환할 배열
        int min = arr[0]; // 최솟값
        int min_idx = 0; // 최솟값의 index 값
        for (int i=1; i<len; i++) { // index 1부터 비교
        	if (min > arr[i]) { // 현재 최솟값보다 작은 경우
        		min = arr[i]; // 최솟값 갱신
        		min_idx = i; // 최솟값 index 갱신
        	}
        }
        int idx = 0; // answer에 채울 index 값
        for (int i=0; i<len; i++) { // arr 순회
        	if (i==min_idx) continue; // 최솟값의 index이면 넘어감
        	answer[idx++] = arr[i]; // answer[idx]에 값을 저장하고 idx 값을 증가시킴
        }
        return answer;
    }
}