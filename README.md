<h2 align="center">
<p>  NihonBW 🇯🇵 </p>
</h2>
<h2 align="center">
<p></p>
<img src="https://img.shields.io/badge/PyTorch%20-%23EE4C2C.svg?&style=for-the-badge&logo=PyTorch&logoColor=white" />
<img src="https://img.shields.io/badge/numpy%20-%23013243.svg?&style=for-the-badge&logo=numpy&logoColor=white" />
<p></p>
</h2>

## 📜 Abstract 

## 🆕 Update
23/01/2021 - The Streamlit is almost finished , the [Pix2Pix](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix) model is loaded and ready to test and the [InstColorization](https://github.com/ericsujw/InstColorization) model is in the last training process .
## 📖 Content
The following tree shows the structure of the application:
```
| -master-NihonBW/
|   |-BW/
|       |-Images/
|       |-Result/
|   |-RC/
|       |-Images/
|   |-env/..
|   |-test_pix2pix/..
|   |-imgs/..
|   |-InstColorization/..
|   |-pytorchpix2pix/..
|         |-data/..
|         |-datasets/..
|         |-imgs/..
|         |-options/..
|         |colorization/..
|         |-models/..
|         |..   
|   |-Main.py
|   |-.gitignore
|   |-README.md
|   |-requeriment.txt
```
## Prerequisites

* Linux
* Python 3
* GPU + CUDA CuDNN

## Getting Started

## Installation
1. Install the envariment
 ```
 pip install virtualenv
 ```
2. Install all dependencies with the command
 ```
 pip install -r requirements.txt.
 ```
## Train models

1. Pix2Pix

* If you want to train the model , I have this available  colab [here](https://colab.research.google.com/drive/19AhOZNh4WV123PdF4A4A0_MlsSpXKgd6?usp=sharing).

## Citation
if you want to cite this code for your research , please cite my papers.
```
 @article{lique , 
 title={Coloring Black and White Images}, 
 author={Lique Lamas, Alexander   Leonardo},
 year={2021}} 
```
## 👨🏽‍💻 Maintainer
* Alexander Leonardo Lique Lamas, Github: [alexliqu09](https://github.com/alexliqu09) Email: alexander.lique.l@uni.pe

## 🙏🏽 Special thanks

* Many thanks to the repository of [junyanz](https://github.com/junyanz) author of [Pix2Pix](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix),this work would not have been possible without your repository.
