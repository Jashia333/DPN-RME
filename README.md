# DPN-RME ( Deep Progressive Network)

This repository contains the implementation of Deep Progressive Network which generates the radio maps using the multiple networks in a recursive way as specified in the Radio Map Estimation with Deep Progressive Network paper

## Installation
The following are steps used to generate the paper results

1. Clone the DPN-RME Respository

2. Navigate to the cloned repository and run the following commands.

```
git clone https://github.com/Jashia515/DPN-RME
cd repo
pip install -r requirements.txt
```
3. To generate the dataset use the following command and pass the "--buildings" to ensure the environmental mask is generated. A folder is created with the test and train sub folder which consists of 250000 maps.
```
python generate_dataset.py --buildings 
```
4. Use the train.py to train the model

5. The visualize.py is used to visual the passed sample map, environmental map and the predicted map.

## Reference 

The Code to generate the dataset is taken from [deep-autoencoders-cartography](https://github.com/fachu000/deep-autoencoders-cartography). 
The model architecture is taken from the [skip-residual-network](https://github.com/nikitalokhmachev-ai/radio-map-estimation-public).

## Warning

The dataset used for the training of the DPN may not be same as the maps are generated in stochastic manner and is also dependent on the GPU Architecture. A slight variations in the results is expected in comparision with the paper results.

## Badges
![Static Badge](https://img.shields.io/badge/pytorch-python?style=plastic&logoColor=hex)
![Static Badge](https://img.shields.io/badge/numpy-python?style=plastic&logoColor=hex)
![Static Badge](https://img.shields.io/badge/matplotli-3.7.1-2?logoColor=hsl&labelColor=green&color=red)
![Static Badge](https://img.shields.io/badge/scikit_learn-1.2.2-2?logoColor=hsl&labelColor=green&color=red)
![Static Badge](https://img.shields.io/badge/opencv_python-4.8.0.76-2?logoColor=hsl&labelColor=green&color=blue)
![Static Badge](https://img.shields.io/badge/wandb-0.14.2-r?logoColor=blue&labelColor=blue)
![Static Badge](https://img.shields.io/badge/joblib-1.2.0-p?logoColor=blue&labelColor=blue)



