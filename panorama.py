import cv2
import os

mainFolder = 'Images'
myFolder = os.listdir(mainFolder)

for folder in myFolder:
    path = mainFolder + '/'+folder
    images = []
    myList = os.listdir(path)

    for imgN in myList:
        curImg = cv2.imread(f'{path}/{imgN}')
        curImg = cv2.resize(curImg,(0,0),None,0.2,0.2)
        images.append(curImg)

    stitcher = cv2.Stitcher.create()
    (status,result) = stitcher.stitch(images)
    if status == cv2.STITCHER_OK:
         print('panorama generated')
         cv2.imshow('result',result)
         cv2.waitKey(1)
    else:
        print('unGenerated')
cv2.waitKey(0)