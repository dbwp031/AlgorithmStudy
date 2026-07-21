def solution(triangle):
    # dp[i][j] = i번째 높이 j번째 순서 노드 위치에서의 최댓값
    width = len(triangle[-1])
    height = len(triangle)
    dp = [[0] * width for _ in range(height)]
    
    dp[0][0] = triangle[0][0]
    for h in range(1, height):
        for w in range(len(triangle[h])):
            cur = triangle[h][w]
            if w == 0:
                dp[h][w] = dp[h-1][w] + triangle[h][w]
            else:
                dp[h][w] = max(dp[h-1][w-1], dp[h-1][w])  + triangle[h][w]
    
    answer = max(dp[height-1])
    return answer