/*
 * 완주하지 못한 선수
 */

package level1;

import java.util.Arrays;

public class Prob_42576 {

	public static void main(String[] args) {
		Solution_42576 s = new Solution_42576();

		// example
		System.out.println(s.solution(new String[] {"leo","kiki","eden"}, new String[] {"eden","kiki"})); // "leo"
		System.out.println(s.solution(new String[] {"marina","josipa","nikola","vinko","filipa"}, new String[] {"josipa","filipa","marina","nikola"})); // "vinko"
		System.out.println(s.solution(new String[] {"mislav","stanko","mislav","ana"}, new String[] {"stanko","ana","mislav"})); // "mislav"
	}

}

class Solution_42576 {
    public String solution(String[] participant, String[] completion) {
        // 두 배열 정렬
    	Arrays.sort(participant);
        Arrays.sort(completion);
        for (int i=0; i<completion.length; i++) {
        	// 한 명씩 순서대로 비교
        	// 같지 않으면 참가자가 완주자 목록에 없는 것이므로 해당 참가자 반환
        	if (!participant[i].equals(completion[i])) return participant[i];
        }
        // 마지막에서 2번째 참가자까지 전부 완주자 목록에 있으므로 마지막 참가자가 완주하지 못함
        return participant[participant.length-1];
    }
}