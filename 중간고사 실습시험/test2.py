dice_combinations = [(i, j, k) for i in range(1, 13) for j in range(1, 13) for k in range(1, 13) if 10 <= i + j + k <= 30]
print(dice_combinations)