# %%
import os
from cv2 import imshow
# import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import glob
import cv2
from pyparsing import originalTextFor
from tqdm import tqdm
from tqdm.contrib import tenumerate

# %%
config = {
    "figure.figsize": [16, 16],
    "axes.titlesize": 40,
    "axes.labelsize": 30,
    "font.size": 20
}
plt.rcParams.update(config)
# print(plt.rcParams)
pd.options.display.precision = 4

# %%
root = 'AGMdataset_2.5/trainval.txt'

AGM_dict = {
    'tag': [],
    'age': [],
    'gender': [],
    'mask': []
}


# %%
names = ['tag', 'age', 'gender', 'mask']
AGM_df = pd.read_csv(root, header=None, names=names, sep=' ')
AGM_df['height'] = 0.0
AGM_df['width'] = 0.0
AGM_df['area'] = 0.0
AGM_df['SDD-FIQA'] = 0.0
# AGM_df.head()
# len(AGM_df)
# pdp.ProfileReport(AGM_df)

# %%
AGM_df.sort_values('tag', inplace=True)
AGM_df.head()

# %%
AGM_df_re = AGM_df.reset_index()
AGM_df_re.head()

# %%
score_df = pd.read_csv('AGMdataset_2.5/eval_AGM.csv', sep=',')

# %%
for i in range(10):
    print(AGM_df_re['tag'][i])
    print(score_df['tag'][i], score_df['SDD-FIQA'][i])
    # print(AGM_df['tag'][i])

# %%
img_list = []
for i in tqdm(range(len(AGM_df_re))):
    tag = AGM_df_re['tag'][i]
    path = 'AGMdataset_2.5/images/' + tag
    # print(path)
    img = cv2.imread(path)
    img_list.append(img)
    AGM_df_re['height'][i] = img.shape[0]
    AGM_df_re['width'][i] = img.shape[1]
    AGM_df_re['area'][i] = img.shape[0] * img.shape[1]
    AGM_df_re['SDD-FIQA'][i] = score_df['SDD-FIQA'][i]

# %%
AGM_df_re[0:1]

# %%
fig, ax = plt.subplots()
x = AGM_df_re['area']
y = AGM_df_re['SDD-FIQA']
ax.scatter(x, y)

corr = round(AGM_df_re["area"].corr(AGM_df_re["SDD-FIQA"]), 5)

ax.text(x=100000, y=10, s='correlation = ' + str(corr), fontsize=25, c='orange')
ax.set_xlabel('Area [pixel]')
ax.set_ylabel('SDD-FIQA')
plt.show()
# %%

AGM_df_re.to_csv('AGMdataset_2.5/trainval(1).csv', ',')

# %%
