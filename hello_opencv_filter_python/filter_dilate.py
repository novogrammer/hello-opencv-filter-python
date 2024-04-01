
import cv2
import numpy as np

from runner import run


def filter_dilate(img_before:cv2.UMat)->cv2.UMat:
  kernel = np.ones([3,3],np.uint8)
  img_after = cv2.dilate(img_before, kernel)
  return img_after

if __name__ == '__main__':
  run(filter_dilate)
