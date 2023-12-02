import numpy as np

np.random.seed(74321)
def generate_proficiency(data_ids):
    proficiencies = np.random.beta(4, 2.5, len(data_ids))*10
    return np.round(proficiencies, 1)

data = generate_proficiency(np.arange(0, 1000))
print(data)
print(np.mean(data))
print("0-1: ", np.sum(data < 1))
print("1-2: ", np.sum((data >= 1) & (data < 2)))
print("2-3: ", np.sum((data >= 2) & (data < 3)))
print("3-4: ", np.sum((data >= 3) & (data < 4)))
print("4-5: ", np.sum((data >= 4) & (data < 5)))
print("5-6: ", np.sum((data >= 5) & (data < 6)))
print("6-7: ", np.sum((data >= 6) & (data < 7)))
print("7-8: ", np.sum((data >= 7) & (data < 8)))
print("8-9: ", np.sum((data >= 8) & (data < 9)))
print("9-10: ", np.sum((data >= 9) & (data < 10)))

