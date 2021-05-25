import cv2
import dropbox
import time
import random
startTime=time.time()
def takeSnapshot(): 
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result): 
        ret,frame=videoCaptureObject.read()
        imageName="img"+str(number)+".png"
        cv2.imwrite(imageName,frame)
        startTime=time.time()
        result=False
    return imageName
    print("Snapshot Taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()
def uploadFile(imageName): 
    accessToken='sl.AwphuB73syt4bHiIqW-hnyQi2kCI0gMazz3B2i63WWHBHaBkJNnIoMcM-yHorhoOQnrlw6mpBdgYkNqUxyXuM51YcRdJhTAxbWHb7Cf33fcrUhJ1zo27Aikga3EWHaLKwQRAEyc'
    file=imageName
    fileFrom=file
    file2="/NewFolder1/"+(imageName)
    dbx=dropbox.Dropbox(accessToken)
    with open(fileFrom,'rb') as f: 
        dbx.files_upload(f.read(),file2,mode=dropbox.files.WriteMode.overwrite)
        print("File Uploaded")
def main():
    while(True): 
        if((time.time()-startTime)>=10): 
            name=takeSnapshot()
            uploadFile(name)
main()