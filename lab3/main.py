import matplotlib.pyplot as plt
import numpy as np

old_points = []
filename =  'DS8.txt'
OUTPUT_IMAGE = 'result3.png'

with open(filename, 'r') as f:
    for line in f:
        l = line.split()
        old_points.append([int(l[0]), int(l[1])])

a = 10*(8+1)

M1 = np.matrix([[1,0,-480],
                [0,1,-480],
                [0,0,1]])
M3 = np.matrix([[1,0,480],
                [0,1,480],
                [0,0,1]])
M2 = np.matrix([[np.cos(a), -np.sin(a), 0],
                [np.sin(a), np.cos(a), 0],
                [0, 0, 1]])
res_matrix = M3 @ M2 @ M1


for point in old_points: #додаємо z = 1, щоб скористатись нелінійною трансформацієї(перенос)
    point.append(1)

old_points_np = np.array(old_points).T

new_points = (res_matrix @ old_points_np).T.tolist()

with open('new_DS8.txt', 'w') as f:
    for point in new_points:
        f.write(f'{point[0]} {point[1]}')



x_cords2 = [point[0] for point in new_points]
y_cords2 = [point[1] for point in new_points]

x_cords1 = [point[0] for point in old_points]
y_cords1 = [point[1] for point in old_points]

plt.figure(figsize=(9.6, 5.4), dpi=100)
plt.axis('equal')
plt.grid(True, linestyle='--', alpha=0.3)
plt.xlim(0, 1000)
plt.ylim(0, 1000)

plt.scatter(x_cords2, y_cords2, s = 1, marker = '.')
plt.scatter(x_cords1, y_cords1, c = 'red', s = 1, marker = '.')
# plt.scatter(x_list, y_list, c = 'black', s = 10, marker = '.')

# plt.axis('off')
plt.savefig(OUTPUT_IMAGE)
plt.show()



