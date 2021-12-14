import cv2
import dropbox
import time
import random

start_time=time.time()

def take_snapshot():
    number=random.randint(0,100)
    #initializing cv2 ,starts webcam
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        #read the  frames while the cam is on
        ret,frame=videoCaptureObject.read()
        #save the image

        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time
        result=False
    return img_name
    print("snapshot taken") 
    # release the camera
    videoCaptureObject.release()
    #close all windows
    cv2.destroyAllWindows()


def upload_file(img_name):
    access_token="PjC49KuFbfwAAAAAAAAAATc5NhbD7ewOBIdQ6Huwt_oTbexGKk198DTG4uMQZQcI" 
    file=img_name
    file_from=file
    file_2="/testFolder/"+(img_name)   
    dbx=dropbox.Dropbox(access_token)  

    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_2,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")


def main():
    while(True):
        if((time.time()-start_time)>=120):
            name=take_snapshot()
            upload_file(name)

main()











    