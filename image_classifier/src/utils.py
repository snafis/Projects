import time
import json

import torch
from torchvision import datasets, models, transforms

import PIL
from PIL import Image
import numpy as np


def load_checkpoint(filepath):

    if torch.cuda.is_available():
        checkpoint = torch.load(filepath)
    else:
        checkpoint = torch.load(filepath, map_location='cpu')
    
    model = checkpoint['model']
    model.load_state_dict(checkpoint['state_dict'])
    optimizer = checkpoint['optimizer']
    optimizer.load_state_dict(checkpoint['optimizer_dict'])
    
    if torch.cuda.is_available():
        for state in optimizer.state.values():
            for k, v in state.items():
                if torch.is_tensor(v):
                    state[k] = v.cuda()
                  
    model.class_to_idx = checkpoint['class_to_idx']
    iterations = checkpoint['iterations']
    train_losses = checkpoint['train_losses']
    valid_losses = checkpoint['valid_losses']
    model_name = checkpoint['model_name']

    res = dict(
        model=model,
        optimizer=optimizer,
        iterations=iterations,
        train_losses=train_losses,
        valid_losses=valid_losses,
        model_name=model_name)

    return res

def validate_model(model, validloader, criterion, device):
    
    accuracy = 0
    valid_loss = 0
    since_test_step = time.time()
    
    for images, labels in validloader:
        
        images, labels = images.to(device), labels.to(device)
        output = model.forward(images)
        batch_loss = criterion(output, labels)
        valid_loss += batch_loss.item()
        
        ## Calculating the accuracy 
        # Model's output is log-softmax, take exponential to get the probabilities
        ps = torch.exp(output)
        # Class with highest probability is our predicted class
        _, top_class = ps.topk(1, dim=1)
        equals = top_class == labels.view(*top_class.shape)
        accuracy += torch.mean(equals.type(torch.FloatTensor))

        print("Time since test step: {}".format(time.time() - since_test_step))

    return valid_loss, accuracy

def load_data(data_dir):
    train_dir = data_dir + '/train'
    valid_dir = data_dir + '/valid'

    # Define your transforms for the training, validation, and testing sets
    train_transforms = transforms.Compose([transforms.RandomVerticalFlip(),
                                        transforms.RandomRotation(45),
                                        transforms.RandomResizedCrop(224),
                                        transforms.ToTensor(),
                                        transforms.Normalize(mean=[0.485, 0.456, 0.406], 
                                                                std=[0.229, 0.224, 0.225])])

    valid_transforms = transforms.Compose([transforms.Resize(256),
                                        transforms.CenterCrop(224),
                                        transforms.ToTensor(),
                                        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                                                std=[0.229, 0.224, 0.225])])

    # Loading the datasets with ImageFolder
    train = datasets.ImageFolder(train_dir, transform=train_transforms)
    validation = datasets.ImageFolder(valid_dir, transform=valid_transforms)

    # Using the image datasets and the trainforms, define the dataloaders
    trainloader = torch.utils.data.DataLoader(train, batch_size=64, shuffle=True)
    validloader = torch.utils.data.DataLoader(validation, batch_size=64)

    return train, trainloader, validloader

def process_image(image):
    ''' Scales, crops, and normalizes a PIL image for a PyTorch model,
        returns an Numpy array
    '''
    image = Image.open(image)
    image.thumbnail([256, 256])
    
    torch_cropped = transforms.CenterCrop((224,224))
    center_cropped = torch_cropped(image)
 
    np_image = np.array(center_cropped)/256
    mean = np.array([0.485, 0.456, 0.406])
    std = np.array([0.229, 0.224, 0.225])
    norm_image = (np_image - mean)/std
    trans_image = norm_image.transpose((2, 0, 1))
    
    return trans_image

def predict(image_path, checkpoint, topk=1, pred_cat_names=None, use_gpu=False):
    ''' Predict the class (or classes) of an image using a trained deep learning model.
    '''
    model_dict = load_checkpoint(checkpoint)
    model = model_dict["model"]

    device = torch.device('cuda' if use_gpu else 'cpu')
    
    model = model.to(device)

    img_numpy = process_image(image_path)
    img = torch.from_numpy(img_numpy)
    
    model.eval()
    # Turn off gradients to speed up this part
    with torch.no_grad():
        model.type(torch.DoubleTensor)
        logits = model.forward(img.unsqueeze_(0))
    
    # Output of the network are logits, need to take exponential for probabilities
    ps = torch.exp(logits)

    probs, class_idx = ps.topk(topk, dim=1)
    probs = probs.data.numpy().squeeze()
    class_idx = class_idx.data.numpy().squeeze()

    if pred_cat_names is not None:
        with open(pred_cat_names, 'r') as f:
            cat_to_name = json.load(f)

    classes = []
    for i in range(class_idx.size):
        for key, value in model.class_to_idx.items():
            if class_idx.size == 1 and class_idx == value:
                classes.append(key)
            elif class_idx.size > 1 and class_idx[i] == value:
                classes.append(key)

    if pred_cat_names is None:
        print(f'top {topk} probabilities: {probs}, flower classes: {classes}')
    else: 
        pred_class_names = []
        for x in classes:
            y = cat_to_name[x]
            pred_class_names.append(y)
        print(f'top {topk} probabilities: {probs}, flower names: {pred_class_names}')
