import cv2
import sys as s
import os

if __name__ == '__main__':

    if len(s.argv)!=2:
        print("Only One parameter is required for this")
        s.exit()
    if not os.path.exists(s.argv[1]):
        print("File not found")
        s.exit()
    if not s.argv[1].endswith(".mp4") or s.argv[1].endswith(".wav") or s.argv[1].endswith(".waw"):
        print("File must be of video type only")
        s.exit()    

    if not os.path.exists('Video_Frames'):
        os.mkdir('Video_Frames')        
    video=cv2.VideoCapture(s.argv[1])
    os.chdir('./Video_Frames')
    if video.isOpened()==False:
        print("Some Error occured while reading the video file")
        s.exit()
    else:
        success,img=video.read()
        if success==True:
            h,w,layers=img.shape
            fourcc=cv2.VideoWriter_fourcc(*'mp4v')
            output=cv2.VideoWriter('video_output.mp4',fourcc,10,(w,h))

    i=0
    while(video.isOpened()):
        success,img=video.read()
        if success==True:
            gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            success,bw= cv2.threshold(gray,130,255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)            
            cv2.imwrite("Image"+str(i)+".png",bw)
            output.write(cv2.imread(("Image"+str(i)+".png")))
            i+=1
        else:
            break

    cv2.destroyAllWindows()
    output.release()