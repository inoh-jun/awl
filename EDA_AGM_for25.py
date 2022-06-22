# %%
import os
# import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_profiling as pdp
import glob
import cv2
from tqdm import tqdm
# from tqdm.contrib import tenumerate
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
AGM_df = pd.read_csv(root, header=None, names=names, sep=' ').sort_values('tag')
AGM_df.head()
len(AGM_df)
# pdp.ProfileReport(AGM_df)
# %%
config = {
    "figure.figsize": [16, 16],
    "axes.titlesize": 40,
    "axes.labelsize": 30,
    "font.size": 20
}
plt.rcParams.update(config)
# print(plt.rcParams)
# %%
# # age
# fig, ax = plt.subplots(figsize = (16, 16))
# # ax.plot(AGM_df['age'])
# bins = range(0, 101, 10)
# ax.hist(AGM_df['age'], bins=bins)
# ax.set_xticks(bins)
# ax.set_xlabel('age')
# ax.set_ylabel('count')
# ax.set_title('Age')
# plt.show()

# # gender
# male = AGM_df['gender'] == 'male'
# # print(male.sum())
# female = AGM_df['gender'] == 'female'
# # print((female.sum()))
# fig, ax = plt.subplots(figsize = (16, 16))
# left = ['male', 'female']
# height = [male.sum(), female.sum()]
# ax.bar(left, height)
# ax.set_ylabel('count')
# ax.set_title('Gender')
# plt.show()

# # mask
# mask = AGM_df['mask'] == 'mask'
# # print(mask.sum())
# nomask = AGM_df['mask'] == 'nomask'
# # print((nomask.sum()))

# fig, ax = plt.subplots(figsize = (16, 16))
# left = ['mask', 'nomask']
# height = [mask.sum(), nomask.sum()]
# ax.bar(left, height)
# ax.set_ylabel('count')
# ax.set_title('Mask')
# plt.show()



# %%
path_list = sorted(glob.glob('AGMdataset_2.5/images/**.jpg', recursive=True))

img_list = []
img_shape_list = []
img_area_list = []

for path in tqdm(path_list):
    img = cv2.imread(path)
    img_list.append(img)
    img_shape_list.append(img.shape)
    img_area_list.append(img.shape[0] * img.shape[1])

# %%
img_df = pd.DataFrame((img_shape_list, img_area_list), index=['img_shape', 'img_area']).T
# print(len(img_df))

# age
fig, ax = plt.subplots(figsize = (16, 16))
# bins = range(0, 101, 10)
ax.hist(img_df['img_area'], bins = 100)
# ax.set_xticks(bins)
ax.set_xlabel('area')
ax.set_ylabel('count')
ax.set_title('Area Distribution [AGMdataset_2.5]')
plt.grid()
plt.show()

# %%