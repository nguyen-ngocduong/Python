import random
import numpy as np

states = ['S0', 'S1', 'S2', 'S3', 'S4']
actions = ['A0', 'A1', 'A2', 'A3']
q_table = np.zeros((len(states), len(actions)))

# Tham số
learning_rate = 0.1
discount_factor = 0.99
epsilon = 0.1  # Tỷ lệ khám phá

# Hàm để chọn hành động dựa trên định luật Epsilon-Greedy
def choose_action(state_index):
    if random.uniform(0, 1) < epsilon:
        return random.randint(0, len(actions) - 1)  # Khám phá
    else:
        return np.argmax(q_table[state_index])  # Khai thác

# Mô phỏng quá trình học
for episode in range(1000):  # Chạy nhiều episode
    state_index = 0  # Bắt đầu từ trạng thái S0
    steps = 0
    
    while state_index != 2 and steps < 5:  # Dừng nếu đạt S2 hoặc vượt quá 5 bước
        action_index = choose_action(state_index)
        
        # Giả định: xác định trạng thái tiếp theo và phần thưởng
        # (Sẽ cần được điều chỉnh dựa trên quy tắc chuyển trạng thái thực tế)
        if action_index == 0:  # Di chuyển lên
            next_state_index = state_index - 1  # Ví dụ
        elif action_index == 1:  # Di chuyển xuống
            next_state_index = state_index + 1  # Ví dụ
        elif action_index == 2:  # Di chuyển trái
            next_state_index = state_index - 1  # Ví dụ
        elif action_index == 3:  # Di chuyển phải
            next_state_index = state_index + 1  # Ví dụ
        
        # Giả định phần thưởng
        if next_state_index == 2:
            reward = 10  # Đến phô mai lớn
        elif next_state_index == 3:
            reward = -10  # Đến chất độc
        else:
            reward = -1  # Phần thưởng nhỏ cho các trạng thái khác
        
        # Cập nhật Q-value
        q_table[state_index, action_index] += learning_rate * (
            reward + discount_factor * np.max(q_table[next_state_index]) - q_table[state_index, action_index]
        )
        
        # Chuyển trạng thái
        state_index = next_state_index
        steps += 1

print("Q-table:")
print(q_table)