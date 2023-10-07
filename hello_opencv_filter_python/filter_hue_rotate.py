
import cv2
import time

from runner import run
import numpy as np


def filter_hue_rotate(img_before:cv2.UMat)->cv2.UMat:
  t=time.perf_counter()
  tshift=int((t/10.0*256)%256)
  img_hsv=cv2.cvtColor(img_before,cv2.COLOR_BGR2HSV_FULL)
  img_hsv_rotated:cv2.UMat=img_hsv.copy()
  img_hsv_rotated[:,:,0]=img_hsv[:,:,0]+tshift

  img_after=cv2.cvtColor(img_hsv_rotated,cv2.COLOR_HSV2BGR_FULL)
  return img_after

if __name__ == '__main__':
  run(filter_hue_rotate)
