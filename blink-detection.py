"""
Beginnings of the blinking detection
"""

# For retrieving the webcam video
import cv2
# For finding the face/eyes
import mediapipe
# For detecting keyboard inputs (JUST FOR PROTOTYPE--WILL BE REMOVED IN FINAL VERSION)
from pynput import keyboard
# For doing the mouse clicks
from pynput.mouse import Button, Controller

# We begin by setting up the variable for the while loop.
running = True
eye_contour = [362, 385, 387, 263, 373, 380]
eye_contour_coords = [[], [], [], [], [], []]
eye_aspect_ratio = None
blinking = False


# Upon pressing the Esc key, we will end the loop
def on_key_press(key):
    global running
    if key == keyboard.Key.esc:
        running = False


listener = keyboard.Listener(on_press=on_key_press)
listener.start()

mouse = Controller()

# We start by capturing the video from the computer's webcam, index 0.
webcam = cv2.VideoCapture(0)

face_mesh = mediapipe.solutions.face_mesh.FaceMesh(refine_landmarks=True)  # We need refined_landmarks to be True, as
# an essential landmark within in eye is only shown with this setting enabled. There will be a total of 478 landmarks

while running:
    frame_captured, frame = webcam.read()  # 1st variable is to tell whether the frame was captured
    # 2nd variable the actual frame--None if there is no frame.
    frame = cv2.flip(frame, 1)

    correctedColorFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(correctedColorFrame)
    face_landmarks = output.multi_face_landmarks

    # print(face_landmarks)  # When there is no face in the frame, or it's hidden, this prints None

    if face_landmarks is not None:
        # From .multi_face_landmarks, we assume that there are MULTIple faces. We only want one, so we specify the
        # index as 0
        landmarks = face_landmarks[0].landmark

        frame_h = frame.shape[0]  # 480
        frame_w = frame.shape[1]  # 640

        # TODO: We retrieve the coordinates of the landmarks so we can draw them in the for-loop. REMOVE DRAWING LATER.
        lm_num = -1
        for lm in eye_contour:
            lm_num += 1
            # lm.x and lm.y give us a decimal number relating to the percent of the screen the face landmark is located.
            # For example, if the landmark is exactly in the middle of the screen, lm.x = 0.5, lm.y = 0.5.
            # Thus, we must multiply this by the frame's width and height (defined earlier), and wrap all of this in
            # int(), as the result is still fractional
            lm_x = int(landmarks[lm].x * frame_w)
            lm_y = int(landmarks[lm].y * frame_h)
            # print(lm_x, lm_y)

            eye_contour_coords[lm_num] = [lm_x, lm_y]

            # Now, we draw the circle indicating the position of the landmark:
            cv2.circle(img=frame, center=(lm_x, lm_y), radius=2, color=(255, 150, 0), thickness=1, lineType=1, shift=0)

        # Calculate Eye Aspect Ratio (EAR)--if it's less than 0.15, the user is most likely blinking/winking
        diff_p1_p5 = abs(eye_contour_coords[1][1] - eye_contour_coords[5][1])
        diff_p2_p4 = abs(eye_contour_coords[2][1] - eye_contour_coords[4][1])
        diff_p0_p3 = abs(eye_contour_coords[0][0] - eye_contour_coords[3][0])
        denom_weight = 2
        eye_aspect_ratio = (diff_p1_p5 + diff_p2_p4)/(denom_weight * diff_p0_p3)

        if eye_aspect_ratio <= 0.15 and not blinking:
            blinking = True
            print("Blink! " + str(eye_aspect_ratio))
            mouse.click(Button.right)
        elif eye_aspect_ratio >= 0.15 and blinking:
            blinking = False

    # Show the frame in a window so we see what we are doing:
    if frame_captured:
        cv2.imshow("Dev Video Capture", frame)
        cv2.waitKey(50)  # Wait 100 milliseconds (or until a key is pressed) to change the frame

    else:
        print("Frame unavailable. Check webcam")

# After the loop has ended, stop listening for key presses and end the program.
listener.stop()
