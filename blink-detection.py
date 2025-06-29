"""
Beginnings of the blink detection
"""

# For retrieving the webcam video
import cv2
# For finding the face/eyes
import mediapipe

# We start by capturing the video from the computer's webcam, index 0.
webcam = cv2.VideoCapture(0)

face_mesh = mediapipe.solutions.face_mesh.FaceMesh()

# Now, we set the while loop to continuously turn the video into what we want (eye/blink detection)
running = True
while running:
    frame_captured, frame = webcam.read()  # 1st variable is to tell whether the frame was captured
    # 2nd variable the actual frame--None if there is no frame.

    # correctedColorFrame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

    # Show the frame in a window so we see what we are doing:
    if frame_captured:
        cv2.imshow("Dev Video Capture", frame)
        cv2.waitKey(1)  # Wait 1 millisecond (or until a key is pressed) to change the frame

    else:
        print("Frame unavailable. Check webcam")
