/*
 * 기능개발
 * 스택/큐
 */

package level2;

import java.util.LinkedList;
import java.util.Queue;

public class Prob_42586 {
	public static void main(String[] args) {
		Solution_42586 s = new Solution_42586();
		System.out.println(s.solution(new int[] {93,30,55}, new int[] {1,30,5})); // [2,1]
		System.out.println(s.solution(new int[] {95,90,99,99,80,99}, new int[] {1,1,1,1,1,1})); // [1,3,2]
		
		System.out.println(s.solution(new int[] {96,99,98,97}, new int[] {1,1,1,1})); // [4]
	}
}

class Solution_42586 {
	public int[] solution(int[] progresses, int[] speeds) {
		// 몇 개의 기능이 배포되는지
		// 우선 기능의 개수로 초기화하여 저장한 후, answer 배열을 만들어서 다시 저장할 것
        int[] cnts = new int[progresses.length];
        
        // 큐 : 각 작업이 완료되는 데 걸리는 기간
        Queue<Integer> q = new LinkedList<Integer>();
        for (int i=0; i<progresses.length; i++) {
        	q.add((99-progresses[i])/speeds[i]+1);
        }
        
        int idx = 0; // (idx+1)번째 배포
        while (!q.isEmpty()) {
        	int cnt = 1; // 배포할 기능의 개수
        	int cur = q.poll(); // 아직 배포되지 않은 기능 중 제일 앞에 있는 것
        	
        	// 큐의 길이를 미리 저장한 후 for문에 사용해야 모든 요소들을 다 탐색할 수 있음
        	// 그렇지 않으면, poll이 실행됐을 경우 큐의 길이가 짧아져서 다 순회하지 못하고 for문이 종료됨
        	int len = q.size();
        	for (int i=0; i<len; i++) {
        		if (q.peek() > cur) break; // 앞에 있는 기능보다 작업이 늦게 완료된다면 종료
        		
        		// 해당 기능도 앞 기능과 같이 배포됨
        		cnt++; // 기능 개수 증가
        		q.poll(); // 큐에서 제거
        	}
        	
        	// 배포된 기능 개수 저장 및 idx 값 증가
        	cnts[idx++] = cnt;
        }
        
        // answer를 배포 횟수에 맞게 초기화한 후, cnts 값 저장하고 반환
        int[] answer = new int[idx];
        for (int i=0; i<idx; i++) {
        	answer[i] = cnts[i];
        }
        return answer;
    }
}