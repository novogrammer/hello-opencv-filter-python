
import cv2

from runner import run


def filter_mirror(img_before:cv2.UMat)->cv2.UMat:
  img_after=cv2.flip(img_before,1)
  return img_after

if __name__ == '__main__':
  run(filter_mirror)
