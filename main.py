"""
Task 4 - Object Detection and Tracking
YOLOv8 Nano + ByteTrack + OpenCV

Examples:
  python main.py                         # webcam (default camera 0)
  python main.py --source 0              # webcam
  python main.py --source input.mp4      # video file
  python main.py --source input.mp4 --no-save
  python main.py --source 0 --conf 0.4 --model yolov8s.pt
"""

import argparse
from pathlib import Path
import time

import cv2
from ultralytics import YOLO


def parse_args():
    parser = argparse.ArgumentParser(
        description="Real-time object detection and tracking with YOLOv8 and ByteTrack."
    )
    parser.add_argument(
        "--source", default="0",
        help="Webcam index (0, 1, ...) or path to a video file. Default: 0"
    )
    parser.add_argument("--model", default="yolov8n.pt",
                        help="Ultralytics model weights. Default: yolov8n.pt")
    parser.add_argument("--conf", type=float, default=0.35,
                        help="Minimum detection confidence (0-1). Default: 0.35")
    parser.add_argument("--save", dest="save", action="store_true",
                        help="Save annotated video (default).")
    parser.add_argument("--no-save", dest="save", action="store_false",
                        help="Do not save annotated video.")
    parser.set_defaults(save=True)
    parser.add_argument("--output", default="output/tracked_output.mp4",
                        help="Output video path.")
    parser.add_argument("--camera-width", type=int, default=1280)
    parser.add_argument("--camera-height", type=int, default=720)
    return parser.parse_args()


def main():
    args = parse_args()

    # A numeric source selects a webcam; otherwise use the supplied video path.
    source = int(args.source) if args.source.isdigit() else args.source
    if isinstance(source, str) and not Path(source).is_file():
        raise FileNotFoundError(f"Input video not found: {source}")

    print(f"[INFO] Loading model: {args.model}")
    # The first run downloads the pretrained weights automatically.
    model = YOLO(args.model)

    cap = cv2.VideoCapture(source)
    if not cap.isOpened():
        raise RuntimeError(f"Could not open video source: {args.source}")

    if isinstance(source, int):
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, args.camera_width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, args.camera_height)

    fps_in = cap.get(cv2.CAP_PROP_FPS)
    if not fps_in or fps_in <= 1:
        fps_in = 30.0

    writer = None
    if args.save:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)

    frame_count = 0
    prev_time = time.perf_counter()
    smoothed_fps = 0.0

    print("[INFO] Detection started. Press Q or ESC to quit.")
    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                break

            # persist=True keeps tracker identities consistent between frames.
            results = model.track(
                frame,
                persist=True,
                tracker="bytetrack.yaml",
                conf=args.conf,
                verbose=False
            )
            result = results[0]

            # Create the output writer once the actual frame size is known.
            if args.save and writer is None:
                h, w = frame.shape[:2]
                writer = cv2.VideoWriter(
                    str(output_path),
                    cv2.VideoWriter_fourcc(*"mp4v"),
                    fps_in,
                    (w, h)
                )
                if not writer.isOpened():
                    raise RuntimeError(f"Could not create output video: {output_path}")

            object_count = 0
            if result.boxes is not None:
                boxes = result.boxes
                ids = boxes.id
                for i, box in enumerate(boxes):
                    x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
                    cls_id = int(box.cls[0].item())
                    confidence = float(box.conf[0].item())
                    track_id = int(ids[i].item()) if ids is not None else -1
                    class_name = model.names.get(cls_id, str(cls_id))
                    object_count += 1

                    # Draw bounding box and readable label.
                    color = (40, 210, 80)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                    id_text = f"ID {track_id}" if track_id >= 0 else "ID --"
                    label = f"{class_name} | {id_text} | {confidence:.2f}"
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    (tw, th), baseline = cv2.getTextSize(label, font, 0.55, 2)
                    label_y = max(y1, th + 10)
                    cv2.rectangle(frame, (x1, label_y - th - 8),
                                  (x1 + tw + 6, label_y + baseline - 4), color, -1)
                    cv2.putText(frame, label, (x1 + 3, label_y - 4),
                                font, 0.55, (0, 0, 0), 2, cv2.LINE_AA)

            # Smooth FPS estimate to reduce display flicker.
            now = time.perf_counter()
            elapsed = now - prev_time
            prev_time = now
            current_fps = 1.0 / elapsed if elapsed > 0 else 0.0
            smoothed_fps = current_fps if smoothed_fps == 0 else (
                0.9 * smoothed_fps + 0.1 * current_fps
            )
            frame_count += 1

            cv2.rectangle(frame, (10, 10), (275, 78), (25, 25, 25), -1)
            cv2.putText(frame, f"Objects: {object_count}", (20, 37),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 2)
            cv2.putText(frame, f"FPS: {smoothed_fps:.1f}", (20, 65),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 255, 255), 2)

            if writer is not None:
                writer.write(frame)

            cv2.imshow("YOLOv8 Object Detection and Tracking", frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q") or key == 27:
                break

    finally:
        cap.release()
        if writer is not None:
            writer.release()
        cv2.destroyAllWindows()

    print(f"[INFO] Processed {frame_count} frames.")
    if args.save and frame_count:
        print(f"[INFO] Annotated video saved to: {args.output}")


if __name__ == "__main__":
    main()
