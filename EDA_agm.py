# %%
import os
from cv2 import imshow
import numpy as np
import pandas as pd
import pandas_profiling as pdp
import matplotlib.pyplot as plt
import glob
import cv2
from pyparsing import originalTextFor
from tqdm import tqdm
from tqdm.contrib import tenumerate
import seaborn as sns
# %%
config = {
    "figure.figsize": [16, 16],
    "axes.titlesize": 40,
    "axes.labelsize": 30,
    "font.size": 20
}
plt.rcParams.update(config)
# print(plt.rcParams)
pd.options.display.precision = 1

# %%
root = 'AGMdataset_2.5/trainval(1).csv'
df = pd.read_csv(root)

df.head()
# pdp.ProfileReport(df)
# %%
# for i in tqdm(range(len(df))):
for i in range(len(df)):
    tag = df['tag'][i]
    path = 'AGMdataset_2.5/images/' + tag
    # print(path)
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    df['min_gray'][i] = img.min()
    df['max_gray'][i] = img.max()
    df['mean_gray'][i] = img.mean()
    df['median_gray'][i] = np.median(img)
    df['var_gray'][i] = img.var()
    df['std_gray'][i] = img.std()


# %%
corr = (df[["SDD-FIQA", "area", "age",'min_gray', 'max_gray', 'mean_gray', 'median_gray', 'var_gray', 'std_gray']].corr())
# corr
sns.heatmap(corr, square=True, annot=True, fmt='.1f')
# df.head()
# pdp.ProfileReport(df)

# %%
# # %%
# df.drop(columns='Unnamed: 0', inplace=True)
# df.head()
# # %%
df.to_csv('AGMdataset_2.5/trainval(1).csv', ',', index=None)

# %%
df
