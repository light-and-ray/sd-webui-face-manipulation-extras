import os, cv2
import numpy as np
from PIL import Image
from modules import shared
from face_manipulation.zerodim.network.training import Model


script_dir = os.path.dirname(os.path.abspath(__file__))

model = None

def process(image: Image.Image, factor: str):
    global model
    if model is None:
        model_dir = os.path.join(script_dir, 'zerodim', 'cache', 'models', 'zerodim-ffhq-x256')
        old_disable_safe_unpickle = shared.cmd_opts.disable_safe_unpickle
        try:
            shared.cmd_opts.disable_safe_unpickle = True
            model = Model.load(model_dir)
        finally:
            shared.cmd_opts.disable_safe_unpickle = old_disable_safe_unpickle

    img = np.asarray(image.convert('RGB'))
    img = cv2.resize(img, dsize=(model.config['img_shape'][1], model.config['img_shape'][0]))
    manipulated_img = model.manipulate(img, factor)
    return Image.fromarray(manipulated_img)
