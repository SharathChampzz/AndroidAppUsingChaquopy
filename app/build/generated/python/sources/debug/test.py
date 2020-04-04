import warnings
warnings.simplefilter("ignore")
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import cv2
import os
ht=75
wd=75
classNames = ["Tomato_Bacterial_spot","Tomato_Early_blight","Tomato_healthy",
                  "Tomato_Late_blight","Tomato_Leaf_Mold","Tomato_Septoria_leaf_spot",
                  "Tomato_Spider_mites_Two_spotted_spider_mite","Tomato__Target_Spot",
                  "Tomato__Tomato_mosaic_virus","Tomato__Tomato_YellowLeaf__Curl_Virus"]
totClass = len(classNames)


mdl = r"M:\pythonD\15Days\7cls\TensorFlowModel[PB]\Output"
im = r"M:\pythonD\PlantVillageFullDataBase\Tomato\Tomato_healthy\100.JPG"
image = cv2.imread(im)
orig = image.copy()

try:
    image = cv2.resize(image, (ht, wd))
    image = image.astype("float") / 255.0
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
except Exception as e:
    print("Error Occured : ",e)

print("[INFO] loading network...")
model = load_model(os.getcwd())

(zero, one, two , three,four,five,six,seven,eight,nine ) = model.predict(image)[0]
prob = [zero, one, two , three,four,five,six,seven,eight,nine]

maxProb = max(prob)
maxIndex = prob.index(maxProb)
label = classNames[maxIndex]
proba = maxProb

print(label)
print(proba * 100)
