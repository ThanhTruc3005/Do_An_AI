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

class QLearningAgent: 
    def __init__(self, n_states, n_actions, alpha=0.1, gamma=0.9, epsilon=0.9): #Hàm khởi tạo cho agent, nhận vào số lượng trạng thái, số lượng hành động, tốc độ học (alpha) và hệ số chiết khấu (gamma)
       self.q_table = np.zeros((n_states, n_actions)) 
       self.alpha = alpha
       self.gamma = gamma
       self.epsilon = epsilon
       self.n_actions = n_actions

    def choose_action(self, state):
        if random.uniform(0,1) < self.epsilon:
            return random.randint(0, self.n_actions - 1) 
        else:
            return np.argmax(self.q_table[state, :])
    def learn(self, state, action, reward, next_state, done):
        q_predict = self.q_table[state, action]
        if done:
            q_target = reward
        else:
            q_target = reward + self.gamma * np.max(self.q_table[next_state, :])
        self.q_table[state, action] += self.alpha * (q_target - q_predict)
if __name__ == "__main__":
    env = LineEnvironment(length=6)
    agent = QLearningAgent(n_states=6, n_actions=2)
    episodes = 20
    for episode in range(episodes):
        state = env.reset()
        done = False
        steps = 0
        while not done:
            env.render()
            action = agent.choose_action(state)
            next_state, reward, done = env.step(action)
            agent.learn(state, action, reward, next_state, done)
            state = next_state
            steps += 1
        print(f"\nEpisode {episode + 1}: Total steps = {steps}")
        agent.epsilon = max(0.1, agent.epsilon * 0.8)
        print("\nQUÁ TRÌNH HỌC KẾT THÚC!")
    print("\nBẢNG Q-TABLE CUỐI CÙNG:")
    print("Hàng là Trạng thái (0->5). Cột 0 là Trái, Cột 1 là Phải.")
    print(np.round(agent.q_table, 2))


    