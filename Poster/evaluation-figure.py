import numpy as np
import matplotlib.pyplot as plt

# Data
labels = ['MPBoot-Orig', 'MPBoot-TBR', 'MPBoot-ACO']
bar_values = [90, 92, 96]
line_values = [227.1, 279.1, 249.8]

# Set figure size
fig, ax1 = plt.subplots(figsize=(8, 4))

# Create numpy array for x-axis
x = np.arange(len(labels))

# Plotting bar chart on left y-axis
width = 0.35
bar_plot = ax1.bar(x - width/2, bar_values, width, label='#Best scores')
ax1.set_ylim([80, 100])
ax1.set_yticks(range(80, 101, 5))
ax1.set_ylabel('Best-known MP-score frequency\nin the original MSAs', fontsize=20)


# Creating twin y-axis for bar chart on the right
ax2 = ax1.twinx()

# Plotting bar chart on right y-axis
line_plot = ax2.bar(x + width/2, line_values, width, color='red', alpha=0.5, label='Time (minutes)')
ax2.set_ylim([200, 300])
ax2.set_yticks(range(180, 301, 20))
ax2.set_ylabel('Average computation time (minutes)', fontsize=20)


ax1.set_xticks(x)
ax1.set_xticklabels(labels, fontsize=27)

ax1.tick_params(axis='y', labelsize=21)
ax2.tick_params(axis='y', labelsize=21)

# Labeling and displaying
plt.title('Best-known MP-score frequency in the original MSAs\nand average computation time out of 115 datasets', fontsize=20)
ax1.legend(loc='upper left', fontsize=22)
ax2.legend(loc='upper right', fontsize=22)
plt.show()
