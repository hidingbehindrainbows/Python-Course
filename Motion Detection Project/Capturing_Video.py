import cv2, pandas
from datetime import datetime

video = cv2.VideoCapture(0)

first_frame = None
key:int =None
status_list = []
times = []

df = pandas.DataFrame(columns=("Start", "End"))


while key!= ord("q"):
    
    check, frame = video.read()
    status = 0
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21,21), 0)
    
    if first_frame is None:
        first_frame = gray
        continue
    
    delta_frame = cv2.absdiff(first_frame, gray)
#                                                  ,white colour,
    threshold_delta = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    threshold_delta = cv2.dilate(threshold_delta, None, iterations=2) #smoothning out the threshold thing 
    
    
    cnts = cv2.findContours(threshold_delta.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    
    
    for contour in cnts:
        if cv2.contourArea(contour) <10000:  #size of the moving object, changable
            continue
        status = 1
        # print(status)
        (x,y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 3)
    
    if len(status_list) > 1:
        if status_list[-1] == 1 and status_list[-2] == 0:
            times.append(datetime.now())
        if status_list[-1] == 0 and status_list[-2] == 1:
            times.append(datetime.now())
        
    
    
    status_list.append(status)
    
    
    cv2.imshow("Gray Frame", gray)
    cv2.imshow("Difference", delta_frame)
    cv2.imshow("Threshold delta", threshold_delta)
    cv2.imshow("Frame with motion detection", frame)

    key = cv2.waitKey(1)


times.append(datetime.now())
if len(times) %2 != 0:
    times.append(datetime.now())

for i in range(0,len(times), 2):
    # df = pandas.concat((df, pandas.DataFrame.from_records(({"Start":(times[i],), "End":(times[i+1],)}))))
    df.loc[len(df), df.columns] = (times[i], times[i+1])


df.to_csv("C:\\mycode\\python\\Functions\\open_cv\\Times.csv")
video.release()
cv2.destroyAllWindows()
