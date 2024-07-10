import cv2
img1=cv2.imread('/home/rizzal/Documents/git/Python/Opencv/avngers1.jpeg')
img2=cv2.imread('/home/rizzal/Documents/git/Python/Opencv/tny2.jpeg')

print(img1,img2)
gry_img=cv2.cvtColor(cv2.imread('/home/rizzal/Documents/git/Python/Opencv/tny1.jpeg'),cv2.COLOR_BGR2GRAY)
# cv2.imshow("Grey Scale",gry_img)
# cv2.waitKey(5000)
# (thresh,bw_img)=cv2.threshold(gry_img,200,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# print(thresh)

# cv2.imshow("Thresh",bw_img)

# cv2.imwite('path',filename,)#to save the img and give the path
# print(gry_img.shape) #For get the size of image or dimension(height,width,chanel) if c 3  its rgb else binarycolor
# resize_img=cv2.resize(gry_img,(1080,1080)) To resize the picture 
# cv2.imshow("imagee",img1)
# cv2.waitKey(5000)
#  cv2.imshow('Img2',img2)
# cv2.waitKey(4000)
# cv2.destroyAllWindows()

# Rectangle
# img = cv2.rectangle(cv2.imread('/home/rizzal/Documents/git/Python/Opencv/lk.jpeg'),pt1=(80,100),pt2=(110,80),color=(101,200,255),thickness=2)

# Ciricle
# img=cv2.circle(cv2.imread('/home/rizzal/Documents/git/Python/Opencv/lk.jpeg'),center=(100,80),radius=40,color=(255,230,200),thickness=3)
# cv2.imshow("Rgb Rectangle",img)
# cv2.waitKey(5000)
# cv2.destroyAllWindows()



# #TExt

# txt=cv2.putText(
#     img2,
#     org=(3,3),
#     text='Iam IRONMAN......',
#     fontFace=cv2.FONT_HERSHEY_COMPLEX,
#     fontScale=2,
#     color=(0,0,255),
#     thickness=1)
# cv2.imshow("IRON MAN",txt)
# cv2.waitKey(8000)
# cv2.destroyAllWindows()
# resize_inmg2=cv2.resize(200,300)
# cv2.imshow(resize_inmg2)
# cv2.waitKeyEx()
# cv2.destroyAllWindows()


img=cv2.imread('/home/rizzal/Documents/git/Python/Opencv/tny1.jpeg')
rec_img=cv2.rectangle(img,plt1=(20,90),plt2=(50,50),color=(0,255,220),thickness=-1)
cir_img=cv2.circle(rec_img,center=(300,300),radius=50,color=(255,199,255),thickness=cv2.FILLED)
txt_img=cv2.putText(
    cir_img,
    org=(200,250),
    text='Smile Plz',
    fontFace=cv2.FONT_HERSHEY_COMPLEX,
    fontScale=2,
    color=(0,0,0),
    thickness=2
)
cv2.imshow('IMAge',txt_img)
cv2.waitKey(5000)
cv2.destroyAllWindows()