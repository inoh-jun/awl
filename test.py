# %%
import numpy as np
import glob
from PIL import Image
from tqdm.contrib import tenumerate
import MLBook.codes.data as data
myData = data.unsupervised()
myData.makeData(dataType=1)
# %%
print(myData.X.shape)
# %%
root = 'AGMdataset_2.5/images'
path_list = glob.glob(root + '/**.jpg')
N = 10
height = 256
width = 256

dataset = np.zeros(height * width * N).reshape(N, height * width)
for i, path in tenumerate(path_list[:10]):
    img = Image.open(path).convert('L').resize((256, 256), Image.BICUBIC)
    dataset[i] = np.array(img).flatten()

print(dataset.shape)


# %%
