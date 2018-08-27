import cv2
import numpy as np
import os
original="/home/victor/AAR/demo/"
original_out="/home/victor/AAR/demo/original_output/"
blurred="/home/victor/AAR/demo/blurred/"
blurred_out="/home/victor/AAR/demo/blurred_output/"
directory_out="/home/victor/AAR/demo/display/"
imglist=filter( lambda f: f.endswith(".jpg"), os.listdir(original)) # ignore hidden folders like .DS_Store
original1=cv2.imread(original+imglist[0])
original2=cv2.imread(original+imglist[1])
imglist=filter( lambda f: f.endswith(".jpg"), os.listdir(original_out)) # ignore hidden folders like .DS_Store
original_out1=cv2.imread(original_out+imglist[0])
original_out2=cv2.imread(original_out+imglist[1])
imglist=filter( lambda f: f.endswith(".jpg"), os.listdir(blurred)) # ignore hidden folders like .DS_Store
blurred1=cv2.imread(blurred+imglist[0])
blurred2=cv2.imread(blurred+imglist[1])
imglist=filter( lambda f: f.endswith(".jpg"), os.listdir(blurred_out)) # ignore hidden folders like .DS_Store
blurred_out1=cv2.imread(blurred_out+imglist[0])
blurred_out2=cv2.imread(blurred_out+imglist[1])

side=cv2.imread("/home/victor/AAR/demo/side.png")
bottom=cv2.imread("/home/victor/AAR/demo/bottom.png")
top=cv2.imread("/home/victor/AAR/demo/top.png")
tmp1=np.concatenate((original1,blurred1),1)
tmp2=np.concatenate((original_out1,blurred_out1),1)
tmp1=np.concatenate((tmp1,tmp2,bottom))
tmp1=np.concatenate((side,tmp1),1)
cv2.imwrite(directory_out+imglist[0],tmp1)
tmp2=np.concatenate((original2,blurred2),1)
tmp3=np.concatenate((original_out2,blurred_out2),1)
tmp3=np.concatenate((tmp2,tmp3,bottom))
tmp3=np.concatenate((side,tmp3),1)
cv2.imwrite(directory_out+imglist[1],tmp3)
tmp2=np.concatenate((tmp1,tmp3),1)
tmp3=np.concatenate((top,tmp2))
cv2.imshow('Results',tmp3)
cv2.waitKey(0)
cv2.destroyAllWindows()
