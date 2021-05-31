import matplotlib.pyplot as plt
names=['Yamkela', 'Jason', 'Brent', 'Shuaib', 'Devin']
test_marks= [99,  80, 75, 70, 85]
x_pos = [i for i, _ in enumerate(names)] #labels on the x-axis
#labeling and visuals

plt.bar(x_pos, test_marks, color='orange')
plt.xlabel("python test")
plt.ylabel("test_marks")
plt.title("Test")
plt.xticks(x_pos, names)
plt.show()
