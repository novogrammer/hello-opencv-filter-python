
import cv2

from runner import run
from filter_mirror import filter_mirror
from filter_canny import filter_canny

def filter_mirrored_canny(img_before:cv2.UMat)->cv2.UMat:
  img_mirrored=filter_mirror(img_before)
  img_after=filter_canny(img_mirrored)
  return img_after

if __name__ == '__main__':
  run(filter_mirrored_canny)
