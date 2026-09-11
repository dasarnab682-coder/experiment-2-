import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris 

iris= load_iris()
df= pd.DataFrame(iris.data,columns=iris.feature_names)
df["target"]=iris.traget

print("---Frist Five Rows---")
print(df.head())

print("\n---Dataset Information---")
print(df.info())

print("\n---Statistical Summary---")
print(df.describe())

print("\n---Missing Values---")
print(df.isnull().sum())

print("\n---Correlation Matrix---")
print(df.corr(numeric_only=True))

plt.figure(figsize=(7,5))
sns.scatterplot(
data=df,
x="sepal length (cm)",
y=" petal length (cm)",
hue="target",
palette="viridis"
)
ptl.title("Sepal Length vs Petal Length bt Class")
plt.show()

plt.figure(figsize=(7,5)
sns.histplot(df["sepal length (cm)"], kde= True,colour="blue")
plt.title("Distribution Of Sepal Length")
plt.show()



