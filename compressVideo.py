import sys as s
import os
import cv2

if __name__ == '__main__':

    if len(s.argv)!=3:
        print("3 parameters are required to be entered")
        s.exit()
    if int(s.argv[2])<1 or int(s.argv[2])>99:
        print("X should lie between 1 and 99 only")
        s.exit()
    if not os.path.exists(s.argv[1]):
        print("File not Found")
        s.exit()
    if not s.argv[1].endswith(".mp4") or s.argv[1].endswith(".wav") or s.argv[1].endswith(".waw"):
        print("File must be of video type only")
        s.exit()    

    try:
        if not os.path.exists('Compressed_Frames'):
            os.mkdir('Compressed_Frames')
    except OSError as o:
        print("Error in creating the folder")
        s.exit()    

    video=cv2.VideoCapture(s.argv[1])
    os.chdir('./Compressed_Frames')
    frames_per_sec=video.get(cv2.CAP_PROP_FPS)       
    if video.isOpened()==False:
        print("Some Error occured while reading the video file ")
        s.exit()    
    else:
        success,img=video.read()
        if success==True:
            h,w,layers=img.shape
            h1=int(h*int(s.argv[2])/100)
            w1=int(w*int(s.argv[2])/100)
            fourcc=cv2.VideoWriter_fourcc(*'mp4v')
            out=cv2.VideoWriter('video_output.mp4',fourcc,frames_per_sec,(w1,h1))

    count = 0
    while (True):
        success,img=video.read()
        if success==True:
            h, w, layers=img.shape
            h1=int(h*int(s.argv[2])/100)
            w1=int(w*int(s.argv[2])/100)
            resized=cv2.resize(img,(w1,h1))
            cv2.imwrite("Image"+str(count)+".jpg",resized)
            out.write(cv2.imread(("Image"+str(count)+".jpg")))
            count += 1
        else:
            break

    cv2.destroyAllWindows()
    out.release()
    video.release()