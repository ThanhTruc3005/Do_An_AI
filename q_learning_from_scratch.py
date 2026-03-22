import numpy as np
import random
import time
import os
# Bài này test cho robot đi từ trái sang phải, nếu đi sai sẽ bị phạt, nếu đi đúng sẽ được thưởng
class LineEnvironment: #Xây dựng môi trường
    def __init__(self, length=6): #Hàm định nghĩa độ dài
        self.length = length
        self.state = 0
        self.goal = length - 1 #Mục tiêu là vị trí cuối cùng
    def reset(self): #Hàm reset để khởi tạo lại môi trường
        self.state = 0
        return self.state
    def step(self, action): #Hàm step để thực hiện hành động và trả về trạng thái mới, phần thưởng và trạng thái kết thúc
        if action == 0:
            self.state = max(0, self.state - 1) #Nếu hành động là 0, robot sẽ đi sang trái, nhưng không được vượt quá vị trí 0  
        elif action == 1:
            self.state = min(self.length - 1, self.state + 1) #Nếu hành động là 1, robot sẽ đi sang phải, nhưng không được vượt quá vị trí cuối cùng
        if self.state == self.goal:
            reward = 10
            done = True
        else:
            reward = -1
            done = False
        return self.state, reward, done
    def render(self):
        env_str = ['-'] * self.length #Tạo một chuỗi để hiển thị môi trường, ban đầu là tất cả dấu '-'
        env_str[self.goal] = 'T' #Đặt mục tiêu là 'T'
        if self.state == self.goal:
            env_str[self.state] = 'W' #Nếu robot đạt được mục tiêu, hiển thị 'W' (Win)
        else:
            env_str[self.state] = 'R' #Nếu robot chưa đạt được mục tiêu, hiển thị 'R' (Robot)
        print('\r' + ''.join(env_str), end='') #In ra môi trường hiện tại, sử dụng '\r' để quay về đầu dòng và end='' để không xuống dòng
        time.sleep(0.1)