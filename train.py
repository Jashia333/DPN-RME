import torch
import numpy as np

import os
import glob
import joblib
import random

from data_utils import MapDataset

from models.autoencoders import BaselineAutoencoder
from models.autoencoders import SkipAutoencoder, SkipResidualAutoencoder, SkipMaskAutoencoder, SkipMaskMapAutoencoder
from models.autoencoders import SkipMapAutoencoder, SkipMapMaskAutoencoder, SkipInputAutoencoder
from models.autoencoders import DualMaskAutoencoder, DualMaskMapAutoencoder, DualMapAutoencoder, DualMaskMapAutoencoder, DualInputAutoencoder


seed = 3
torch.manual_seed(seed)
torch.use_deterministic_algorithms(True)
np.random.seed(seed)
random.seed(seed)
torch.cuda.empty_cache()

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

train_batch_size = 256
# train_batch_size = 128
# train_batch_size = 512
# train_batch_size = 1
num_epochs = 100
# num_epochs = 100
lr = 5e-4
# lr = 6e-4
# lr = 7e-4  # 1.7197576692141305
# lr = 7.5e-4  # loss is too big
# lr = 8e-4  # loss is too big
# lr = 1e-3  # loss increase.

# Manually set values for buildings, unsampled locations, and sampled locations in the environment mask.
# For the models in the PIMRC paper, these are set to "None", meaning they keep the default values of -1, 0, and 1 respectively.
building_value = None
unsampled_value = None
sampled_value = None

# this is skip residual
model = SkipResidualAutoencoder().to(device)
# model = SkipMapMaskAutoencoder().to(device)
#model = SkipInputAutoencoder().to(device)



# this is skip map
# model = SkipMapAutoencoder().to(device)

# model_name = 'Skip_Residual.pth'

model_folder = r'E:\unt\spring_2024\special_probs\DPN-RME\models'


# train_data_folder = '/home/UNT/sd1260/radio-map-estimation-public/dataset/train'
train_data_folder = r'E:\unt\spring_2024\special_probs\radio-map-estimation-public\dataset\generated_maps\04_30__22h_03m\test'
scaler_path =r'E:\unt\spring_2024\special_probs\DPN-RME\scalers\minmax_scaler_zero_min134.joblib'


train_pickle_path = os.path.join(train_data_folder, '*.pickle')
train_pickles = glob.glob(train_pickle_path)

with open(scaler_path, 'rb') as f:
  scaler = joblib.load(f)

train_ds = MapDataset(train_pickles, scaler=scaler, building_value=building_value, sampled_value=sampled_value)
train_dl = torch.utils.data.DataLoader(train_ds, batch_size=train_batch_size, shuffle=False)
optimizer = torch.optim.AdamW(model.parameters(), lr=lr)

model.fit(train_dl, optimizer, epochs=num_epochs)
# model.save_model(os.path.join(model_folder, model_name))

# torch.save(model.state_dict(), os.path.join(model_folder, 'model_baseline_skipresidual_100.pth'))
torch.save(model.state_dict(), os.path.join(model_folder, 'DPN_Network.pth'))
