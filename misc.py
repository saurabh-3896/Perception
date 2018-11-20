import cv2,numpy as np
from scipy.spatial.distance import euclidean


img = cv2.imread('box.png')
img_shape = img.shape
print(img_shape)
#
#
def perspect_transform(img, src, dst,obj):
    obj = np.array([obj],np.float32)
    # corners = np.hstack(tuple(obj.ravel()))
    # print(corners)
    # Get transform matrix using cv2.getPerspectivTransform()
    M = cv2.getPerspectiveTransform(src, dst)
    # Warp image using cv2.warpPerspective()
    # keep same size as input image

    warped = cv2.warpPerspective(img, M, (img.shape[1], img.shape[0]))

    print(obj,M)


    objWarped =  cv2.perspectiveTransform(obj,M)

    return warped,M,objWarped
#
source = np.array([[150,310],[455,310],[540,405],[45,405]],np.float32)
source1 = np.array([[150,310],[455,310],[540,405],[45,405]])
#
car_coord =[[255,200],[350,200],[350,290],[255,290]]
car_coord1 =[255,200],[350,200],[350,290],[255,290]
#
#
dst_size = 10

# Set a bottom offset to account for the fact that the bottom of the image
# is not the position of the rover but a bit in front of it
bottom_offset = 10

destination = np.array([[img.shape[1]/2 - dst_size, img.shape[0] - 2*dst_size - bottom_offset],
                        [img.shape[1]/2 + dst_size, img.shape[0] - 2*dst_size - bottom_offset],
                        [img.shape[1] / 2 + dst_size, img.shape[0] - bottom_offset],
                        [img.shape[1]/2 - dst_size, img.shape[0] - bottom_offset] ],np.float32)

#
# # destination = np.array([[120. ,304.],[150. ,304.],[180. ,354.],[120. ,354.]],np.float32)
# # destination = np.array([[190. ,360.],[210. ,360.],[210. ,380.],[190. ,380.]],np.float32)
print(destination)
# print(source.shape,destination.shape)
cv2.rectangle(img,tuple(car_coord[0]) , tuple(car_coord[2]), (0, 255, 0), 3)
cv2.rectangle(img,tuple(destination[0]) , tuple(destination[2]), (255, 255, 0), 3)
#
# cv2.rectangle(img, source[0] , source[2], (255, 0, 0), 3)
# pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = source1.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255))
#
#
warped,objWarped = perspect_transform(img, source, destination,car_coord)
#
print("objWarped",objWarped)

warpedDistance = euclidean(destination[0],destination[1])

# centerDistance = euclidean([320,460],[320,441])
centerDistance = euclidean([320,460],[319,417])

print(warpedDistance,centerDistance)

print("final distance ", (30*centerDistance)/warpedDistance)

### 20 pixels == 30 cm
### 102 pixels == ?



cv2.imshow("car",img)
cv2.imshow("warp",warped)
# # cv2.polylines(img,car_coord,(255,255,255),1)
cv2.waitKey(0)
#




#
#
# import cv2
#
# cap = cv2.VideoCapture(0)
#
# while True:
#     ret,img = cap.read()
#     cv2.imshow("img",img)
#
#
#
#     k = cv2.waitKey(1)
#
#     if  k == 27:
#         break


