# Project Report: Object Detection and Tracking

## 1. Title
Real-Time Object Detection and Tracking Using YOLOv8, ByteTrack, and OpenCV

## 2. Objective
The objective is to detect multiple objects in a live webcam stream or video file, identify their classes, track them across frames, and display bounding boxes with unique tracking IDs.

## 3. Tools and Technologies
- **Python:** Main programming language.
- **OpenCV:** Video capture, frame processing, drawing, display, and video writing.
- **YOLOv8:** Pre-trained deep-learning object detector.
- **ByteTrack:** Multi-object tracking algorithm used to associate detections across frames.

## 4. Methodology
1. Capture frames from a webcam or video file using OpenCV.
2. Pass each frame to the pretrained YOLOv8 model.
3. Obtain detected object coordinates, class IDs, and confidence scores.
4. Use ByteTrack to associate detections between frames and maintain object identities.
5. Draw bounding boxes and display the object class, tracking ID, and confidence.
6. Display the annotated frame and optionally save the processed video.

## 5. Expected Output
The application opens a live video window. Detected objects are enclosed in bounding boxes and annotated with their class names, tracking IDs, and confidence values. The display also shows the current object count and approximate processing FPS. The processed video is saved as `output/tracked_output.mp4` unless saving is disabled.

## 6. Advantages
- Supports both webcam and prerecorded video.
- Uses pretrained weights, so no custom training dataset is required.
- Lightweight YOLOv8 Nano model is suitable for quick setup.
- Tracking IDs help distinguish objects across frames.
- Output can be saved for later review.

## 7. Limitations
- Detection quality depends on lighting, camera quality, object size, and occlusion.
- Tracking IDs can change when objects disappear for a long time or become heavily occluded.
- Real-time FPS depends on the computer's CPU/GPU and input resolution.
- The pretrained model recognizes its supported classes; custom classes require model training.

## 8. Conclusion
The project demonstrates a complete object detection and tracking pipeline. YOLOv8 detects objects in each frame, ByteTrack associates detections over time, and OpenCV visualizes and records the results. The system supports both live webcam input and video-file input.
