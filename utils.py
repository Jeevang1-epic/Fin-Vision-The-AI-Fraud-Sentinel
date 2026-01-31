import cv2
import numpy as np

def check_blur(img):
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    score = cv2.Laplacian(gray, cv2.CV_64F).var()
    return score

def check_tampering(img):
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    score = np.mean(edges)
    return score

def get_status(blur, edge):
    if blur < 100:
        return "Blurry (Suspicious)"
    if edge < 10:
        return "Low Detail (Possible Fake)"
    return "Clear (Likely Authentic)"