# %%
import pandas as pd

# %%
ref_path_list = [
    'aaf_mask_nomask_agm/trainval.txt',
    # 'aaf_mask_nomask_agm/train.txt',
    # 'aaf_mask_nomask_agm/test.txt',
    # 'aaf_mask_nomask_agm/val.txt'
]

path = 'AGMdataset_2.5/trainval.txt'
# %%
names = ['tag', 'age', 'gender', 'mask']
AGM25_df = pd.read_csv(path, header=None, names=names, sep=' ')

# AGM25_df.head()
 # %%
df_ref0 = pd.read_csv(ref_path_list[0], header=None, names=names, sep=' ')

# print(df_ref0)
# %%
for i, tag in enumerate(AGM25_df['tag']):
    tag = AGM25_df['tag'][i]
    if tag.startswith('masked_'):
        tag = tag[7:]
    if tag.endswith('.jpg'):
        tag = tag[-12: -4]
    age = AGM25_df['age'][i]
    # print(tag)
    flag = 0

    for j, ref_tag in enumerate(df_ref0['tag']):
        if tag == ref_tag[:8]:
            flag = 1
            ref_age = df_ref0['age'][j]
            AGM25_df['age'][i] = ref_age
            print(tag, age, ref_age)
            break
    
    if flag == 1:
        print('not find tag:', tag, age)

# %%
AGM25_df.to_csv('/Users/junya.inoh/inoh_awl/AGMdataset_2.5/trainval(1).txt', sep=',')
# %%
