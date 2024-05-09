import cv2

img=cv2.imread("/home/user/Pictures/news_preview_mob_image__preview_404.jpg")
img2=cv2.imread("/home/user/Pictures/pngtree-group-of-girls-posing-for-a-picture-picture-image_2781639.jpg")
# print(img2)

#to show image

# cv2.imshow('second_image',img2)
# cv2.imshow('group_photo',img)
# cv2.waitKey(5000)       #how long in milliseconds
# cv2.destroyAllWindows()

# ## to convert image to greyscle
grey_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# cv2.imshow('grey',grey_image)
# cv2.waitKey(5000) 
# cv2.destroyAllWindows()

# (thresh,bw_img)=cv2.threshold(grey_image,97,255,cv2.THRESH_BINARY| cv2.THRESH_OTSU)
# print(thresh)

# cv2.imshow('grey',bw_img)
# cv2.waitKey(5000) 
# cv2.destroyAllWindows()


# #To save image

# cv2.imwrite('/home/user/Pictures/greyimage.jpg',grey_image)

# to resize image 
# resized_image = cv2.resize(img,(720,480))


#to check the size of the image
print(img.shape)


# #to create a rectangle in image
# img=cv2.rectangle(img,pt1=(200,400),pt2=(300,600),color=(255,0,0),thickness=5)
# cv2.imshow('rectangle_image',img)
# cv2.waitKey() 
# cv2.destroyAllWindows()

# #circle

# img=cv2.circle(img,center=(200,400),radius=100,color=(0,255,0),thickness=5)
# cv2.imshow('rcircle_image',img)
# cv2.waitKey() 
# cv2.destroyAllWindows()

# #text
# img=cv2.putText(
#             img,
#             text="Group_PHOTO",
#             org=(200,300),
#             fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=3,
#             color=(0,0,255),
#             thickness=5)
# cv2.imshow('textimage',img)
# cv2.waitKey() 
# cv2.destroyAllWindows()


######

img=cv2.rectangle(img,pt1=(30,200),pt2=(900,500),color=(255,0,0),thickness=-1)
img=cv2.circle(img,center=(175,350),radius=150,color=(0,255,0),thickness=-1)
img=cv2.putText(
            img,
            text="Group_PHOTO",
            org=(400,300),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=2,
            color=(0,0,255),
            thickness=5)
cv2.imshow('textimage',img)
cv2.waitKey() 
cv2.destroyAllWindows()