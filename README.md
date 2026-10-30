# 🚀 Real-Time Object Detection and Tracking

A Python-based real-time object detection and tracking system using **YOLOv8, OpenCV, and ByteTrack**. This project detects multiple objects in live webcam streams or video files, draws bounding boxes, assigns tracking IDs, and displays object information in real time.

## 📌 Project Overview

The main objective of this project is to detect and track objects in video frames using a pretrained deep-learning model.

The system identifies objects, displays their names, tracks their movement across frames, and provides unique tracking IDs.

## ✨ Features

- Real-time object detection using YOLOv8.
- Webcam and video-file input support.
- Multi-object tracking using ByteTrack.
- Bounding boxes around detected objects.
- Object names and tracking IDs.
- Detection confidence scores.
- Real-time FPS display.
- Automatic output video saving.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.12 | Programming language |
| OpenCV | Video processing and webcam access |
| YOLOv8 | Object detection |
| ByteTrack | Object tracking |
| Ultralytics | YOLO model implementation |

## 📂 Project Structure

```text
Object-Detection-and-Tracking/
│
├── main.py
├── requirements.txt
├── README.md
├── PROJECT_REPORT.md
│
└── output/
    └── tracked_output.mp4
```

## ⚙️ Installation

**Step 1: Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/Object-Detection-and-Tracking.git
```

**Step 2: Navigate to the project directory**

```bash
cd Object-Detection-and-Tracking
```

**Step 3: Install the required libraries**

```bash
pip install -r requirements.txt
```

## ▶️ How to Run

**Run using webcam:**

```bash
python main.py
```

**Run using a video file:**

```bash
python main.py --source input.mp4
```

**Change confidence threshold:**

```bash
python main.py --conf 0.5
```

**Run without saving output:**

```bash
python main.py --no-save
```

Press `Q` or `ESC` to stop the application.

## 📊 Expected Output

The application displays:

- Detected object names.
- Bounding boxes around objects.
- Unique tracking IDs.
- Confidence scores.
- Number of detected objects.
- Frames per second (FPS).

The processed video is automatically saved in the `output` folder as:

`tracked_output.mp4`

## 🧠 Working Methodology

1. Capture video frames using OpenCV.
2. Pass each frame to the pretrained YOLOv8 model.
3. Detect objects and obtain bounding boxes.
4. Use ByteTrack to associate objects across consecutive frames.
5. Assign tracking IDs to detected objects.
6. Draw bounding boxes, labels, and IDs.
7. Display and save the processed video.

## ⚠️ Limitations

- Detection accuracy depends on lighting and video quality.
- Objects outside the model's trained categories may be misclassified.
- Tracking IDs may change when objects are heavily occluded.
- Performance depends on available CPU/GPU resources.

## 🔮 Future Improvements

- Train a custom YOLO model for additional object classes.
- Improve detection accuracy.
- Add object counting and movement analysis.
- Build a graphical user interface.
- Support multiple camera inputs.

## 🎯 Conclusion

This project demonstrates real-time object detection and multi-object tracking using YOLOv8, OpenCV, and ByteTrack. It provides a practical implementation of computer vision techniques for identifying and tracking multiple objects in video streams.

## 👨‍💻 Author

**Shaik Imdadulla**

GitHub: https://github.com/Sabeel-18

---

⭐ If you find this project useful, consider giving it a star!v
