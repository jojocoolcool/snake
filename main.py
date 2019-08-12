from displayer import Displayer
from wall import Wall
from snake import Snake
import time
import threading
from bug import Bug
import sys

displayer = Displayer()  # 创建显示管理类对象
wall = Wall()  # 创建墙的对象
snake = Snake()  # 创建蛇的对象
bug = Bug(snake.points)  # 创建虫子

running = True


class InputThread(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        global running, snake  # 引入声明在函数外的变量
        while True:  # sys.stdin.readline( ) sys.stdin.getch()
            c = str(sys.stdin())
            print(c)
            if c == "b'q'":
                running = False
            elif c == "b'w'":
                snake.set_toward("UP")
            elif c == "b's'":
                snake.set_toward("DOWN")
            elif c == "b'a'":
                snake.set_toward("LEFT")
            elif c == "b'd'":
                snake.set_toward("RIGHT")


input_thread = InputThread()
input_thread.start()

while True:
    # 蛇动
    death = snake.action(bug, wall.points)
    if death:
        print("\n小蛇蛇冒险失败!!!请按Q退出。\n")
        break

    # 将墙的坐标导入到 displayer
    displayer.extend_points(wall.points)
    displayer.extend_points(snake.points)
    displayer.extend_points(bug.point)

    # 绘制图像
    displayer.draw_graphics(snake.score)  # 返回分数

    # 清空这一帧数据
    displayer.clear()
    time.sleep(snake.sleep_time)  # 时间让蛇给他
