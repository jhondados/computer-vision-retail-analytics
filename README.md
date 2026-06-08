# 👁️ Computer Vision Retail Analytics

[![YOLOv9](https://img.shields.io/badge/YOLOv9-Custom%20Fine--tuned-orange)](.)
[![Accuracy](https://img.shields.io/badge/Detection%20mAP-94.3%25-green)](.)
[![Cameras](https://img.shields.io/badge/Cameras-1%2C240-blue)](.)

> Real-time retail analytics system deployed across 1,240 cameras in 87 stores. Shelf occupancy detection (94.3% mAP), customer flow analysis, and automated planogram compliance saving R$8.2M annually.

## 🏆 Impact
- **R$8.2M/year** saved through optimized inventory restocking
- **94.3% mAP** on custom shelf/product detection dataset (320K annotated images)
- **1,240 cameras** across 87 stores processing in real-time
- **23% reduction in stockouts** via proactive restocking alerts

## 📊 Detection Capabilities
| Feature | Model | Accuracy | Latency |
|---------|-------|----------|---------|
| Shelf Occupancy | YOLOv9-custom | 94.3% mAP | 28ms |
| Customer Count | YOLO + Tracking | 97.1% | 31ms |
| Queue Length | Pose + Counting | 95.6% | 35ms |
| Planogram Check | ResNet + Siamese | 91.8% | 47ms |
