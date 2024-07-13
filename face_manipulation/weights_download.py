import os
from modules.modelloader import load_file_from_url

script_dir = os.path.dirname(os.path.abspath(__file__))

ROOT_URL = 'https://huggingface.co/light-and-ray/face-manipulation'

def ensureAllModelsDownloaded():
    modelsPath = os.path.join(script_dir, 'weights')
    os.makedirs(modelsPath, exist_ok=True)

    files = ['amortized.pth', 'latent.pth', 'config.pkl', 'shape_predictor_68_face_landmarks.dat']
    for file in files:
        if os.path.exists(os.path.join(modelsPath, file)):
            continue
        load_file_from_url(url=f'{ROOT_URL}/resolve/main/{file}?download=true', model_dir=modelsPath)


