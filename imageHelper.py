import cv2
import face_recognition
import numpy as np

async def img2encoding(file):
    encodings = []
    file = await file.read()
    img1 = np.frombuffer(file, np.uint8)
    img_cv = cv2.imdecode(img1, cv2.IMREAD_ANYCOLOR)
    rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(rgb,model='hog')
    encodings = face_recognition.face_encodings(rgb, boxes)
    return list(encodings[0])



def isRegistered(encoding, knownEnc):
    encoding = np.array(encoding)
    knownEnc = np.array(knownEnc)
    matches = face_recognition.compare_faces(knownEnc, encoding)
    if True in matches:
        return True
    
    return False

