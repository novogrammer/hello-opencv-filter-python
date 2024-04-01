
import cv2
import numpy as np

from runner import run


def filter_reduce_colors(img_before:cv2.UMat)->cv2.UMat:
  div = 4
  th1 = 256 / div
  th2 = 256 / (div-1)
  img_after = np.clip(img_before // th1 * th2 , 0, 255).astype(np.uint8)
  return img_after

if __name__ == '__main__':
  run(filter_reduce_colors)
