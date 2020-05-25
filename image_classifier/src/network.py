from torch import nn
import torch.nn.functional as F

# define deep learning network as a class
class Network(nn.Module):
    def __init__(self, input_size, output_size, hidden_sizes, drop_p=0.3):
        super().__init__()
                
        # Inputs to hidden layer linear transformation
        self.hidden_sizes = nn.ModuleList([nn.Linear(input_size, hidden_sizes[0])])
        
        # Add a variable number of more hidden layers
        layer_sizes = zip(hidden_sizes[:-1], hidden_sizes[1:])
        self.hidden_sizes.extend([nn.Linear(h1, h2) for h1, h2 in layer_sizes])
        # Output layer
        self.output = nn.Linear(hidden_sizes[-1], output_size)
        
        self.dropout = nn.Dropout(p=drop_p)
        
    def forward(self, x):
        ''' Forward pass through the network, returns the output logits '''
        
        for each in self.hidden_sizes:
            
            x = F.relu(each(x))
            x = self.dropout(x)
        
        x = self.output(x)
        
        return F.log_softmax(x, dim=1)
