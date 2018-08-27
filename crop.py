import cv2
import numpy as np
import os
from ftplib import FTP
ftp=FTP()
ftp.connect('10.245.13.3',2121)
ftp.login('demo','notadmin')
imglist=ftp.nlst()
ftp.retrbinary('RETR '+imglist[len(imglist)-83],open(imglist[len(imglist)-83],'wb').write)
ftp.retrbinary('RETR '+imglist[len(imglist)-84],open(imglist[len(imglist)-84],'wb').write)
ftp.quit()
#file retrieval complete
directory_in="/home/victor/AAR/demo/"
directory_blurred="/home/victor/AAR/demo/blurred/"
imglist=filter( lambda f: f.endswith(".jpg"), os.listdir(directory_in)) # ignore hidden folders like .DS_Store
for img in imglist:
    M=cv2.imread(directory_in+img,0)
    M=cv2.resize(M,(480,360))
    #cv2.imwrite('small'+img,M)
    #M=M[128:384,128:384,:]
    M=M[104:,112:368]
    #N=np.add(M[:,:,0]/3,M[:,:,1]/3)
    #N=np.add(N,M[:,:,2]/3)
    #cv2.imwrite("/home/victor/AAR/demo/archive_photos/"+img,N)
    ret,M=cv2.threshold(M,165,255,cv2.THRESH_BINARY)
    cv2.imwrite(directory_in+img,M)
    M = cv2.GaussianBlur(M,(9,9),0)
    ret,M=cv2.threshold(M,235,255,cv2.THRESH_BINARY)
    cv2.imwrite(directory_blurred+img,M)
