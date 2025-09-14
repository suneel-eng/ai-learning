# Visualization helps you spot patterns, trends, and anomalies before modeling.
# In AI, it’s used for exploratory data analysis (EDA), model diagnostics, and communicating results.

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# simple line plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, marker='o')
plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# Histogram
data = [7, 8, 5, 6, 9, 7, 8, 6, 7, 9]
sns.histplot(data, bins=5, kde=True)
plt.title("Score Distribution")
plt.show()

# Scatter plot
df = pd.DataFrame({
    "Hours_Studied": [1, 2, 3, 4, 5],
    "Score": [40, 50, 60, 70, 80]
})

sns.scatterplot(x="Hours_Studied", y="Score", data=df)
plt.title("Study Hours vs Score")
plt.show()