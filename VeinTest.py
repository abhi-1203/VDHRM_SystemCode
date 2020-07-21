import cv2
import numpy as np

def veinDetect():
    print("Capturing image wait..")
    i=cv2.VideoCapture(0)
    check,frame = i.read()
    #frame = cv2.imread("new12.jpg",1)
    og_image = frame[:]
    height, width = frame.shape[0:2]
    startRow = int(height*.45)

    startCol = int(width*.35)

    endRow = int(height*.85)

    endCol = int(width*.85)
    cv2.imwrite('ini.jpg', frame)
    print('\nImage Captured.')

    croppedImage = frame[startRow:endRow, startCol:endCol]
    cv2.imwrite('cropped.jpg', croppedImage)


    img = np.zeros(frame.shape,dtype=np.uint8)
    img.fill(0) # or img[:] = 255
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    my_clahe = cv2.createCLAHE(clipLimit=30, tileGridSize=(8,8))
    cl_img=my_clahe.apply(gray)
    
    gray_filtered = cv2.bilateralFilter(cl_img,150, 10,10)
    ret3,th31 = cv2.threshold(cl_img,0,255,cv2.THRESH_TRUNC+cv2.THRESH_OTSU)
    cv2.imwrite('thresh.jpg',th31 )
    lap=cv2.Laplacian(th31,cv2.CV_64F,ksize=3)
    lap=np.uint8(np.absolute(lap))
    edges_high_thresh = cv2.Canny(th31, 100, 200)
    contours, hierarchy = cv2.findContours(th31,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
    for c in contours:
        rect = cv2.boundingRect(c)
        x,y,w,h = rect
        cv2.drawContours(th31, c, -1, (255,255,255), 1)
    
    cv2.imshow('Final.jpg', th31)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return True

#veinDetect()
