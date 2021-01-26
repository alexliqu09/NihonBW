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
- 23/01/2021 :
 The Streamlit is almost finished , the [Pix2Pix](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix) model is loaded and ready to test and the [InstColorization](https://github.com/ericsujw/InstColorization) model is in the last training process .
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

3. Clone this repo:
 ```
git clone https://github.com/alexliqu09/NihonBW.git
 ```
## Train models

## Pix2Pix
1. If you want to train the model in local , first you need clone the original repository [Pix2Pix](https://colab.research.google.com/drive/19AhOZNh4WV123PdF4A4A0_MlsSpXKgd6?usp=sharing).
2. Now you should create a dir  in pytorch-CycleGAN-and-pix2pix / datasets / with the name colorization and inside of this dir you create train dir , now  in train dir put your color images of trains . 
3. Finally , you only follow the script of Pix2Pix repository and use the follow command  
```
python train.py --dataroot ./datasets/colorization --name color_pix2pix --model colorization 
```
4. Search the dir checkpoints/color_pix2pix the weigth  ```latest_net_G.pth ```.

5. Now in the dir ```/NihongoBW/pytorchpix2pix/checkpoints/ ``` create the dir ```experiment_name``` and  you need to move the  ```latest_net_G.pth ``` in the dir ```/NihongoBW/pytorchpix2pix/checkpoints/experiment_name/```.

* Note: If you want to train the model in colab , I have this available [here](https://colab.research.google.com/drive/19AhOZNh4WV123PdF4A4A0_MlsSpXKgd6?usp=sharing).
* Note: The dataset used me is available [here](https://drive.google.com/drive/folders/1h92vKaWDMGzolhSv0mOF8-J_OkVznQBw?usp=sharing)
## Run the work
If You want to proof the work , you need mov to dirs and position yourself with ```NihonBW/``` and run this command
```
streamlit run Main.py
```
* Note: 
```
Local host : http://localhost:8501 
Network URL:  http://192.168.0.5:8501
```
## 👨🏽‍💻 Maintainer
* Alexander Leonardo Lique Lamas, Github: [alexliqu09](https://github.com/alexliqu09) Email: alexander.lique.l@uni.pe

## 🙏🏽 Special thanks

* Many thanks to the repository of [junyanz](https://github.com/junyanz) author of [Pix2Pix](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix),this work would not have been possible without your repository.
* Many thanks to the repository of [ericsujw](https://github.com/ericsujw) author of [InstColorization](https://github.com/ericsujw/InstColorization),this work would not have been possible without your repository.

## Citation
If you want to cite this code for your research , please cite my paper:
```
 @article{lique , 
 title={Coloring Black and White Images}, 
 author={Lique Lamas, Alexander Leonardo},
 year={2021}} 
```
If you find InstColorization useful , please cite this paper:
```
@inproceedings{Su-CVPR-2020,
  author = {Su, Jheng-Wei and Chu, Hung-Kuo and Huang, Jia-Bin},
  title = {Instance-aware Image Colorization},
  booktitle = {IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
  year = {2020}
}
```
If you find Pix2Pix useful , please cite this paper:
```
@inproceedings{isola2017image,
  title={Image-to-Image Translation with Conditional Adversarial Networks},
  author={Isola, Phillip and Zhu, Jun-Yan and Zhou, Tinghui and Efros, Alexei A},
  booktitle={Computer Vision and Pattern Recognition (CVPR), 2017 IEEE Conference on},
  year={2017}
}
```