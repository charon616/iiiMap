import cv2
import numpy as np

# def readXml():
# 	fs = cv2.FileStorage('calibration_result.xml', cv2.FILE_STORAGE_READ)
# 	imgShape = fs['imgShape']
# 	ret = fs['rms']
# 	camInt = fs['intrinsic']
# 	camDist = fs['distortion']
# 	fs.release()

# 	return imgShape, ret, camInt, camDist

# imgShape, ret, camInt, camDist = readXml()
# print(ret)

import cv2
fs = cv2.FileStorage("calibration_result.xml", cv2.FILE_STORAGE_READ)
imgShape = fs.getNode("imgShape")
ret = fs.getNode("rms")
camInt = fs.getNode("intrinsic")
camDist = fs.getNode("distortion")
camInt = cv2.Mat(camInt)
#camDist = np.array(camDist)
print(type(camInt))
print(camInt)

#img = cv2.imdecode(jpg, cv2.IMREAD_COLOR)
img = cv2.imread('data/temp/camera_capture_0.jpg')
print(type(img))
h,  w = img.shape[:2]
newcameramtx, roi=cv2.getOptimalNewCameraMatrix(camInt,camDist,(w,h),1,(w,h))