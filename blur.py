import cv2
import os
import numpy as np

directory_in="/home/kuz22/additional_programs/pix2pix/datasets/edges2handbags_original/train/"
directory_out="/home/kuz22/additional_programs/pix2pix/datasets/edges2handbags/train/"
#directory_in="/home/victor/AAR/bin/"
#directory_out="/home/victor/AAR/"
imglist=filter( lambda f: f.endswith(".jpg"), os.listdir(directory_in)) # ignore hidden folders like .DS_Store
#imglist=["1_AB.jpg","2_AB.jpg"]
E=np.zeros((256,256,3))
for img in imglist:
    M=cv2.imread(os.path.join(directory_in,img),cv2.IMREAD_COLOR)
    N=M[:,0:256,0] #assuming that M is RGB, which it likely is
    N = cv2.GaussianBlur(N,(9,9),0)
    ret,N=cv2.threshold(N,245,255,cv2.THRESH_BINARY)
    E[:,:,0]=N
    E[:,:,1]=N
    E[:,:,2]=N
    out=np.concatenate((E,M[:,256:,:]),1)
    cv2.imwrite(directory_out+img,out)
