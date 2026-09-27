import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
wine = load_wine()

df = pd.DataFrame(wine.data, columns=wine.feature_names)
correlation = df.corr()

plt.figure(figsize=(12, 8))
sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")

plt.title("Correlation Heatmap of Wine Dataset")
plt.tight_layout()
plt.show()

corr_pairs = correlation.where(
    ~correlation.eq(1)
).stack().sort_values(ascending=False)

print("Strongest positive correlation:")
print(corr_pairs.head(1))