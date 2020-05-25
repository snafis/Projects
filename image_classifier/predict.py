import argparse

from lib.workspace_utils import active_session
from src.utils import predict

parser =  argparse.ArgumentParser()
parser.add_argument("input",
    help = "provide /path/to/image, default 'flowers/test/101/image_07949.jpg'",
    type = str,
    default = 'flowers/test/101/image_07949.jpg'
)
parser.add_argument("checkpoint",
    help = "provide checkpoint to load the model for prediction, e.g. 'checkpoints/checkpoint_resnet18_1epochs.pth'",
    type = str
)
parser.add_argument("--top_k",
    help = "provide the number of top probabilities to display, default 1",
    type = int,
    default = 1
)
parser.add_argument("--category_names",
    help = "specify the location of json file to map categories to real flower names, e.g. cat_to_name.json",
    type = str,
    default = None
)
parser.add_argument("--gpu",
    help = "use gpu for prediction",
    action="store_true"
)
args = parser.parse_args()

#with active_session():
predict(image_path=args.input, checkpoint=args.checkpoint,
        topk=args.top_k, pred_cat_names=args.category_names, use_gpu=args.gpu)
