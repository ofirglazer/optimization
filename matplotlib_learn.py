import matplotlib.pyplot as plt

names = ['A', 'B', 'C', 'D']
salaries = [100, 150, 120, 170]
plt.bar(names, salaries, color='green')
plt.plot(names, salaries, color='red')
plt.show()