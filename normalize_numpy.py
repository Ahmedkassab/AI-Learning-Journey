import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def normalize_numpy(xs):
    xs = np.array(xs, dtype=float)   # convert to NumPy array
    return xs / xs.max()             # element-wise division

print(normalize_numpy([1,2,3,4,5]))
print(normalize_numpy([10,20,40]))

df = sns.load_dataset("tips")
print(df.head())
print(df.info())
print(df.describe())
print(df.groupby ("sex")["tip"].mean())

df["tip"].hist(bins=20)
plt.xlabel("tip amount")
plt.ylabel("count")
plt.title("Distribution of Tips")
plt.show()