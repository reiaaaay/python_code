import matplotlib.pyplot as plt
x_list = []
y_list = []
with open("atoms.txt","r") as a:
	lines = a.readlines()
n = int(lines[0].strip())
print(f"the number of atoms is {n} ")
total_x = 0.0
for line in lines[1:]:
	parts = line.strip().split()
	atom_type = parts[0]
	x = float(parts[1])
	y = float(parts[2])
	z = float(parts[3])
	print (f"the atom is {atom_type}, {x}, {y}, {z}")
	total_x += x
	x_list.append(float(parts[1]))
	y_list.append(float(parts[2]))
plt.scatter(x_list, y_list, color="blue", label="Atoms")
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.title("The first plot")
plt.legend()
plt.grid(True)
plt.savefig("my_plot.png")
print ("图片已保存,画图完成")
print (f"平均x坐标为: {total_x/n}")

