import cv2
import numpy as np
import os
dir_A="/home/kuz22/AAR/real_sketches/A"
B=np.zeros(shape=(256,256))
B+=255
dir_out="/home/kuz22/AAR/real_sketches/val"
imglist=filter( lambda f: f.endswith(".jpg"), os.listdir(dir_A)) # ignore hidden folders like .DS_Store
for img in imglist:
    M=cv2.imread(os.path.join(dir_A,img),cv2.IMREAD_COLOR)
    if(M.ndim==3):
        M=M[:,:,0]
    M=np.concatenate([M,B],1)
    cv2.imwrite(os.path.join(dir_out,img),M)
