# Task 4: Object Detection and Tracking

A real-time object detection and multi-object tracking application built with **Python, OpenCV, YOLOv8, and ByteTrack**.

## Features
- Webcam input or prerecorded video input
- Pretrained YOLOv8 Nano object detector
- ByteTrack tracking with persistent IDs across frames
- Bounding boxes, class labels, confidence scores, object count, and FPS
- Optional saving of the annotated output video
- Simple command-line configuration

## 1. Requirements
- Python 3.9–3.12 (recommended)
- Webcam for live mode, or an MP4/AVI video file
- Internet connection on the first run to download YOLO weights

## 2. Installation

Open a terminal in this project folder.

```bash
python -m venv .venv
```

Activate the environment:

**Windows**
```bash
.venv\Scripts\activate
```

**macOS / Linux**
```bash
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 3. Run the project

**Webcam (default camera 0):**
```bash
python main.py
```

**Video file:**
```bash
python main.py --source input.mp4
```

**Use a different webcam:**
```bash
python main.py --source 1
```

**Adjust confidence threshold and model:**
```bash
python main.py --source input.mp4 --conf 0.45 --model yolov8s.pt
```

**Run without saving an output video:**
```bash
python main.py --source 0 --no-save
```

Press **Q** or **Esc** in the video window to stop.

## 4. Output
By default, the annotated video is saved to:

`output/tracked_output.mp4`

The first execution downloads `yolov8n.pt` automatically. Keep an internet connection available for this initial download.

## 5. How it works
1. OpenCV reads frames from the webcam or video file.
2. YOLOv8 predicts object classes, bounding boxes, and confidence scores.
3. ByteTrack associates detections across consecutive frames and assigns tracking IDs.
4. OpenCV draws each bounding box and its class, ID, and confidence on the frame.
5. The application displays the processed frame and optionally writes it to an MP4 file.

## Troubleshooting
- **Camera not opening:** Close other applications using the webcam; try `--source 1`.
- **Video not found:** Put the video in this folder and pass its correct filename.
- **Slow performance:** Use the default `yolov8n.pt`, lower camera resolution, or use a smaller input video.
- **Window does not appear:** Run the script on a desktop session with GUI support; `cv2.imshow` does not work in many headless environments.
- **First run takes time:** YOLO model weights are downloaded once and cached.

## Project structure
```text
object_detection_tracking_project/
├── main.py
├── requirements.txt
├── README.md
├── PROJECT_REPORT.md
└── output/
```
