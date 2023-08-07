import matplotlib.pyplot as plt

input_values = list(range(1, 11))
squares = [i ** 2 for i in range(1, 11)]

plt.plot(input_values, squares, linewidth=5)

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.tick_params(axis='both', labelsize=14)

plt.show()
