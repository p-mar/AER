import cv2


def video_divider(video_name):   
    vidcap = cv2.VideoCapture("media\\videos\\"+video_name)
    frames = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    success,image = vidcap.read()
    count = 1
    while success:
        cv2.imwrite("ferapp\ml_model\\video_mode\\frames\\frame%d.jpg" % count, image)      
        success,image = vidcap.read()
        count += 1
        if count==10:
            break
    
    vidcap.release()
    return fps, frames
