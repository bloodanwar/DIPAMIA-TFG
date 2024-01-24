import mediapipe as mp
import cv2 
import numpy as np
import time

class PoseDetector:

    models = {
        "lite": "./models/pose_landmarker_lite.task",
        "full": "./models/pose_landmarker_full.task",
        "heavy": "./models/pose_landmarker_heavy.task"
    }

    def __init__(self, model, min_detection_confidence, min_pose_presence_confidence, min_tracking_confidence, num_poses, output_segmentation_masks):
        
        model_path = self.models[model]
        PoseLandmarkerOptions = mp.tasks.vision.PoseLandmarkerOptions
        BaseOptions = mp.tasks.BaseOptions
        VisionRunningMode = mp.tasks.vision.RunningMode

        self.options = PoseLandmarkerOptions(
            base_options=BaseOptions(model_asset_path=model_path),
            running_mode=VisionRunningMode.VIDEO,
            min_pose_detection_confidence=min_detection_confidence,
            min_pose_presence_confidence=min_pose_presence_confidence,
            min_tracking_confidence = min_tracking_confidence,
            num_poses = num_poses,
            output_segmentation_masks=output_segmentation_masks
        )
        
        PoseLandmarker = mp.tasks.vision.PoseLandmarker
        self.landmarker = PoseLandmarker.create_from_options(self.options)
        self.timestamp = 0

    def detectPose(self, frame):
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
        pose_landmarker_result = self.landmarker.detect_for_video(mp_image, self.timestamp)
        self.timestamp += 33*1000 # 30 fps
        return pose_landmarker_result

        
class FrameDraw:

    def __init__(self, cap):
        
        # get frame
        ret, frame = cap.read()
        cv2.imshow('Video', frame)

        self.height, self.width, _ = frame.shape
        self.joint_colors = [(0, 255, 0) if i < 11 else (255, 0, 0) if i in [11, 13, 21, 15, 19, 17, 23, 25, 27, 29, 31] else (0, 0, 255) for i in range(32)]
        self.connection_color = (255,255,255)
        self.connection_thickness = 5
        self.joint_radius = 11
        self.connections = mp.solutions.pose.POSE_CONNECTIONS


    def draw(self, frame, pose_landmarker_result):
        if pose_landmarker_result.pose_landmarks:
            for normalized_landmarks in pose_landmarker_result.pose_landmarks:
                for i, landmarks in enumerate(normalized_landmarks):
                    x = int(landmarks.x * self.width)
                    y = int(landmarks.y * self.height)
                    z = float(landmarks.z)
                    if x < 0 or x > self.width or y < 0 or y > self.height:
                        continue
                    cv2.circle(frame, (x, y), self.joint_radius, self.joint_colors[i], -1)
                    print (i,x,y,z)
                
                for connection in self.connections:
                    x0 = int(normalized_landmarks[connection[0]].x * self.width)
                    y0 = int(normalized_landmarks[connection[0]].y * self.height)
                    x1 = int(normalized_landmarks[connection[1]].x * self.width)
                    y1 = int(normalized_landmarks[connection[1]].y * self.height)
                    cv2.line(frame, (x0, y0), (x1, y1), self.connection_color, self.connection_thickness)        

        cv2.imshow('Video', frame)


if __name__ == "__main__":

    min_detection_confidence = 0.5
    min_pose_presence_confidence = 0.5
    min_tracking_confidence = 0.5
    num_poses = 1
    output_segmentation_masks = False

    cap = cv2.VideoCapture(0)
    # set to 30 fps
    cap.set(cv2.CAP_PROP_FPS, 30)

    frame_draw = FrameDraw(cap)
        pose_detector = PoseDetector("heavy", min_detection_confidence, min_pose_presence_confidence, min_tracking_confidence, num_poses, output_segmentation_masks)
    
    while True:
        ret,frame = cap.read()
        pose_landmarker_result = pose_detector.detectPose(frame)
        frame_draw.draw(frame, pose_landmarker_result)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break







