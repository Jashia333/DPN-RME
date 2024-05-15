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
4. 