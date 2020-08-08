import cv2


video = cv2.VideoCapture('video/Pedestrian.mp4')
#Our pre-trained car and pedestrian classifiers
car_tracker_file= 'xml/car_detector.xml'
pedestrian_tracker_file = 'xml/Pedestrian.xml'

#create car classifier
car_tracker = cv2.CascadeClassifier(car_tracker_file)
pedestrian_tracker = cv2.CascadeClassifier(pedestrian_tracker_file)

while True:
    #Read the current Frae
    (read_successful, frame) = video.read()

    #safe coding
    if read_successful:
        grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break

    #detect car and pedestrian
    cars = car_tracker.detectMultiScale(grayscaled_frame)
    pedestrian = pedestrian_tracker.detectMultiScale(grayscaled_frame)

    for(x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y),(x+w , y+h), (0 ,0, 255), 2 )

    for(x, y, w, h) in pedestrian:
        cv2.rectangle(frame, (x, y),(x+w , y+h), (0 ,255, 255), 2 )
    # # #Display the image with the faces spotted
    cv2.imshow('Clever Programmer Car Detector', frame)

    #Dont autoclose
    key = cv2.waitKey(1)

    #stop  if Q key is pressed
    if  key==81 or key ==113:
        break

#Realese the video capture objec
video.release()

# #create opencv image
# img_file = 'test.jpg'
# img = cv2.imread(img_file)
#
# #create classifier(needed for haar cascade)
# car_tracker = cv2.CascadeClassifier(classifier_file)
#
# #conver to grayscale
# black_n_white = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# #detect cars
# cars = car_tracker.detectMultiScale(black_n_white)
#
# for(x, y, w, h) in cars:
#     cv2.rectangle(img, (x, y),(x+w , y+h), (0 ,0, 255), 2 )
#
# #Display the image with the faces spotted
# cv2.imshow('Clever Programmer Car Detector', img)
#
# #Dont autoclose
# cv2.waitKey()
print("Code Completed")
