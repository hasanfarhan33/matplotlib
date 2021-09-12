import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 11)
y = x ** 2
# plt.plot(x, y)
# plt.show()
#
# plt.subplot(1, 2, 1)
# plt.plot(x, y, 'r')
#
# plt.subplot(1, 2, 2)
# plt.plot(y, x, 'b')
# plt.show()

# Object Oriented Method
# fig = plt.figure()
# axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# axes.plot(x, y)
# axes.set_xlabel("X Label")
# axes.set_ylabel("Y Label")
# axes.set_title("Title")
# plt.show()

# fig = plt.figure()
# axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])
# axes1.plot(x, y)
# axes2.plot(y, x)
# axes2.set_title("Smaller Plot")
# axes1.set_title("Larger Plot")

# Creates multiple axes automatically based on number of rows and columns
# fig, axes = plt.subplots(nrows=1, ncols=2)
# plt.tight_layout()
# axes.plot(x, y)
# for current in axes:
#     current.plot(x, y)

# FIGURE SIZE AND DPI
# fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(8,4))
#
# axes[0].plot(x, y)
# axes[1].plot(y, x)
# plt.tight_layout()

# fig.savefig('my_picture.png', dpi = 200)


# fig = plt.figure()
# ax = fig.add_axes([0.1, 0.1, 0.9, 0.9])
# ax.plot(x, x**2, label="X Squared")
# ax.plot(x, x**3, label="X Cubed")
# ax.plot(x, x, label="X")
# ax.legend(loc = "best")
# ax.set_title("Title")
# ax.set_ylabel("Y Label")
# ax.set_xlabel("X Label")


# PLOT APPEARANCE
fig = plt.figure()
ax = fig.add_axes([0.05, 0.05, 0.95, 0.95])
ax.set_xlim([0, 1])
ax.set_ylim([0, 2])
ax.plot(x, y, color='green', lw=1, linestyle="-", marker='x') #Can use HEX code as a color



plt.show()