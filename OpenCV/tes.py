import mediapipe as mp
import cv2

mp_face_detection = mp.solutions.face_detection
mp_drawing        = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_holistic       = mp.solutions.holistic

# For webcam input:
cap = cv2.VideoCapture(0)


with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.8) as face_detection:
    with mp_holistic.Holistic(min_detection_confidence = 0.8, min_tracking_confidence = 0.8) as holistic:

        def run_tracking( cap ):
            if cap.isOpened():
                success, image = cap.read()
                image = cv2.flip(image, 1)
                if not success:
                    return False 
                center_x_shooter = int(image.shape[1] * 0.5)
                center_y_shooter = int(image.shape[0] * 0.5)
                # To improve performance, optionally mark the image as not writeable to
                # pass by reference.
                image.flags.writeable = False
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                results = holistic.process(image)
                mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS, landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
                # coordinates = (left eye + right eye / 2) * screen center
                x_shooter = int((results.pose_landmarks.landmark[2].x + results.pose_landmarks.landmark[5].x) * center_x_shooter)
                y_shooter = int((results.pose_landmarks.landmark[2].y + results.pose_landmarks.landmark[5].y) * center_y_shooter)
                distance_shooter_center_x = center_x_shooter - x_shooter
                distance_shooter_center_y = center_y_shooter - y_shooter
                cv2.line(image, (x_shooter, y_shooter), (center_x_shooter, center_y_shooter), (255, 255, 255), 4)
                cv2.putText(image, f'x:{x_shooter} y:{y_shooter}', (x_shooter, y_shooter - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)  # hypotenuse
                cv2.line(image, (x_shooter, center_y_shooter), (center_x_shooter, center_y_shooter), (255, 255, 255), 2)
                cv2.putText(image, f'{distance_shooter_center_x}', (x_shooter, center_y_shooter + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)  # x
                cv2.line(image, (center_x_shooter, y_shooter), (center_x_shooter, center_y_shooter), (255, 255, 255), 4)
                cv2.putText(image, f'{distance_shooter_center_y}', (center_x_shooter + 20, y_shooter + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)  # y
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                cv2.imshow('MediaPipe Face Detection', image )
            return True 
            