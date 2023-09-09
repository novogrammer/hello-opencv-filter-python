
import cv2

from runner import run


def filter_canny(img_before:cv2.UMat)->cv2.UMat:
  img_gray = cv2.cvtColor(img_before, cv2.COLOR_BGR2GRAY)
  img_after = cv2.Canny(img_gray, 100, 200)
  return img_after

if __name__ == '__main__':
  run(filter_canny)
