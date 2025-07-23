# Buoy Detection Model (buoy-model)

This page documents the MHSeals buoy detection model repository, which is used to train and run object detection models for buoys using YOLOv8 and Roboflow datasets.

---

## Overview

- **Repository:** [MHSeals/buoy-model](https://github.com/MHSeals/buoy-model)
- **Main Language:** Python
- **Framework:** YOLOv8 (Ultralytics)
- **Dataset:** Roboflow (customizable)

---

## Features

- Train custom buoy detection models using annotated datasets
- Supports Roboflow integration for easy dataset management
- Multiple run modes: test, detection, and tracking
- Easily adaptable to other datasets by modifying code

---

## How to Use

### 1. Clone the Repository
```bash
git clone https://github.com/MHSeals/buoy-model.git
```

### 2. Install Requirements
```bash
pip install -r requirements.txt
```

### 3. Train the Model
```bash
python train_annotated.py
```
- By default, downloads dataset from Roboflow.
- To use your own dataset, modify `train_annotated.py` to pass your own `Dataset` instance and remove Roboflow-specific code.

### 4. Retrieve Model Weights
- After training, weights are saved in `runs/detect/<version name>/weights/best.pt`.
- Location may vary (project root or Python installation root).

### 5. Run the Model
- **Test mode:**
  ```bash
  python detect_test.py
  ```
  - Runs on a folder of images, allows manual navigation.
- **Detection mode:**
  ```bash
  python detect_webcam.py
  ```
  - Runs detection on webcam input.
- **Tracking mode:**
  ```bash
  python detect_tracking.py
  ```
  - Runs object tracking on video input.

---

## Roboflow Integration

- Dataset and model management is streamlined with Roboflow.
- [Download Dataset](https://universe.roboflow.com/mhseals/buoys-4naae)
- [Try Model Online](https://universe.roboflow.com/mhseals/buoys-4naae/model/)

---

## Customization & Extending

- You can remove Roboflow-specific code to use your own datasets.
- Modify `train_annotated.py` and related scripts for custom data pipelines.
- Supports YOLOv8 features and configuration options.

---

## References & Links

- [MHSeals/buoy-model GitHub](https://github.com/MHSeals/buoy-model)
- [YOLOv8 Documentation](https://docs.ultralytics.com/)
- [Roboflow Documentation](https://docs.roboflow.com/)

---
