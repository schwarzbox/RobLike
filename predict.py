"""guru predict.py """

from fastai.vision import open_image, load_learner, image
import numpy as np
import PIL


def image_to_tensor(img):
    pil_img = PIL.Image.open(img).convert('RGB')
    tensor_img = image.pil2tensor(pil_img, np.float32).div_(255)
    return image.Image(tensor_img)


def process_image(file, modpath):
    img = image_to_tensor(file)
    model = load_learner(modpath)
    pred_class = model.predict(img)[0]
    pred_prob = round(max(model.predict(img)[2]).item() * 100)
    return (str(pred_class), str(pred_prob))
