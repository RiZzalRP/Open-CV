# Grey Scale image
import cv2
img1=cv2.imread('/home/rizzal/Documents/git/Python/Opencv/tny1.jpeg')

gry_img=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)  # color image converted to gray color

# print(gry_img)
cv2.imshow("COLOR IMAGE ",img1)
cv2.imshow("Grey Scale Color",gry_img)
cv2.waitKey()
cv2.destroyAllWindows()

# Binary Image 
(thresh,bw_img)=cv2.threshold(gry_img,200,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# print(thresh)
cv2.imshow("Binary Image",bw_img)
cv2.waitKey()
cv2.destroyAllWindows()

print(gry_img.shape) #For get the size of image or dimension(height,width,chanel) if c 3  its rgb else binarycolor
print(img1.shape)


