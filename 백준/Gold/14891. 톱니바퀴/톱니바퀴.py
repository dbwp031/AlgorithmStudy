topp = []

def turnRight(nums):
  return [nums[-1]] + nums[:7]
def turnLeft(nums):
  return nums[1:] + [nums[0]]

def move(root, target, dir):
  # print("====")
  # print(root, target, dir)

  # print("0: ", topp[0])
  # print("1: ", topp[1])
  # print("2: ", topp[2])
  # print("3: ", topp[3])
  # 오른쪽 전파
  if root <= target:
    nt = target + 1
    if nt == -1 or nt == 4:
      pass
    elif topp[target][2] == topp[nt][6]:
      pass
    else:
      move(root, nt, dir * -1)
  if root >= target:
    nt = target - 1
    if nt == -1 or nt == 4:
      pass
    elif topp[target][6] == topp[nt][2]:
      pass
    else:
      move(root, nt, dir * -1)

  if dir == -1: # left
    # print("turnLeft")
    topp[target] = turnLeft(topp[target])
  elif dir == 1:
    # print("turnRight")
    topp[target] = turnRight(topp[target])
for _ in range(4):
  topp.append(list(map(int,list(input()))))

k = int(input())
for _ in range(k):
  target, dir = map(int, input().split())
  move(target-1,target-1,dir)

# 1번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 1점
# 2번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 2점
# 3번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 4점
# 4번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 8점
score = 0
for i in range(4):
  score += topp[i][0] * 2 ** i
print(score)
