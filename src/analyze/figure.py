import matplotlib.pyplot as plt
import numpy as np

# Assuming these are your scores (replace with your actual values)
coverage_rates = {
    'GPT-4 Generated': 60.19777503090235,  # example value
    'Non-Expert Modified': 97.77503090234858,  # example value
    'Expert Modified': 100  # example value
}

# informativeness_scores = {
#     'GPT-4 Generated': 4.5,  # example value
#     'Non-Expert Modified': 4.2,  # example value
#     'Expert Modified': 4.8  # example value
# }

# Setup
labels = list(coverage_rates.keys())
coverage_values = list(coverage_rates.values())
# informativeness_values = list(informativeness_scores.values())
bar_width = 0.35
index = np.arange(len(labels))

# Create bars
fig, ax1 = plt.subplots()

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
rects1 = ax1.bar(index, coverage_values, bar_width, label='Coverage Rate (%)', color='b', alpha=0.6)
# rects2 = ax2.bar(index + bar_width, informativeness_values, bar_width, label='Informativeness (Score)', color='r', alpha=0.6)

# Add some text for labels, title, and custom x-axis tick labels, etc.
ax1.set_xlabel('Manual Type')
ax1.set_ylabel('Coverage Rate (%)', color='b')
ax2.set_ylabel('Informativeness (Score)', color='r')
ax1.set_xticks(index + bar_width / 2)
ax1.set_xticklabels(labels)
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

ax1.tick_params(axis='y', labelcolor='b')
ax2.tick_params(axis='y', labelcolor='r')

plt.tight_layout()
plt.savefig('./output/figure/coverage_rate_and_informativeness.png')
