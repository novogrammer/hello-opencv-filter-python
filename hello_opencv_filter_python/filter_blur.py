
import cv2

from runner import run


def filter_blur(img_before:cv2.UMat)->cv2.UMat:
  img_after = cv2.GaussianBlur(img_before,(5,5),0)
  # img_after = cv2.GaussianBlur(img_before,(7,7),0)
  return img_after

if __name__ == '__main__':
  run(filter_blur)
