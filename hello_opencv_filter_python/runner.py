
import cv2

from typing import Callable


def run(callback:Callable[[cv2.UMat],cv2.UMat]):
  capture=cv2.VideoCapture(0)
  while capture.isOpened():
    result_read,frame=capture.read()
    if not result_read:
      print("not result_read")
      continue
    img_before=frame
    img_after=callback(img_before)
    cv2.imshow('img_before',img_before)
    cv2.imshow('img_after',img_after)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  capture.release()
  cv2.destroyAllWindows()
