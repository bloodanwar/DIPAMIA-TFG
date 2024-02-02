import mediapipe as mp
import cv2 
import numpy as np
import time
import csv

def getVisibleLandmarks(pose_landmarker_result):
        visible_landmarks = []
        if pose_landmarker_result.pose_landmarks:
            for normalized_landmarks in pose_landmarker_result.pose_landmarks:
                for i, landmarks in enumerate(normalized_landmarks):
                    if landmarks.visibility > 0.5:  # Adjust visibility threshold as needed
                        visible_landmarks.append(i)
        return visible_landmarks
        
class StepCounter:
    def __init__(self):
        
        self.prev_heights = None
        self.steps = 0
        self.lftFeet = [27, 29, 31]
        self.rgtFeet = [28, 30, 32]

        self.errorMargin = 0.1 #Error margin to avoid the jittering of the landmarks

    def count_steps(self, visible_landmarks,pose_landmarker):
       if set(self.lftFeet).issubset(set(visible_landmarks)) and set(self.rgtFeet).issubset(set(visible_landmarks)):
            #print("countingSteps")
            leftFeet_heights = []
            rightFeet_heights = []
            for normalized_landmarks in pose_landmarker.pose_landmarks:
                for i, landmarks in enumerate(normalized_landmarks):
                    if i  in self.lftFeet:
                    # Extract the heights of feet landmarks
                        leftFeet_heights.append(landmarks.y)
                    if i in self.rgtFeet:
                        rightFeet_heights.append(landmarks.y)

                    # Check if previous heights are available
            if self.prev_heights is not None:
                # Check for exchange of height between feet
                if (min(leftFeet_heights) > (max(self.prev_heights[1])) and
                        max(rightFeet_heights) < (min(self.prev_heights[0]))):
                    self.steps += 1
                    print ("StepCounted")

            # Update previous heights
            self.prev_heights = (leftFeet_heights, rightFeet_heights)

    def get_total_steps(self):
        return self.steps

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
        self.joint_colors = [(0, 255, 0) if i < 11 else (255, 0, 0) if i in [11, 13, 21, 15, 19, 17, 23, 25, 27, 29, 31] else (0, 0, 255) for i in range(33)]
        self.connection_color = (255,255,255)
        self.connection_thickness = 5
        self.joint_radius = 11
        self.connections = mp.solutions.pose.POSE_CONNECTIONS


    def draw(self, frame, pose_landmarker_result,writer):
        if pose_landmarker_result.pose_landmarks:
            for normalized_landmarks in pose_landmarker_result.pose_landmarks:
                for i, landmarks in enumerate(normalized_landmarks):
                    x = int(landmarks.x * self.width)
                    y = int(landmarks.y * self.height)
                    z = float(landmarks.z)
                    if x < 0 or x > self.width or y < 0 or y > self.height:
                        continue
                    cv2.circle(frame, (x, y), self.joint_radius, self.joint_colors[i], -1)
                    writer.writerow([i,landmarks.x,landmarks.y,landmarks.z])
                    
                
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

    file = open('export.csv','w', newline='')
    writer = csv.writer(file)
    writer.writerow(['Point','x','y','z'])

    cap = cv2.VideoCapture(0)
    # set to 30 fps
    cap.set(cv2.CAP_PROP_FPS, 30)

    frame_draw = FrameDraw(cap)
    pose_detector = PoseDetector("heavy", min_detection_confidence, min_pose_presence_confidence, min_tracking_confidence, num_poses, output_segmentation_masks)
    step_counter = StepCounter()
    
    while True:
        ret,frame = cap.read()
        pose_landmarker_result = pose_detector.detectPose(frame)

        # Check for steps
        step_counter.count_steps(getVisibleLandmarks(pose_landmarker_result),pose_landmarker_result)


        frame_draw.draw(frame, pose_landmarker_result,writer)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Number of steps:", step_counter.get_total_steps())
            file.close()
            break







