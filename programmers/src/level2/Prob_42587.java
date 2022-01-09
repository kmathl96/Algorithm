/*
 * 프린터
 * 큐
 */

package level2;

import java.util.LinkedList;
import java.util.Queue;

public class Prob_42587 {

	public static void main(String[] args) {
		Solution_42587 s = new Solution_42587();
		
		System.out.println(s.solution(new int[] {2,1,3,2},2)); // 1
		System.out.println(s.solution(new int[] {1,1,9,1,1,1},0));
	}

}

class Solution_42587 {
    public int solution(int[] priorities, int location) {
        int answer = 0; // 인쇄 횟수
        
        // 큐 : {중요도, 순서}를 문서 순서대로 넣음
        Queue<int[]> q = new LinkedList<int[]>();
        for (int i=0; i<priorities.length; i++) {
        	q.add(new int[] {priorities[i],i});
        }
        
        while (!q.isEmpty()) {
        	// 1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 꺼냄
        	int[] j = q.poll();
        	
        	// 2. 나머지 인쇄 대기목록의 문서 탐색
        	boolean flag = true; // J의 인쇄 여부
        	for (int[] node : q) {
        		// J보다 중요도가 높은 문서가 한 개라도 있는 경우
        		if (node[0] > j[0]) {
        			flag = false; // 인쇄하지 못함
        			break;
        		}
        	}
        	
        	if (!flag) { // J를 인쇄하지 못하는 경우
        		q.add(j); // J를 대기목록의 가장 마지막에 넣음
        	} else { // J를 인쇄하는 경우
        		answer++; // 인쇄 횟수 증가
        		
        		// 내가 요청한 문서인 경우, 더 탐색할 필요가 없으므로 종료
        		if (j[1] == location) break;
        	}
        }
        return answer;
    }
}