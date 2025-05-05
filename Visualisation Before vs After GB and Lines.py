import matplotlib.pyplot as plt

# Data
file_size_before = 35.2
file_size_after = 6.31
lines_before = 6511146
lines_after = 4088762

# Percentage calculations
file_size_change = 100 * (file_size_before - file_size_after) / file_size_before
lines_change = 100 * (lines_before - lines_after) / lines_before

# Create figure with two subplots side by side
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# Plot 1: File Size
bars1 = axs[0].bar(['Before', 'After'], [file_size_before, file_size_after],
                   color=['#4169e1', 'orange'])
for bar in bars1:
    height = bar.get_height()
    axs[0].annotate(f'{height:.2f} GB',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 5),
                    textcoords='offset points',
                    ha='center', va='bottom')

axs[0].set_title(f'File Size Reduction\n({file_size_change:.1f}% smaller)')
axs[0].set_ylabel('Size (GB)')
axs[0].spines['top'].set_visible(False)
axs[0].spines['right'].set_visible(False)
axs[0].yaxis.grid(True, linestyle='--', alpha=0.2)

# Plot 2: Number of Lines
bars2 = axs[1].bar(['Before', 'After'], [lines_before, lines_after],
                   color=['#4169e1', 'orange'])
for bar in bars2:
    height = bar.get_height()
    axs[1].annotate(f'{height:,}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 5),
                    textcoords='offset points',
                    ha='center', va='bottom')

axs[1].set_title(f'Line Count Reduction\n({lines_change:.1f}% fewer lines)')
axs[1].set_ylabel('Number of Lines')
axs[1].spines['top'].set_visible(False)
axs[1].spines['right'].set_visible(False)
axs[1].yaxis.grid(True, linestyle='--', alpha=0.2)

plt.tight_layout()
plt.show()





