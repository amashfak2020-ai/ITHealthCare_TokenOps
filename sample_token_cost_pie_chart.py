import matplotlib.pyplot as plt

# Sample Token Cost Calculations data
labels = ['Input Tokens Cost', 'Output Tokens Cost']
sizes = [0.0025, 0.0075]
colors = ['#66b3ff', '#99ff99']
explode = (0.05, 0.05)

plt.figure(figsize=(8, 6))
plt.pie(
    sizes,
    labels=labels,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    explode=explode,
    shadow=True
)
plt.title('Sample Token Cost Calculations')
plt.axis('equal')

# Save and display chart
plt.savefig('sample_token_cost_pie_chart.png', dpi=300, bbox_inches='tight')
plt.show()
