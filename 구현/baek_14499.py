import sys
input = sys.stdin.readline

EAST = 1
WEST = 2
NORTH = 3
SOUTH = 4

n,m,x,y,k = map(int,input().split())
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))

orders = list(map(int,input().split()))

class Dice:
    def __init__(self):
        self.front = 0
        self.back = 0
        self.left = 0
        self.right = 0
        self.up = 0
        self.down = 0
    def roll(self, order):
        if order == EAST: self.roll_right()
        elif order == WEST: self.roll_left()
        elif order == SOUTH: self.roll_down()
        elif order == NORTH: self.roll_up()
        self.copy_or_paste()
        
    def roll_left(self):
        global x,y
        tmp = self.left
        self.left = self.up
        self.up = self.right
        self.right = self.down
        self.down = tmp
        y-=1
    def roll_right(self):
        global x,y

        tmp = self.right
        self.right = self.up
        self.up = self.left
        self.left = self.down
        self.down = tmp
        y+=1
    def roll_up(self):
        global x,y

        tmp = self.up
        self.up = self.front
        self.front = self.down
        self.down = self.back
        self.back = tmp
        x-=1
    def roll_down(self):
        global x,y

        tmp = self.up
        self.up = self.back
        self.back = self.down
        self.down = self.front
        self.front = tmp
        x+=1
    def copy_or_paste(self):
        global x,y

        if board[x][y] == 0:
            board[x][y] = self.down
        else:
            self.down = board[x][y]
            board[x][y] = 0

def is_valid_order(order):
    if order == EAST:
        return y < m-1
    elif order == WEST:
        return y > 0
    elif order == NORTH:
        return x > 0
    elif order == SOUTH:
        return x < n-1

dice = Dice()

for i, order in enumerate(orders):
    if is_valid_order(order):
        dice.roll(order)
        print(dice.up)
    # else:
    #     print(f"#{i} - {x},{y}")
   
