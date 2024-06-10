import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Assuming your dataframe is named df
sns.boxplot(x='Cause Category', y='Total Injuries', data=df("D:\Workspace\internship\traffic\dataset\df.csv"))

plt.title('Distribution of Injuries by Cause Category')
plt.xticks(rotation=45)
plt.show()


