
import cv2
import numpy as np

from runner import run


def filter_canny(img_before:cv2.UMat)->cv2.UMat:
  sigma = 0.33
  med = np.median(img_before)
  th1 = int(max(0, (1-sigma)*med))
  th2 = int(min(255, (1+sigma)*med))  
  img_gray = cv2.cvtColor(img_before, cv2.COLOR_BGR2GRAY)
  canny = cv2.Canny(img_gray, th1, th2)
  img_after = cv2.cvtColor(canny, cv2.COLOR_GRAY2BGR)
  return img_after

if __name__ == '__main__':
  run(filter_canny)
