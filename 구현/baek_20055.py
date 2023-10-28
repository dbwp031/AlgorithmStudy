import sys
input = sys.stdin.readline

class Node:
    def __init__(self, endurance):
        self.isRobotExist = False
        self.endurance = endurance

n,k = map(int,input().split())
endurances = list(map(int,input().split()))
belt = []
upper_nodes = list(range(1,n+1))

belt.append(Node(-1))
for endurance in endurances:
    belt.append(Node(endurance))
def get_next_node(cur_node):
    result = None
    if cur_node == 2*n:
        result = 1
    else:
        result = cur_node + 1
    return result
                
def update_upper_nodes():
    upper_nodes.pop(-1)
    if upper_nodes[0] == 1:
        upper_nodes.insert(0,2*n)
    else:
        upper_nodes.insert(0,upper_nodes[0]-1)
def post_process():
    if belt[upper_nodes[-1]].isRobotExist:
        belt[upper_nodes[-1]].isRobotExist = False
    # print("===belt===")
    # for node in belt[1:]:
    #     print(node.isRobotExist, node.endurance)
    # print("=== upper_nodes===")
    # print(upper_nodes)
def belt_move_process():
    update_upper_nodes()
    post_process()
    
def robot_move_process():
    for upper_node_position in upper_nodes[::-1]:
        next_node_position = get_next_node(upper_node_position)
        if belt[upper_node_position].isRobotExist and not belt[next_node_position].isRobotExist and belt[next_node_position].endurance>0:
            belt[upper_node_position].isRobotExist = False
            belt[next_node_position].isRobotExist = True
            belt[next_node_position].endurance-=1
    post_process()
    
def put_robot_process():
    if belt[upper_nodes[0]].endurance > 0:
        belt[upper_nodes[0]].endurance -=1
        belt[upper_nodes[0]].isRobotExist = True
    post_process()
        
def isFinish(step):
    broken_node_count = 0
    for node in belt[1:]:
        if node.endurance <= 0:
            broken_node_count +=1
    # print(step, broken_node_count)
    return broken_node_count >= k
step = 0
while True:
    step +=1
    belt_move_process()
    robot_move_process()
    put_robot_process()
    if isFinish(step):
        print(step)
        break
