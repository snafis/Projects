# Image Classifier

In this project, I have first developed code for an image classifier built with PyTorch (see [Jupyter Notebook](https://github.com/k-bosko/Image-Classifier/blob/master/Image_Classifier_Project.ipynb)), then converted it into a command line application .

## Data
Image Classifier predicts 102 flower categories. The full dataset can be found [here](http://www.robots.ox.ac.uk/~vgg/data/flowers/102/index.html)

Due to size restrictions on GitHub, the dataset is not posted here. You will need to download it separately to run the classifier.

## Requirements
Python 3.7.2
* torchvision==0.2.1
* requests==2.19.1
* torch==1.0.1
* Pillow==5.4.1
* numpy==1.16.2 

## Specifications for command line app

    Train a new network on a data set with train.py
        Basic usage: python train.py data_directory
        Prints out training loss, validation loss, and validation accuracy as the network trains

        Options:
            Set directory to save checkpoints: python train.py data_dir --save_dir save_directory
            Choose architecture: python train.py data_dir --arch "vgg13"
            Set hyperparameters: python train.py data_dir --learning_rate 0.003 --hidden_units 512 --epochs 5
            Use GPU for training: python train.py data_dir --gpu

    Predict flower name from an image with predict.py along with the probability of that name. That is, you'll pass in a single image /path/to/image and return the flower name and class probability.
        Basic usage: python predict.py /path/to/image checkpoint
        Options:
            Return top K most likely classes: python predict.py input checkpoint --top_k 3
            Use a mapping of categories to real names: python predict.py input checkpoint --category_names cat_to_name.json
            Use GPU for inference: python predict.py input checkpoint --gpu

## Acknowledgement

Parts of these code is based on:
- Udacity Introduction to Pytorch Tutorials 
- [Transfer Learning Tutorial](https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html) provided by Sasank Chilamkurthy 


