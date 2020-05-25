import copy
import time

import torch
import torch.nn.functional as F
from torch import nn, optim
from torchvision import datasets, models, transforms

from src.network import Network
from src.utils import load_checkpoint, load_data, validate_model

#define train_model function
def train_model(model_name='resnet18',
    num_epochs=1, hidden_sizes=[256], 
    learning_rate=0.003,  model_path=None, data_dir='flowers', 
    use_gpu=False, save_dir='checkpoints'):
    
    train, trainloader, validloader = load_data(data_dir)
    output_size = 102
      
    device = torch.device('cuda' if use_gpu else 'cpu')

    if model_path is None:
        start = 0
        iterations = num_epochs
        train_losses, valid_losses = [], []

        model = None

    else:
        # model, optimizer, iterations, train_losses, valid_losses =load_checkpoint(model_path)
        model_dict = load_checkpoint(model_path)
        
        model = model_dict["model"]
        model = model.to(device)
        optimizer = model_dict["optimizer"]
        model_name = model_dict["model_name"]

        start = model_dict["iterations"]
        iterations = num_epochs + start
        train_losses, valid_losses = model_dict["train_losses"], model_dict["valid_losses"]
        print('starting from {} epoch and training {} epoch(s) now'.format(start, num_epochs))

    #CHECK: also in load_checkpoint, maybe refactor
    if model is None and model_name=='vgg13':
        model = models.vgg13(pretrained=True)
        #turn off gradients for the model
        for param in model.parameters():
            param.requires_grad = False
        input_size = 25088
        model.classifier = Network(input_size, output_size, hidden_sizes)
        optimizer = optim.Adam(model.classifier.parameters(), lr=learning_rate)
    elif model is None and model_name=='resnet18':
        model = models.resnet18(pretrained=True)
        #turn off gradients for the model
        for param in model.parameters():
            param.requires_grad = False
        input_size = 512
        model.fc = Network(input_size, output_size, hidden_sizes)
        optimizer = optim.Adam(model.fc.parameters(), lr=learning_rate)
        
    print('-' * 20)
    print(f"Model name: {model_name}")
    print(f"Learning_rate: {learning_rate}")
    print(f"Hidden_units: {hidden_sizes}\n")
    model.class_to_idx = train.class_to_idx

    criterion = nn.NLLLoss()

    best_model_wts = copy.deepcopy(model.state_dict())
    best_acc = 0.0

    since = time.time()
    steps = 0
    model.to(device)
    
    for epoch in range(start, iterations):
        print('Epoch {}/{}'.format(epoch+1, iterations))
        print('-' * 10)
        print("Train losses: {}".format(train_losses))
        print("Valid losses: {}".format(valid_losses))
        running_loss = 0
        model.train()
        
        for images, labels in trainloader:
            since_train_step = time.time()
            steps += 1
            
            # Move input and label tensors to the GPU
            images, labels = images.to(device), labels.to(device)

            model.train()  
            optimizer.zero_grad()

            with torch.set_grad_enabled(True):
                log_ps = model(images)
                loss = criterion(log_ps, labels)
                loss.backward()
                optimizer.step()
                
                running_loss += loss.item() 
                
                print("Time per train step {}/{}: {}".format(steps, len(trainloader), time.time() - since_train_step))

        else: 
            # Model in inference mode, dropout is off
            model.eval()

            # Turn off gradients for validation, will speed up inference
            with torch.no_grad():
                valid_loss, accuracy = validate_model(model, validloader, criterion, device)

            train_losses.append(round(running_loss/len(trainloader), 3))
            valid_losses.append(round(valid_loss/len(validloader), 3))

            if accuracy > best_acc:
                best_acc = accuracy
                best_model_wts = copy.deepcopy(model.state_dict())

            print("Epoch: {}/{}.. ".format(epoch+1, iterations),
                  "Training Loss: {:.3f}.. ".format(running_loss/len(trainloader)),
                  "Test Loss: {:.3f}.. ".format(valid_loss/len(validloader)),
                  "Test Accuracy: {:.3f}..".format(accuracy/len(validloader)))

            running_loss = 0
            steps = 0

            # Make sure dropout and grads are on for training
            model.train()

    # load best model weights
    model.load_state_dict(best_model_wts)
    
    time_elapsed = time.time() - since
    print('Training complete in {:.0f}m {:.0f}s'.format(time_elapsed // 60, time_elapsed % 60))
    # Save the model to checkpoint 
    checkpoint = {'hidden_sizes': hidden_sizes,
                  'model': model,
                  'state_dict': model.state_dict(),
                  'optimizer': optimizer,
                  'optimizer_dict': optimizer.state_dict(),
                  'class_to_idx': model.class_to_idx,
                  'iterations': iterations,
                  'learning_rate': learning_rate,
                  'train_losses': train_losses,
                  'valid_losses': valid_losses,
                  'model_name': model_name}
    
    checkpoint_filename = "".join(["checkpoint_", model_name, "_", str(iterations), "epochs.pth"])
    if save_dir is not None:
        torch.save(checkpoint, '{}/{}'.format(save_dir, checkpoint_filename))
    else:
        torch.save(checkpoint, checkpoint_filename) 
    return model
