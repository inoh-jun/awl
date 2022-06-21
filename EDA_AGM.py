# %%
import os
import pandas as pd
import matplotlib.pyplot as plt
# %%
root = 'aaf_mask_nomask_agm/images'

AGM_dict = {
    'tag': [],
    'age': [],
    'gender': [],
    'mask': []
}

path_list = os.listdir(root)
# print(path_list)
for path in path_list:
    # print(path.split('.')[0].split('_'))
    path = path.split('.')[0].split('_')

    AGM_dict['tag'].append(path[0])
    AGM_dict['age'].append(int(path[-3]))
    AGM_dict['gender'].append(path[-2])
    AGM_dict['mask'].append(path[-1])

# print(AGM_dict)
AGM_df = pd.DataFrame(AGM_dict)
AGM_df
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
# age
fig, ax = plt.subplots(figsize = (16, 16))
# ax.plot(AGM_df['age'])
bins = range(0, 101, 10)
ax.hist(AGM_df['age'], bins=bins)
ax.set_xticks(bins)
ax.set_xlabel('age')
ax.set_ylabel('count')
plt.show()

# gender
male = AGM_df['gender'] == 'male'
# print(male.sum())
female = AGM_df['gender'] == 'female'
# print((female.sum()))
fig, ax = plt.subplots(figsize = (16, 16))
left = ['male', 'female']
height = [male.sum(), female.sum()]
ax.bar(left, height)
plt.show()
 # %%
# mask
mask = AGM_df['mask'] == 'mask'
# print(mask.sum())
nomask = AGM_df['mask'] == 'nomask'
# print((nomask.sum()))

fig, ax = plt.subplots(figsize = (16, 16))
left = ['mask', 'nomask']
height = [mask.sum(), nomask.sum()]
ax.bar(left, height)
plt.show()

# %%
