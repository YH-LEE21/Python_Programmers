def solution(a, b, g, s, w, t):
    answer = int(10e9) * int(10e5) * 4
    n = len(g)  # 도시의 수
    # 이진 탐색
    start = 0
    end = int(10e9) * int(10e5) * 4
    while start <= end:
        mid = (start + end) // 2
        total_g, total_s, total_w = 0, 0, 0  # mid 시간 동안 옮긴 총 광물의 무게
        for i in range(n):
            # mid 시간 동안 가능한 왕복 횟수
            move_cnt = mid // (t[i] * 2)
            if (mid % (t[i] * 2)) >= t[i]:  # 편도로 한 번 더 갈 수 있을 경우
                move_cnt += 1
            # 옮길 수 있는 광물의 양
            total_g += move_cnt * w[i] if move_cnt * w[i] < g[i] else g[i]
            total_s += move_cnt * w[i] if move_cnt * w[i] < s[i] else s[i]
            total_w += move_cnt * w[i] if move_cnt * w[i] < g[i] + s[i] else g[i] + s[i]
        # mid 시간 내에 주어진 광물을 모두 전달할 수 있는지 확인
        if total_g >= a and total_s >= b and total_w >= a + b:
            answer = min(answer, mid)
            end = mid - 1
        else:
            start = mid + 1

    return answer