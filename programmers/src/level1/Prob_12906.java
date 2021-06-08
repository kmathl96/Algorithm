/*
 * 같은 숫자는 싫어
 */

package level1;

import java.util.ArrayList;

public class Prob_12906 {
	public static void main(String[] args) {
		Solution_12906 s = new Solution_12906();
		System.out.println(s.solution(new int[] {1,1,3,3,0,1,1})); // [1,3,0,1]
		System.out.println(s.solution(new int[] {4,4,4,3,3})); // [4,3]
	}
}

class Solution_12906 {
	public int[] solution(int []arr) {
        ArrayList<Integer> num = new ArrayList<>();
        int pre = arr[0]; // 이전 숫자를 arr의 맨 처음 숫자로 초기화
        num.add(pre); // num에 숫자를 넣음
        for (int i=1; i<arr.length; i++) {
        	if (pre != arr[i]) { // 해당 값이 이전 값과 다른 경우
        		pre = arr[i]; // 이전 숫자 갱신
        		num.add(pre); // 해당 값을 num에 넣기
        	}
        }
        // 반환할 answer 배열에 num의 요소들을 순서대로 넣기
        int[] answer = new int[num.size()];
        for (int j=0; j<num.size(); j++) {
        	answer[j] = num.get(j);
        }
        return answer;
    }
}