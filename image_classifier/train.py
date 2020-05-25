import argparse

from lib.workspace_utils import active_session
from src.train_model import train_model

parser = argparse.ArgumentParser()
parser.add_argument("data_dir",
    help="specify directory with data",
    type=str
 )
parser.add_argument("--arch",
    help="specify network architecture",
    choices=['vgg13', 'resnet18'],
    default='resnet18'
 )
parser.add_argument("--learning_rate",
    help="specify learning rate, default 0.003",
    type=float,
    default=0.003
 )
parser.add_argument("--epochs",
    help="specify number of epochs, default 1",
    type=int,
    default=1
 )
parser.add_argument("--hidden_units",
    help="specify the size of hidden units via comma, default None",
    nargs='+',
    type=int,
    default=[256]
 )
parser.add_argument("--checkpoint",
    help="specify checkpoint file (*.pth) to load, default None",
    type=str,
    default=None
 )
parser.add_argument("--gpu",
    help = "use gpu for prediction",
    action="store_true"
)
parser.add_argument("--save_dir",
    help="set directory to save checkpoints, default None",
    type=str,
    default=None
 )
args = parser.parse_args()

# train your network
#with active_session():
train_model(model_name=args.arch,
        num_epochs=args.epochs,
        hidden_sizes=args.hidden_units,
        learning_rate=args.learning_rate, data_dir=args.data_dir, model_path=args.checkpoint, 
        use_gpu=args.gpu, save_dir=args.save_dir)
