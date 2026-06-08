"""YOLOv9-based shelf occupancy detector."""
import torch
import cv2
import numpy as np
from pathlib import Path

class ShelfOccupancyDetector:
    def __init__(self, model_path: str, confidence: float = 0.45):
        self.model = torch.hub.load("ultralytics/yolov9", "custom",
                                    path=model_path, force_reload=False)
        self.model.conf = confidence
        self.model.iou = 0.45
        self.classes = ["product_present", "empty_slot", "misplaced_product"]

    def analyze_frame(self, frame: np.ndarray) -> dict:
        results = self.model(frame)
        detections = results.pandas().xyxy[0]
        total_slots = len(detections)
        empty = len(detections[detections["name"] == "empty_slot"])
        occupancy = 1 - (empty / total_slots) if total_slots > 0 else 1.0
        return {"total_slots": total_slots, "empty_slots": empty,
                "occupancy_rate": round(occupancy, 4),
                "alert": empty > total_slots * 0.15,
                "detections": detections.to_dict("records")}

    def process_video_stream(self, camera_url: str):
        cap = cv2.VideoCapture(camera_url)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret: break
            result = self.analyze_frame(frame)
            if result["alert"]:
                yield result
        cap.release()
