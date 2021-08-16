# Algorithm :penguin:

> 알고리즘 문제 풀이 코드를 업로드합니다.

- 표 설명 :mag:
  - 문제 : 해당 문제 페이지로 이동
  - 문제 제목 : 내 풀이 코드
    - 문제 제목 옆에 언어를 구분해놓지 않은 문제는 `Python`으로 풂
  - 알고리즘 : 해당 문제의 알고리즘 분류 또는 내가 푼 방법
- 비고 : 내가 풀어볼 방법 또는 공부할 알고리즘, 문제 출처, 기타
  
- [백준](#baekjoon)
- [프로그래머스](#programmers)
  - [Level 1](#level-1) :egg:
  - [Level 2](#level-2) :hatching_chick:
  - [Level 3](#level-3) :hatched_chick:
  - [Level 4](#level-4) :chicken:
  - [SQL](#sql)​ (알고리즘은 아니지만:dolphin:)



## Baekjoon

| 문제                                           | 문제 제목                                              | 알고리즘                                                     | 비고                                                         |
| :--------------------------------------------- | ------------------------------------------------------ | ------------------------------------------------------------ | :----------------------------------------------------------- |
| [1052](https://www.acmicpc.net/problem/1052)   | [물병](baekjoon/1052.py)                               | 구현, 그리디, 시뮬레이션, 비트마스킹                         |                                                              |
| [1062](https://www.acmicpc.net/problem/1062)   | [가르침](baekjoon/1062.py)                             | 브루트포스, 비트마스킹, 백트래킹                             |                                                              |
| [1107](https://www.acmicpc.net/problem/1107)   | [리모컨](baekjoon/1107.py)                             | 브루트포스                                                   |                                                              |
| [1182](https://www.acmicpc.net/problem/1182)   | [부분수열의 합](baekjoon/1182.py)                      | 브루트 포스                                                  |                                                              |
| [1197](https://www.acmicpc.net/problem/1197)   | [최소 스패닝 트리](baekjoon/1197.py)                   | MST, 크루스칼                                                | 프림                                                         |
| [1260](https://www.acmicpc.net/problem/1260)   | [DFS와 BFS](baekjoon/1260.py)                          | DFS, BFS                                                     |                                                              |
| [1261](https://www.acmicpc.net/problem/1261)   | [알고스팟](baekjoon/1261.py)                           | BFS                                                          | 다익스트라                                                   |
| [1339](https://www.acmicpc.net/problem/1339)   | [단어 수학](baekjoon/1339.py)                          | 그리디, 브루트포스                                           |                                                              |
| [1340](https://www.acmicpc.net/problem/1340)   | [연도 진행바](baekjoon/201231_%EC%83%88%ED%95%B4/a.py) | 구현,  문자열, 파싱                                          | :memo: ​_2020-12-31 새해_                                     |
| [1463](https://www.acmicpc.net/problem/1463)   | [1로 만들기](baekjoon/1463.py)                         | DP                                                           |                                                              |
| [1476](https://www.acmicpc.net/problem/1476)   | [날짜 계산](baekjoon/1476.py)                          | 브루트 포스                                                  | 중국인의 나머지 정리                                         |
| [1644](https://www.acmicpc.net/problem/1644)   | [소수의 연속합](baekjoon/1644.py)                      | 투 포인터, 에라토스테네스의 체, 수학, 정수론                 |                                                              |
| [1654](https://www.acmicpc.net/problem/1654)   | [랜선 자르기](baekjoon/1654.py)                        | 이분 탐색, 매개 변수 탐색                                    |                                                              |
| [1697](https://www.acmicpc.net/problem/1697)   | [숨바꼭질](baekjoon/1697.py)                           | BFS                                                          |                                                              |
| [1699](https://www.acmicpc.net/problem/1699)   | [제곱수의 합](baekjoon/1699.py)                        | DP, 수학, 정수론                                             |                                                              |
| [1707](https://www.acmicpc.net/problem/1707)   | [이분 그래프](baekjoon/1707.py)                        | BFS                                                          |                                                              |
| [1748](https://www.acmicpc.net/problem/1748)   | [수 이어 쓰기 1](baekjoon/1748.py)                     | 수학, 구현                                                   |                                                              |
| [1759](https://www.acmicpc.net/problem/1759)   | [암호 만들기](baekjoon/1759.py)                        | 브루트 포스, 수학, 조합론, 백트래킹                          |                                                              |
| [1806](https://www.acmicpc.net/problem/1806)   | [부분합](baekjoon/1806.py)                             | 투 포인터                                                    |                                                              |
| [1912](https://www.acmicpc.net/problem/1912)   | [연속합](baekjoon/1912.py)                             | DP                                                           |                                                              |
| [1920](https://www.acmicpc.net/problem/1920)   | [수 찾기](baekjoon/1920.py)                            | 이분 탐색                                                    |                                                              |
| [1927](https://www.acmicpc.net/problem/1927)   | [최소 힙](baekjoon/1927.py)                            | 힙                                                           |                                                              |
| [1934](https://www.acmicpc.net/problem/1934)   | [최소공배수](baekjoon/1934.py)                         | 유클리드 호제법                                              |                                                              |
| [1966](https://www.acmicpc.net/problem/1966)   | [프린터 큐](baekjoon/1966.py)                          | 큐, 구현, 자료 구조, 시뮬레이션                              |                                                              |
| [1978](https://www.acmicpc.net/problem/1978)   | [소수 찾기](baekjoon/1978.py)                          | 에라토스테네스의 체                                          |                                                              |
| [1987](https://www.acmicpc.net/problem/1987)   | [알파벳](baekjoon/1987.py)                             | DFS, 백트래킹                                                |                                                              |
| [2003](https://www.acmicpc.net/problem/2003)   | [수들의 합 2](baekjoon/2003.py)                        | 투 포인터                                                    |                                                              |
| [2110](https://www.acmicpc.net/problem/2110)   | [공유기 설치](baekjoon/2110.py)                        | 이분 탐색                                                    |                                                              |
| [2156](https://www.acmicpc.net/problem/2156)   | [포도주 시식](baekjoon/2156.py)                        | DP                                                           |                                                              |
| [2178](https://www.acmicpc.net/problem/2178)   | [미로 탐색](baekjoon/2178.py)                          | BFS                                                          |                                                              |
| [2193](https://www.acmicpc.net/problem/2193)   | [이친수](baekjoon/2193.py)                             | DP                                                           |                                                              |
| [2206](https://www.acmicpc.net/problem/2206)   | [벽 부수고 이동하기](baekjoon/2206.py)                 | BFS                                                          |                                                              |
| [2225](https://www.acmicpc.net/problem/2225)   | [합분해](baekjoon/2225.py)                             | DP                                                           |                                                              |
| [2304](https://www.acmicpc.net/problem/2304)   | [창고 다각형](baekjoon/2304.py)                        | 브루트 포스                                                  | 스택                                                         |
| [2309](https://www.acmicpc.net/problem/2309)   | [일곱 난쟁이](baekjoon/2309.py)                        | 브루트 포스                                                  |                                                              |
| [2529](https://www.acmicpc.net/problem/2529)   | [부등호](baekjoon/2529.py)                             | 브루트포스, 백트래킹                                         |                                                              |
| [2580](https://www.acmicpc.net/problem/2580)   | [스도쿠](baekjoon/2580.py)                             | 백트래킹, DFS                                                |                                                              |
| [2606](https://www.acmicpc.net/problem/2606)   | [바이러스](baekjoon/2606.py)                           | DFS                                                          |                                                              |
| [2609](https://www.acmicpc.net/problem/2609)   | [최대공약수와 최소공배수](baekjoon/2609.py)            | 유클리드 호제법                                              |                                                              |
| [2667](https://www.acmicpc.net/problem/2667)   | [단지번호붙이기](baekjoon/2667.py)                     | DFS                                                          |                                                              |
| [2805](https://www.acmicpc.net/problem/2805)   | [나무 자르기](baekjoon/2805.py)                        | 이분 탐색                                                    | [B#1654](https://www.acmicpc.net/problem/1654)와 비슷        |
| [3055](https://www.acmicpc.net/problem/3055)   | [탈출](baekjoon/3055.py)                               | BFS                                                          |                                                              |
| [4963](https://www.acmicpc.net/problem/4963)   | [섬의 개수](baekjoon/4963.py)                          | BFS                                                          |                                                              |
| [6064](https://www.acmicpc.net/problem/6064)   | [카잉 달력](baekjoon/6064.py)                          | 수학, 정수론, 중국인의 나머지 정리                           |                                                              |
| [6588](https://www.acmicpc.net/problem/6588)   | [골드바흐의 추측](baekjoon/6588.py)                    | 에라토스테네스의 체                                          |                                                              |
| [6603](https://www.acmicpc.net/problem/6603)   | [로또](baekjoon/6603.py)                               | 브루트 포스, 조합론                                          | 재귀                                                         |
| [7576](https://www.acmicpc.net/problem/7576)   | [토마토](baekjoon/7576.py)                             | BFS                                                          |                                                              |
| [9095](https://www.acmicpc.net/problem/9095)   | [1, 2, 3 더하기](baekjoon/9095.py)                     | 브루트 포스                                                  | DP                                                           |
| [9372](https://www.acmicpc.net/problem/9372)   | [상근이의 여행](baekjoon/9372.py)                      | 최소 신장 트리, 크루스칼                                     |                                                              |
| [9465](https://www.acmicpc.net/problem/9465)   | [스티커](baekjoon/9465.py)                             | DP                                                           |                                                              |
| [9613](https://www.acmicpc.net/problem/9613)   | [GCD 합](baekjoon/9613.py)                             | 유클리드 호제법                                              |                                                              |
| [9663](https://www.acmicpc.net/problem/9663)   | [N-Queen](baekjoon/9663.py)                            | 브루트포스, 백트래킹                                         |                                                              |
| [10815](https://www.acmicpc.net/problem/10815) | [숫자 카드](baekjoon/10815.py)                         | 이분 탐색                                                    |                                                              |
| [10816](https://www.acmicpc.net/problem/10816) | [숫자 카드 2](baekjoon/10816.py)                       | 해시, 이분 탐색                                              |                                                              |
| [10819](https://www.acmicpc.net/problem/10819) | [차이를 최대로](baekjoon/10819.py)                     | 브루트 포스, 백트래킹                                        |                                                              |
| [10844](https://www.acmicpc.net/problem/10844) | [쉬운 계단 수](baekjoon/10844.py)                      | DP                                                           |                                                              |
| [10971](https://www.acmicpc.net/problem/10971) | [외판원 순회 2](baekjoon/10971.py)                     | 브루트 포스, 백트래킹                                        |                                                              |
| [10972](https://www.acmicpc.net/problem/10972) | [다음 순열](baekjoon/10972.py)                         | 브루트 포스, 수학                                            |                                                              |
| [10973](https://www.acmicpc.net/problem/10973) | [이전 순열](baekjoon/10973.py)                         | 브루트 포스, 수학                                            |                                                              |
| [10974](https://www.acmicpc.net/problem/10974) | [모든 순열](baekjoon/10974.py)                         | 브루트 포스                                                  |                                                              |
| [11047](https://www.acmicpc.net/problem/11047) | [동전 0](baekjoon/11047.py)                            | 그리디 알고리즘                                              |                                                              |
| [11052](https://www.acmicpc.net/problem/11052) | [카드 구매하기](baekjoon/11052.py)                     | DP                                                           |                                                              |
| [11053](https://www.acmicpc.net/problem/11053) | [가장 긴 증가하는 부분 수열](baekjoon/11053.py)        | DP                                                           |                                                              |
| [11054](https://www.acmicpc.net/problem/11054) | [가장 긴 바이토닉 부분 수열](baekjoon/11054.py)        | DP                                                           |                                                              |
| [11055](https://www.acmicpc.net/problem/11055) | [가장 큰 증가 부분 수열](baekjoon/11055.py)            | DP                                                           |                                                              |
| [11057](https://www.acmicpc.net/problem/11057) | [오르막 수](baekjoon/11057.py)                         | DP                                                           |                                                              |
| [11279](https://www.acmicpc.net/problem/11279) | [최대 힙](baekjoon/11279.py)                           | 힙                                                           |                                                              |
| [11664](https://www.acmicpc.net/problem/11664) | [선분과 점](baekjoon/11664.py)                         | 이분 탐색, 기하학, 3차원 기하학, 삼분 탐색                   |                                                              |
| [11722](https://www.acmicpc.net/problem/11722) | [가장 긴 감소하는 부분 수열](baekjoon/11722.py)        | DP                                                           |                                                              |
| [11723](https://www.acmicpc.net/problem/11723) | [집합](baekjoon/11723.py)                              | 브루트 포스                                                  | 비트마스킹                                                   |
| [11724](https://www.acmicpc.net/problem/11724) | [연결 요소의 개수](baekjoon/11724.py)                  | BFS                                                          |                                                              |
| [11726](https://www.acmicpc.net/problem/11726) | [2×n 타일링](baekjoon/11726.py)                        | DP                                                           |                                                              |
| [11727](https://www.acmicpc.net/problem/11727) | [2×n 타일링 2](baekjoon/11727.py)                      | DP                                                           |                                                              |
| [13023](https://www.acmicpc.net/problem/13023) | [ABCDE](baekjoon/13023.py)                             | DFS                                                          |                                                              |
| [13398](https://www.acmicpc.net/problem/13398) | [연속합 2](baekjoon/13398.py)                          | DP                                                           |                                                              |
| [13458](https://www.acmicpc.net/problem/13458) | [시험 감독](baekjoon/13458.py)                         | 수학                                                         |                                                              |
| [13549](https://www.acmicpc.net/problem/13549) | [숨바꼭질 3](baekjoon/13549.py)                        | BFS                                                          | 다익스트라                                                   |
| [14002](https://www.acmicpc.net/problem/14002) | [가장 긴 증가하는 부분 수열 4](baekjoon/14002.py)      | DP                                                           |                                                              |
| [14226](https://www.acmicpc.net/problem/14226) | [이모티콘](baekjoon/14226.py)                          | BFS                                                          | DP                                                           |
| [14499](https://www.acmicpc.net/problem/14499) | [주사위 굴리기](baekjoon/14499.py)                     | 구현, 브루트 포스                                            |                                                              |
| [14500](https://www.acmicpc.net/problem/14500) | [테트로미노](baekjoon/14500.py)                        | 구현, 브루트 포스                                            |                                                              |
| [14501](https://www.acmicpc.net/problem/14501) | [퇴사](baekjoon/14501.py)                              | 브루트 포스                                                  | DP                                                           |
| [14503](https://www.acmicpc.net/problem/14503) | [로봇 청소기](baekjoon/14503.py)                       | 구현, 시뮬레이션                                             |                                                              |
| [14888](https://www.acmicpc.net/problem/14888) | [연산자 끼워넣기](baekjoon/14888.py)                   | 브루트 포스, 백트래킹                                        |                                                              |
| [14889](https://www.acmicpc.net/problem/14889) | [스타트와 링크](baekjoon/14889.py)                     | 브루트 포스, 백트래킹, 비트 마스크                           |                                                              |
| [14890](https://www.acmicpc.net/problem/14890) | [경사로](baekjoon/14890.py)                            | 구현                                                         |                                                              |
| [15649](https://www.acmicpc.net/problem/15649) | [N과 M (1)](baekjoon/15649.py)                         | 브루트 포스                                                  |                                                              |
| [15658](https://www.acmicpc.net/problem/15658) | [연산자 끼워넣기 (2)](baekjoon/15658.py)               | 구현, 브루트 포스, 백트래킹                                  |                                                              |
| [15683](https://www.acmicpc.net/problem/15683) | [감시](baekjoon/15683.py)                              | 구현, 브루트 포스, 시뮬레이션                                | :alarm_clock: 시간 줄이기                                    |
| [15684](https://www.acmicpc.net/problem/15684) | [사다리 조작](baekjoon/15684.py)                       | 구현, 브루트포스, 백트래킹                                   |                                                              |
| [15685](https://www.acmicpc.net/problem/15685) | [드래곤 커브](baekjoon/15685.py)                       | [회전변환](https://ko.wikipedia.org/wiki/%ED%9A%8C%EC%A0%84%EB%B3%80%ED%99%98%ED%96%89%EB%A0%AC), 구현, 시뮬레이션 |                                                              |
| [15988](https://www.acmicpc.net/problem/15988) | [1, 2, 3 더하기 3](baekjoon/15988.py)                  | DP                                                           |                                                              |
| [15990](https://www.acmicpc.net/problem/15990) | [1, 2, 3 더하기 5](baekjoon/15990.py)                  | DP                                                           |                                                              |
| [16194](https://www.acmicpc.net/problem/16194) | [카드 구매하기 2](baekjoon/16194.py)                   | DP                                                           |                                                              |
| [16197](https://www.acmicpc.net/problem/16197) | [두 동전](baekjoon/16197.py)                           | 브루트 포스, 백트래킹                                        | BFS                                                          |
| [16198](https://www.acmicpc.net/problem/16198) | [에너지 모으기](baekjoon/16198.py)                     | 브루트 포스, 재귀                                            |                                                              |
| [16234](https://www.acmicpc.net/problem/16234) | [인구 이동](baekjoon/16234.py)                         | DFS, 구현, BFS, 시뮬레이션                                   | ~~:alarm_clock: 시간 줄이기~~ :heavy_check_mark:             |
| [16235](https://www.acmicpc.net/problem/16235) | [나무 재테크](baekjoon/16235.py)                       | 구현, 시뮬레이션                                             |                                                              |
| [16236](https://www.acmicpc.net/problem/16236) | [아기 상어](baekjoon/16236.py)                         | 구현, BFS, 시뮬레이션                                        |                                                              |
| [16637](https://www.acmicpc.net/problem/16637) | [괄호 추가하기](baekjoon/16637.py)                     | 브루트 포스                                                  |                                                              |
| [17070](https://www.acmicpc.net/problem/17070) | [파이프 옮기기 1](baekjoon/17070.py)                   | DP                                                           |                                                              |
| [17140](https://www.acmicpc.net/problem/17140) | [이차원 배열과 연산](baekjoon/17140.py)                | 구현, 시뮬레이션                                             |                                                              |
| [17142](https://www.acmicpc.net/problem/17142) | [연구소 3](baekjoon/17142.py)                          | BFS, 브루트포스                                              |                                                              |
| [17281](https://www.acmicpc.net/problem/17281) | [:baseball:](baekjoon/17281.py)                        | 구현, 브루트 포스                                            |                                                              |
| [17406](https://www.acmicpc.net/problem/17406) | [배열 돌리기 4](baekjoon/17406.py)                     | 구현, 브루트 포스                                            |                                                              |
| [17439](https://www.acmicpc.net/problem/17439) | [꽃집](baekjoon/201231_%EC%83%88%ED%95%B4/e.py)        | 브루트 포스, 백트래킹                                        | :memo: _2020-12-31 ​새해_<br />:alarm_clock: ​시간 초과<br />DP, 이분 탐색, Alien 트릭, 단조 큐를 이용한 최적화 |
| [17471](https://www.acmicpc.net/problem/17471) | [게리맨더링](baekjoon/17471.py)                        | DFS, 브루트 포스                                             |                                                              |
| [17472](https://www.acmicpc.net/problem/17472) | [다리 만들기 2](baekjoon/17472.py)                     | 구현, 브루트 포스, BFS, MST, 크루스칼                        |                                                              |
| [17779](https://www.acmicpc.net/problem/17779) | [게리맨더링 2](baekjoon/17779.py)                      | 구현, 브루트 포스, 시뮬레이션                                |                                                              |
| [17822](https://www.acmicpc.net/problem/17822) | [원판 돌리기](baekjoon/17822.py)                       | 구현, 시뮬레이션, DFS                                        |                                                              |
| [17837](https://www.acmicpc.net/problem/17837) | [새로운 게임 2](baekjoon/17837.py)                     | 구현, 시뮬레이션                                             |                                                              |
| [19238](https://www.acmicpc.net/problem/19238) | [스타트 택시](baekjoon/19238.py)                       | 구현, BFS, 시뮬레이션                                        |                                                              |
| [20055](https://www.acmicpc.net/problem/20055) | [컨베이어 벨트 위의 로봇](baekjoon/20055.py)           | 구현, 시뮬레이션                                             |                                                              |
| [20056](https://www.acmicpc.net/problem/20056) | [마법사 상어와 파이어볼](baekjoon/20056.py)            | 구현, 시뮬레이션                                             |                                                              |
| [20057](https://www.acmicpc.net/problem/20057) | [마법사 상어와 토네이도](baekjoon/20057.py)            | 구현, 시뮬레이션                                             |                                                              |
| [20058](https://www.acmicpc.net/problem/20058) | [마법사 상어와 파이어스톰](baekjoon/20058.py)          | 구현, DFS, 시뮬레이션                                        |                                                              |
| [20528](https://www.acmicpc.net/problem/20528) | [끝말잇기](baekjoon/201231_GoodByeBOJ2020/a.py)        | 문자열                                                       | :memo: _2020-12-31 Good Bye, BOJ 2020!_<br />애드 혹         |
| [20529](https://www.acmicpc.net/problem/20529) | [가장 가까운 세 사람의 심리적 거리](baekjoon/20529.py) | 브루트 포스, 비둘기집의 원리                                 | :memo: _2020-12-31 Good Bye, BOJ 2020!_                      |
| [21608](https://www.acmicpc.net/problem/21608) | [상어 초등학교](baekjoon/21608.py)                     | 구현                                                         |                                                              |
| [21610](https://www.acmicpc.net/problem/21610) | [마법사 상어와 비바라기](baekjoon/21610.py)            | 구현, 시뮬레이션                                             |                                                              |




## Programmers

### Level 1

| 문제                                                         | 문제 제목                                                    | 알고리즘        | 비고                                                 |
| ------------------------------------------------------------ | ------------------------------------------------------------ | --------------- | ---------------------------------------------------- |
| [1845](https://programmers.co.kr/learn/courses/30/lessons/1845) | [폰켓몬](programmers/level1/1845.py) |                 | :memo: _찾아라 프로그래밍 마에스터_                  |
| [12901](https://programmers.co.kr/learn/courses/30/lessons/12901) | 2016년 ([python](programmers/level1/12901.py)/[java](programmers/src/level1/Prob_12901.java)) |                 |                                                      |
| [12903](https://programmers.co.kr/learn/courses/30/lessons/12903) | 가운데 글자 가져오기 ([python](programmers/level1/12903.py)/[java](programmers/src/level1/Prob_12903.java)) |                 |                                                      |
| [12906](https://programmers.co.kr/learn/courses/30/lessons/12906) | 같은 숫자는 싫어 ([python](programmers/level1/12906.py)/[java](programmers/src/level1/Prob_12906.java)) |                 |                                                      |
| [12910](https://programmers.co.kr/learn/courses/30/lessons/12910) | [나누어 떨어지는 숫자 배열](programmers/level1/12910.py) |                 |                                                      |
| [12912](https://programmers.co.kr/learn/courses/30/lessons/12912) | [두 정수 사이의 합](programmers/level1/12912.py) |                 |                                                      |
| [12915](https://programmers.co.kr/learn/courses/30/lessons/12915) | [문자열 내 마음대로 정렬하기](programmers/level1/12915.py) |                 |                                                      |
| [12916](https://programmers.co.kr/learn/courses/30/lessons/12916) | [문자열 내 p와 y의 개수](programmers/level1/12916.py) |                 |                                                      |
| [12917](https://programmers.co.kr/learn/courses/30/lessons/12917) | [문자열 내림차순으로 배치하기](programmers/level1/12917.py) |                 |                                                      |
| [12918](https://programmers.co.kr/learn/courses/30/lessons/12918) | [문자열 다루기 기본](programmers/level1/12918.py) |                 |                                                      |
| [12919](https://programmers.co.kr/learn/courses/30/lessons/12919) | [서울에서 김서방 찾기](programmers/level1/12919.py) |                 |                                                      |
| [12921](https://programmers.co.kr/learn/courses/30/lessons/12921) | [소수 찾기](programmers/level1/12921.py) |                 |                                                      |
| [12922](https://programmers.co.kr/learn/courses/30/lessons/12922) | [수박수박수박수박수박수?](programmers/level1/12922.py) |                 |                                                      |
| [12925](https://programmers.co.kr/learn/courses/30/lessons/12925) | [문자열을 정수로 바꾸기](programmers/level1/12925.py) |                 |                                                      |
| [12926](https://programmers.co.kr/learn/courses/30/lessons/12926) | [시저 암호](programmers/level1/12926.py) |                 |                                                      |
| [12928](https://programmers.co.kr/learn/courses/30/lessons/12928) | [약수의 합](programmers/level1/12928.py) |                 |                                                      |
| [12930](https://programmers.co.kr/learn/courses/30/lessons/12930) | [이상한 문자 만들기](programmers/level1/12930.py) |                 |                                                      |
| [12931](https://programmers.co.kr/learn/courses/30/lessons/12931) | [자릿수 더하기](programmers/level1/12931.py) |                 |                                                      |
| [12932](https://programmers.co.kr/learn/courses/30/lessons/12932) | [자연수 뒤집어 배열로 만들기](programmers/level1/12932.py) |                 |                                                      |
| [12933](https://programmers.co.kr/learn/courses/30/lessons/12933) | [정수 내림차순으로 배치하기](programmers/level1/12933.py) |                 |                                                      |
| [12934](https://programmers.co.kr/learn/courses/30/lessons/12934) | [정수 제곱근 판별](programmers/level1/12934.py) |                 |                                                      |
| [12935](https://programmers.co.kr/learn/courses/30/lessons/12935) | 제일 작은 수 제거하기 ([python](programmers/level1/12935.py)/[java](programmers/src/level1/Prob_12935.java)) |                 |                                                      |
| [12937](https://programmers.co.kr/learn/courses/30/lessons/12937) | [짝수와 홀수](programmers/level1/12937.py) |                 |                                                      |
| [12940](https://programmers.co.kr/learn/courses/30/lessons/12940) | [최대공약수와 최소공배수](programmers/level1/12940.py) | 유클리드 호제법 |                                                      |
| [12943](https://programmers.co.kr/learn/courses/30/lessons/12943) | [콜라츠 추측](programmers/level1/12943.py) |                 |                                                      |
| [12944](https://programmers.co.kr/learn/courses/30/lessons/12944) | [평균 구하기](programmers/level1/12944.py) |                 |                                                      |
| [12947](https://programmers.co.kr/learn/courses/30/lessons/12947) | [하샤드 수](programmers/level1/12947.py) |                 |                                                      |
| [12948](https://programmers.co.kr/learn/courses/30/lessons/12948) | [핸드폰 번호 가리기](programmers/level1/12948.py) |                 |                                                      |
| [12950](https://programmers.co.kr/learn/courses/30/lessons/12950) | [행렬의 덧셈](programmers/level1/12950.py) |                 |                                                      |
| [12954](https://programmers.co.kr/learn/courses/30/lessons/12954) | [x만큼 간격이 있는 n개의 숫자](programmers/level1/12954.py) |                 |                                                      |
| [12969](https://programmers.co.kr/learn/courses/30/lessons/12969) | [직사각형 별찍기](programmers/level1/12969.py) |                 |                                                      |
| [12977](https://programmers.co.kr/learn/courses/30/lessons/12977) | [소수 만들기](programmers/level1/12977.py)                   |                 | :memo: _​Summer/Winter Coding(~2018)_                 |
| [12982](https://programmers.co.kr/learn/courses/30/lessons/12982) | [예산](programmers/level1/12982.py)                          |                 | :memo: _Summer/Winter Coding(~2018)_                 |
| [17681](https://programmers.co.kr/learn/courses/30/lessons/17681) | [[1차] 비밀지도](programmers/level1/17681.py)                |                 | :memo: _2018 KAKAO BLIND RECRUITMENT_                |
| [17682](https://programmers.co.kr/learn/courses/30/lessons/17682) | [[1차] 다트 게임](programmers/level1/17682.py)               |                 | :memo: _2018 KAKAO BLIND RECRUITMENT_                |
| [42576](https://programmers.co.kr/learn/courses/30/lessons/42576) | [완주하지 못한 선수](programmers/level1/42576.py)            | 해시            |                                                      |
| [42748](https://programmers.co.kr/learn/courses/30/lessons/42748) | [K번째수](programmers/level1/42748.py)                       | 정렬            |                                                      |
| [42840](https://programmers.co.kr/learn/courses/30/lessons/42840) | [모의고사](programmers/level1/42840.py)                      | 브루트 포스     |                                                      |
| [42862](https://programmers.co.kr/learn/courses/30/lessons/42862) | [체육복](programmers/level1/42862.py)                        | 탐욕법(Greedy)  |                                                      |
| [42889](https://programmers.co.kr/learn/courses/30/lessons/42889) | [실패율](programmers/level1/42889.py)                        |                 | :memo: _2019 KAKAO BLIND RECRUITMENT_                |
| [64061](https://programmers.co.kr/learn/courses/30/lessons/64061) | [크레인 인형뽑기 게임](programmers/level1/64061.py)          |                 | :memo: _2019 카카오 개발자 겨울 인턴십_              |
| [67256](https://programmers.co.kr/learn/courses/30/lessons/62756) | [[카카오 인턴] 키패드 누르기](programmers/level1/67256.py)   |                 | :memo: _2020 카카오 인턴십_                          |
| [68644](https://programmers.co.kr/learn/courses/30/lessons/68644) | [두 개 뽑아서 더하기](programmers/level1/68644.py)           |                 | :memo: _월간 코드 챌린지 시즌1_                      |
| [68935](https://programmers.co.kr/learn/courses/30/lessons/68935) | [3진법 뒤집기](programmers/level1/68935.py)                  |                 | :memo: _월간 코드 챌린지 시즌1_                      |
| [70128](https://programmers.co.kr/learn/courses/30/lessons/70128) | [내적](programmers/level1/70128.py)                          |                 | :memo: _월간 코드 챌린지 시즌1_                      |
| [76501](https://programmers.co.kr/learn/courses/30/lessons/76501) | [음양 더하기](programmers/level1/76501.py)                   |                 | :memo: _월간 코드 챌린지 시즌2_                      |
| [77484](https://programmers.co.kr/learn/courses/30/lessons/77484) | [로또의 최고 순위와 최저 순위](programmers/level1/77484.py)  |                 | :memo: _2021 Dev-Matching: 웹 백엔드 개발자(상반기)_ |
| [77884](https://programmers.co.kr/learn/courses/30/lessons/77884) | [약수의 개수와 덧셈](programmers/level1/77884.py)            |                 | :memo: _월간 코드 챌린지 시즌2_                      |
| [81301](https://programmers.co.kr/learn/courses/30/lessons/81301) | [숫자 문자열과 영단어](programmers/level1/81301.py)          |                 | :memo: _2021 카카오 채용연계형 인턴십_               |
| [82612](https://programmers.co.kr/learn/courses/30/lessons/82612) | [부족한 금액 계산하기](programmers/level1/82612.py)          |                 | :memo: _위클리 챌린지  (1주차)_                      |
| [83201](https://programmers.co.kr/learn/courses/30/lessons/83201) | [상호 평가](programmers/level1/83201.py)                     |                 | :memo: _위클리 챌린지  (2주차)_                      |



### Level 2


| 문제                                                         | 문제 제목                                                    | 알고리즘                                                     | 비고                                                 |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ---------------------------------------------------- |
| [1844](https://programmers.co.kr/learn/courses/30/lessons/1844) | [게임 맵 최단거리](programmers/level2/1844.py) | BFS                                                          | :memo: _찾아라 프로그래밍 마에스터_                  |
| [12899](https://programmers.co.kr/learn/courses/30/lessons/12899) | [124 나라의 숫자](programmers/level2/12899.py) |                                                              |                                                      |
| [12905](https://programmers.co.kr/learn/courses/30/lessons/12905) | [가장 큰 정사각형 찾기](programmers/level2/12905.py) | DP                                                           |                                                      |
| [12909](https://programmers.co.kr/learn/courses/30/lessons/12909) | [올바른 괄호](programmers/level2/12909.py) | 스택                                                         |                                                      |
| [12911](https://programmers.co.kr/learn/courses/30/lessons/12911) | [다음 큰 숫자](programmers/level2/12911.py) |                                                              |                                                      |
| [12913](https://programmers.co.kr/learn/courses/30/lessons/12913) | [땅따먹기](programmers/level2/12913.py) | DP                                                           |                                                      |
| [12924](https://programmers.co.kr/learn/courses/30/lessons/12924) | [숫자의 표현](programmers/level2/12924.py) |                                                              |                                                      |
| [12939](https://programmers.co.kr/learn/courses/30/lessons/12939) | [최댓값과 최솟값](programmers/level2/12939.py) |                                                              |                                                      |
| [12941](https://programmers.co.kr/learn/courses/30/lessons/12941) | [최솟값 만들기](programmers/level2/12941.py) |                                                              |                                                      |
| [12945](https://programmers.co.kr/learn/courses/30/lessons/12945) | [피보나치 수](programmers/level2/12945.py) | 메모이제이션                                                 |                                                      |
| [12949](https://programmers.co.kr/learn/courses/30/lessons/12949) | [행렬의 곱셈](programmers/level2/12949.py) |                                                              |                                                      |
| [12951](https://programmers.co.kr/learn/courses/30/lessons/12951) | [JadenCase 문자열 만들기](programmers/level2/12951.py) |                                                              |                                                      |
| [12953](https://programmers.co.kr/learn/courses/30/lessons/12953) | [N개의 최소공배수](programmers/level2/12953.py) |                                                              |                                                      |
| [12973](https://programmers.co.kr/learn/courses/30/lessons/12973) | [짝지어 제거하기](programmers/level2/12973.py) | 스택                                                         | :memo: _2017 팁스타운_                               |
| [12978](https://programmers.co.kr/learn/courses/30/lessons/12978) | [배달](programmers/level2/12978.py) | 다익스트라, 우선순위 큐                                      | :memo: _Summer/Winter Coding(~2018)_                 |
| [12980](https://programmers.co.kr/learn/courses/30/lessons/12980) | [점프와 순간 이동](programmers/level2/12980.py) |                                                              | :memo: _Summer/Winter Coding(~2018)_                 |
| [12981](https://programmers.co.kr/learn/courses/30/lessons/12981) | [영어 끝말잇기](programmers/level2/12981.py) |                                                              | :memo: _Summer/Winter Coding(~2018)_                 |
| [12985](https://programmers.co.kr/learn/courses/30/lessons/12985) | [예상 대진표](programmers/level2/12985.py) |                                                              | :memo: _2017 팁스타운_                               |
| [17677](https://programmers.co.kr/learn/courses/30/lessons/17677) | [[1차] 뉴스 클러스터링](programmers/level2/17677.py) |                                                              | :memo: _2018 KAKAO BLIND RECRUITMENT_                |
| [17679](https://programmers.co.kr/learn/courses/30/lessons/17679) | [[1차] 프렌즈4블록](programmers/level2/17679.py) |                                                              | :memo: _2018 KAKAO BLIND RECRUITMENT_                |
| [17680](https://programmers.co.kr/learn/courses/30/lessons/17680) | [[1차] 캐시](programmers/level2/17680.py) | 큐                                                           | :memo: _2018 KAKAO BLIND RECRUITMENT_                |
| [17683](https://programmers.co.kr/learn/courses/30/lessons/17683) | [[3차] 방금그곡](programmers/level2/17683.py) |                                                              | :memo: _2018 KAKAO BLIND RECRUITMENT_                |
| [17684](https://programmers.co.kr/learn/courses/30/lessons/17684) | [[3차] 압축](programmers/level2/17684.py) |                                                              | :memo: _2018 KAKAO BLIND RECRUITMENT_                |
| [17686](https://programmers.co.kr/learn/courses/30/lessons/17686) | [[3차] 파일명 정렬](programmers/level2/17686.py) |                                                              | :memo: _2018 KAKAO BLIND RECRUITMENT_                |
| [17687](https://programmers.co.kr/learn/courses/30/lessons/17687) | [[3차] n진수 게임](programmers/level2/17687.py) |                                                              | :memo: _2018 KAKAO BLIND RECRUITMENT_                |
| [42577](https://programmers.co.kr/learn/courses/30/lessons/42577) | [전화번호 목록](programmers/level2/42577.py) | 해시                                                         |                                                      |
| [42578](https://programmers.co.kr/learn/courses/30/lessons/42578) | [위장](programmers/level2/42578.py) | 해시                                                         |                                                      |
| [42583](https://programmers.co.kr/learn/courses/30/lessons/42583) | [다리를 지나는 트럭](programmers/level2/42583.py) | 스택/큐                                                      |                                                      |
| [42584](https://programmers.co.kr/learn/courses/30/lessons/42584) | [주식가격](programmers/level2/42584.py) | 스택/큐                                                      |                                                      |
| [42586](https://programmers.co.kr/learn/courses/30/lessons/42586) | [기능개발](programmers/level2/42586.py) | 스택/큐                                                      |                                                      |
| [42587](https://programmers.co.kr/learn/courses/30/lessons/42587) | [프린터](programmers/level2/42587.py) | 스택/큐                                                      |                                                      |
| [42626](https://programmers.co.kr/learn/courses/30/lessons/42626) | [더 맵게](programmers/level2/42626.py) | 힙(Heap)                                                     |                                                      |
| [42746](https://programmers.co.kr/learn/courses/30/lessons/42746) | [가장 큰 수](programmers/level2/42746.py) | ([블로그](https://yurimkoo.github.io/algorithm/2020/06/07/greatest-number.html) 참고) |                                                      |
| [42747](https://programmers.co.kr/learn/courses/30/lessons/42747) | [H-Index](programmers/level2/42747.py) | 정렬                                                         |                                                      |
| [42839](https://programmers.co.kr/learn/courses/30/lessons/42839) | [소수 찾기](programmers/level2/42839.py) | 브루트 포스                                                  |                                                      |
| [42842](https://programmers.co.kr/learn/courses/30/lessons/42842) | [카펫](programmers/level2/42842.py) | 완전탐색                                                     |                                                      |
| [42860](https://programmers.co.kr/learn/courses/30/lessons/42860) | [조이스틱](programmers/level2/42860.py) | 탐욕법(Greedy)                                               |                                                      |
| [42883](https://programmers.co.kr/learn/courses/30/lessons/42883) | [큰 수 만들기](programmers/level2/42883.py) | 탐욕법(Greedy)                                               |                                                      |
| [42885](https://programmers.co.kr/learn/courses/30/lessons/42885) | [구명보트](programmers/level2/42885.py) | 탐욕법(Greedy)                                               |                                                      |
| [42888](https://programmers.co.kr/learn/courses/30/lessons/42888) | [오픈채팅방](programmers/level2/42888.py) |                                                              | :memo: _2019 KAKAO BLIND RECRUITMENT_                |
| [42890](https://programmers.co.kr/learn/courses/30/lessons/42890) | [후보키](programmers/level2/42890.py) |                                                              | :memo: _2019 KAKAO BLIND RECRUITMENT_                |
| [43165](https://programmers.co.kr/learn/courses/30/lessons/43165) | [타겟 넘버](programmers/level2/43165.py) | 깊이/너비 우선 탐색(DFS/BFS)                                 |                                                      |
| [49993](https://programmers.co.kr/learn/courses/30/lessons/49993) | [스킬트리](programmers/level2/49993.py) |                                                              | :memo: _Summer/Winter Coding(~2018)_                 |
| [49994](https://programmers.co.kr/learn/courses/30/lessons/49994) | [방문 길이](programmers/level2/49994.py) |                                                              | :memo: _Summer/Winter Coding(~2018)_                 |
| [60057](https://programmers.co.kr/learn/courses/30/lessons/60057) | [문자열 압축](programmers/level2/60057.py) |                                                              | :memo: _2020 KAKAO BLIND RECRUITMENT_                |
| [60058](https://programmers.co.kr/learn/courses/30/lessons/60058) | [괄호 변환](programmers/level2/60058.py) |                                                              | :memo: _2020 KAKAO BLIND RECRUITMENT_                |
| [62048](https://programmers.co.kr/learn/courses/30/lessons/62048) | [멀쩡한 사각형](programmers/level2/62048.py) | 유클리드 호제법                                              | :memo: _Summer/Winter Coding(2019)_                  |
| [64065](https://programmers.co.kr/learn/courses/30/lessons/64065) | [튜플](programmers/level2/64065.py) |                                                              | :memo: _2019 카카오 개발자 겨울 인턴십_              |
| [67257](https://programmers.co.kr/learn/courses/30/lessons/67257) | [[카카오 인턴] 수식 최대화](programmers/level2/67257.py) |                                                              | :memo: _2020 카카오 인턴십_                          |
| [68645](https://programmers.co.kr/learn/courses/30/lessons/68645) | [삼각 달팽이](programmers/level2/68645.py) |                                                              | :memo: _월간 코드 챌린지 시즌1_                      |
| [68936](https://programmers.co.kr/learn/courses/30/lessons/68936) | [쿼드압축 후 개수 세기](programmers/level2/68936.py) |                                                              | :memo: _월간 코드 챌린지 시즌1_                      |
| [70129](https://programmers.co.kr/learn/courses/30/lessons/70129) | [이진 변환 반복하기](programmers/level2/70129.py) |                                                              | :memo: _월간 코드 챌린지 시즌1_                      |
| [72411](https://programmers.co.kr/learn/courses/30/lessons/72411) | [메뉴 리뉴얼](programmers/level2/72411.py) |                                                              | :memo: _2021 KAKAO BLIND RECRUITMENT_                |
| [72412](https://programmers.co.kr/learn/courses/30/lessons/72412) | [순위 검색](programmers/level2/72412.py) | 이진 탐색                                                    | :memo: _2021 KAKAO BLIND RECRUITMENT_                |
| [76502](https://programmers.co.kr/learn/courses/30/lessons/76502) | [괄호 회전하기](programmers/level2/76502.py) | 스택                                                         | :memo: _월간 코드 챌린지 시즌2_                      |
| [77485](https://programmers.co.kr/learn/courses/30/lessons/77485) | [행렬 테두리 회전하기](programmers/level2/77485.py) |                                                              | :memo: _2021 Dev-Matching: 웹 백엔드 개발자(상반기)_ |
| [77885](https://programmers.co.kr/learn/courses/30/lessons/77885) | [2개 이하로 다른 비트](programmers/level2/77885.py) |                                                              | :memo: _월간 코드 챌린지 시즌2_                      |
| [81302](https://programmers.co.kr/learn/courses/30/lessons/81302) | [거리두기 확인하기](programmers/level2/81302.py) | BFS                                                          | :memo: _2021 카카오 채용연계형 인턴십_               |



### Level 3

| 문제                                                         | 문제 제목                                                    | 알고리즘                     | 비고                        |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ---------------------------- | --------------------------- |
| [12900](https://programmers.co.kr/learn/courses/30/lessons/12900) | [2 x n 타일링](programmers/level3/12900.py) | DP                           |                             |
| [42579](https://programmers.co.kr/learn/courses/30/lessons/42579) | [베스트앨범](programmers/level3/42579.py) | 해시                         |                             |
| [42627](https://programmers.co.kr/learn/courses/30/lessons/42627) | [디스크 컨트롤러](programmers/level3/42627.py) | 힙(Heap)                     |                             |
| [42628](https://programmers.co.kr/learn/courses/30/lessons/42628) | [이중우선순위큐](programmers/level3/42628.py) | 힙(Heap)                     |                             |
| [43162](https://programmers.co.kr/learn/courses/30/lessons/43162) | [네트워크](programmers/level3/43162.py) | 깊이/너비 우선 탐색(DFS/BFS) |                             |
| [43163](https://programmers.co.kr/learn/courses/30/lessons/43163) | [단어 변환](programmers/level3/43163.py) | 깊이/너비 우선 탐색(DFS/BFS) |                             |
| [43164](https://programmers.co.kr/learn/courses/30/lessons/43164) | [여행경로](programmers/level3/43164.py) | 깊이/너비 우선 탐색(DFS/BFS) |                             |
| [43238](https://programmers.co.kr/learn/courses/30/lessons/43238) | [입국심사](programmers/level3/43238.py) | 이분탐색                     |                             |
| [67258](https://programmers.co.kr/learn/courses/30/lessons/67258) | [보석 쇼핑](programmers/level3/67258.py) | 해시, 투 포인터              | :memo: _2020 카카오 인턴십_ |



### Level 4

| 문제                                                         | 문제 제목                                                    | 알고리즘 | 비고 |
| ------------------------------------------------------------ | ------------------------------------------------------------ | -------- | ---- |
| [43236](https://programmers.co.kr/learn/courses/30/lessons/43236) | [징검다리](programmers/level4/43236.py) | 이분탐색 |      |



### SQL

| 문제                                                         | 문제 제목                                                   | 유형                           | 비고                                                 |
| ------------------------------------------------------------ | ----------------------------------------------------------- | ------------------------------ | ---------------------------------------------------- |
| [59034](https://programmers.co.kr/learn/courses/30/lessons/59034) | [모든 레코드 조회하기](programmers/sql/59034.sql)           | SELECT                         |                                                      |
| [59035](https://programmers.co.kr/learn/courses/30/lessons/59035) | [역순 정렬하기](programmers/sql/59035.sql)                  | SELECT                         |                                                      |
| [59036](https://programmers.co.kr/learn/courses/30/lessons/59036) | [아픈 동물 찾기](programmers/sql/59036.sql)                 | SELECT                         |                                                      |
| [59037](https://programmers.co.kr/learn/courses/30/lessons/59037) | [어린 동물 찾기](programmers/sql/59037.sql)                 | SELECT                         |                                                      |
| [59038](https://programmers.co.kr/learn/courses/30/lessons/59038) | [최솟값 구하기](programmers/sql/59038.sql)                  | SUM, MAX, MIN                  |                                                      |
| [59039](https://programmers.co.kr/learn/courses/30/lessons/59039) | [이름이 없는 동물의 아이디](programmers/sql/59039.sql)      | IS NULL                        |                                                      |
| [59040](https://programmers.co.kr/learn/courses/30/lessons/59040) | [고양이와 개는 몇 마리 있을까](programmers/sql/59040.sql)   | GROUP BY                       |                                                      |
| [59041](https://programmers.co.kr/learn/courses/30/lessons/59041) | [동명 동물 수 찾기](programmers/sql/59041.sql)              | GROUP BY                       |                                                      |
| [59042](https://programmers.co.kr/learn/courses/30/lessons/59042) | [없어진 기록 찾기](programmers/sql/59042.sql)               | JOIN                           |                                                      |
| [59043](https://programmers.co.kr/learn/courses/30/lessons/59043) | [있었는데요 없었습니다](programmers/sql/59043.sql)          | JOIN                           |                                                      |
| [59044](https://programmers.co.kr/learn/courses/30/lessons/59044) | [오랜 기간 보호한 동물(1)](programmers/sql/59044.sql)       | JOIN                           |                                                      |
| [59045](https://programmers.co.kr/learn/courses/30/lessons/59045) | [보호소에서 중성화한 동물](programmers/sql/59045.sql)       | JOIN, LIKE                     |                                                      |
| [59046](https://programmers.co.kr/learn/courses/30/lessons/59046) | [루시와 엘라 찾기](programmers/sql/59046.sql)               | String, Date                   |                                                      |
| [59047](https://programmers.co.kr/learn/courses/30/lessons/59047) | [이름에 el이 들어가는 동물 찾기](programmers/sql/59047.sql) | String, Date                   |                                                      |
| [59403](https://programmers.co.kr/learn/courses/30/lessons/59403) | [동물의 아이디와 이름](programmers/sql/59403.sql)           | SELECT                         |                                                      |
| [59404](https://programmers.co.kr/learn/courses/30/lessons/59404) | [여러 기준으로 정렬하기](programmers/sql/59404.sql)         | SELECT, ORDER BY               |                                                      |
| [59405](https://programmers.co.kr/learn/courses/30/lessons/59405) | [상위 n개 레코드](programmers/sql/59405.sql)                | LIMIT, SELECT                  |                                                      |
| [59406](https://programmers.co.kr/learn/courses/30/lessons/59406) | [동물 수 구하기](programmers/sql/59406.sql)                 | COUNT, SUM, MAX, MIN           |                                                      |
| [59407](https://programmers.co.kr/learn/courses/30/lessons/59407) | [이름이 있는 동물의 아이디](programmers/sql/59407.sql)      | IS NULL                        |                                                      |
| [59408](https://programmers.co.kr/learn/courses/30/lessons/59408) | [중복 제거하기](programmers/sql/59408.sql)                  | COUNT, DISTINCT, SUM, MAX, MIN |                                                      |
| [59409](https://programmers.co.kr/learn/courses/30/lessons/59409) | [중성화 여부 파악하기](programmers/sql/59409.sql)           | String, Date                   |                                                      |
| [59410](https://programmers.co.kr/learn/courses/30/lessons/59410) | [NULL 처리하기](programmers/sql/59410.sql)                  | IS NULL                        |                                                      |
| [59411](https://programmers.co.kr/learn/courses/30/lessons/59411) | [오랜 기간 보호한 동물(2)](programmers/sql/59411.sql)       | String, Date                   |                                                      |
| [59412](https://programmers.co.kr/learn/courses/30/lessons/59412) | [입양 시각 구하기(1)](programmers/sql/59412.sql)            | GROUP BY                       |                                                      |
| [59413](https://programmers.co.kr/learn/courses/30/lessons/59413) | [입양 시각 구하기(2)](programmers/sql/59413.sql)            | GROUP BY, WITH RECURSIVE       |                                                      |
| [59414](https://programmers.co.kr/learn/courses/30/lessons/59414) | [DATETIME에서 DATE로 형 변환](programmers/sql/59414.sql)    | String, Date                   |                                                      |
| [59415](https://programmers.co.kr/learn/courses/30/lessons/59415) | [최댓값 구하기](programmers/sql/59415.sql)                  | SUM, MAX, MIN                  |                                                      |
| [62284](https://programmers.co.kr/learn/courses/30/lessons/62284) | [우유와 요거트가 담긴 장바구니](programmers/sql/62284.sql)  | GROUP BY, DISTINCT             | :memo: _Summer/Winter Coding(2019)_                  |
| [77487](https://programmers.co.kr/learn/courses/30/lessons/77487) | [헤비 유저가 소유한 장소](programmers/sql/77487.sql)        | 서브쿼리                       | :memo: _2021 Dev-Matching: 웹 백엔드 개발자(상반기)_ |

