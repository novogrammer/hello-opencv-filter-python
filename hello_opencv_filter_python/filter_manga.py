
import cv2
import numpy as np

from filter_canny import filter_canny
from filter_dilate import filter_dilate
from filter_blur import filter_blur
from filter_reduce_colors import filter_reduce_colors
from runner import run

# https://qiita.com/mo256man/items/8a9bb7bb66e107fd7153
def filter_manga(img_before:cv2.UMat)->cv2.UMat:
  img_canny=filter_canny(img_before)
  img_canny_dilate=filter_dilate(img_canny)
  img_blur=filter_blur(img_before)
  img_blur_reduce_colors=filter_reduce_colors(img_blur)
  img_after = np.where(img_canny_dilate==255, 255-img_canny_dilate, img_blur_reduce_colors)
  return img_after

if __name__ == '__main__':
  run(filter_manga)
