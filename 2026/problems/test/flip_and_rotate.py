# i,j -> i, (N-1)-j
# 각 행을 reverse하면 된다.
def flip_horizontal(m): 
	return list(col[::-1] for col in m)
	
# 각 열을 reverse하면 된다.
def flip_vertical(m):
	return m[::-1]
# i,j -> j,i
# zip을 사용해서 각 열단위로 묶기
def transpose(m):
	return list(list(col) for col in zip(*m))

# i, j -> j, N-1-i
# 시계방향 = 전치 + 좌우 뒤집기
def rot_cw(m):
	return [list(col[::-1]) for col in zip(*m)]

# 반시계방향 = 전치 + 수직 뒤집기
def rot_ccw(m):
	return [list(col) for col in zip(*m)][::-1]
	