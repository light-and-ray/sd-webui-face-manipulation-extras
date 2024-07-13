import os, cv2
import numpy as np
from PIL import Image
from modules import shared
from modules.images import resize_image
from face_manipulation.zerodim.network.training import Model
from face_manipulation.face_alignment import image_align
from face_manipulation.landmarks_detector import LandmarksDetector


script_dir = os.path.dirname(os.path.abspath(__file__))

model = None

def process(image: Image.Image, factor: str):
    global model
    if model is None:
        model_dir = os.path.join(script_dir, 'weights')
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


detector = None

def alignImage(image: Image.Image) -> list[Image.Image]:
    global detector
    w, h = image.size
    image = image.convert('RGB')
    newH = max(h, min(h*2, 2000))
    newW = max(w, min(w*2, 2000))
    image = resize_image(2, image, w, newH, "Nearest")
    image = resize_image(2, image, newW, newH, "Nearest")
    image.show()
    if detector is None:
        detector = LandmarksDetector(os.path.join(script_dir, 'weights', 'shape_predictor_68_face_landmarks.dat'))
    faces = []
    for land_mark in detector.get_landmarks(image):
        faces.append(image_align(image, land_mark))
    return faces
