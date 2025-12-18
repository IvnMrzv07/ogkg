import matplotlib.pyplot as plt

point_x = []
point_y = []
file_name = 'DS8.txt'

with open(file_name, 'r') as f:
    for line in f:
        l = line.split()
        point_x.append(int(l[0]))
        point_y.append(int(l[1]))

plt.figure(figsize=(9.6, 5.4), dpi=100)
plt.scatter(point_x, point_y, c='black', s=10, marker='.')
plt.axis('equal')
plt.grid(True, linestyle='--', alpha=0.3)
plt.xlabel("X")
plt.ylabel("Y")

# plt.axis('off')  #координатну сітку можна прибрати, для отримання чистого зображення

OUTPUT_IMAGE = 'result2.png'
plt.savefig(OUTPUT_IMAGE)

plt.show()