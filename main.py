from yolo_prediction import yoloPrediction
from detect_char import detectChar

img_path = "C:/Users/DELL/Downloads/6.jpg"
img = yoloPrediction(img_path)
str = detectChar(img)

print(str)
