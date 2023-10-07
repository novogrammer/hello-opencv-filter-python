
import cv2

from runner import run
import numpy as np


def filter_boost_saturation(img_before:cv2.UMat)->cv2.UMat:
  img_hsv=cv2.cvtColor(img_before,cv2.COLOR_BGR2HSV_FULL)
  img_hsv_boosted:cv2.UMat=img_hsv.copy()
  img_hsv_boosted[:,:,1]=cv2.add(img_hsv[:,:,1],255)
  # img_hsv_boosted[:,:,2]=128

  img_after=cv2.cvtColor(img_hsv_boosted,cv2.COLOR_HSV2BGR_FULL)
  return img_after


if __name__ == '__main__':
  run(filter_boost_saturation)
