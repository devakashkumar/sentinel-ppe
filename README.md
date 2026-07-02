# 🦺 Sentinel PPE AI

> **A real-time AI-powered Personal Protective Equipment (PPE) Detection System** built using **YOLO**, **OpenCV**, and **Python** to improve workplace safety through intelligent computer vision.

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.12+-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge&logo=opencv" alt="OpenCV">
  <img src="https://img.shields.io/badge/YOLO-Ultralytics-red?style=for-the-badge" alt="YOLO">
  <img src="https://img.shields.io/badge/License-MIT-purple?style=for-the-badge" alt="License">
</p>

---

## 📌 Overview

**Sentinel PPE AI** is a modular computer vision application designed to detect whether workers are wearing the required Personal Protective Equipment (PPE) in real time.

The current implementation detects:

- 🪖 Safety Helmets
- 🦺 Reflective Safety Jackets

Unlike a simple object detection demo, this project is being developed as a **production-style AI application** with clean architecture, modular components, and scalability for future industrial deployments.

---

## 🎥 Demo

**Live PPE Detection in Action**

![Sentinel PPE AI Demo](demo/sample_output.gif)

GitHub doesn't autoplay MP4s inside a README, so the GIF above gives a quick glance at detection quality, bounding boxes, and FPS overlay in action.

📹 **Full-length demo video:** [`demo/sample_output.mp4`](demo/sample_output.mp4)

> **Note:** To regenerate the GIF from the source video, run:
> ```bash
> ffmpeg -i demo/sample_output.mp4 -vf "fps=10,scale=640:-1" -t 8 demo/sample_output.gif
> ```

---

## ✨ Features

- ✅ Custom-trained YOLO PPE Detection Model
- ✅ Real-time Helmet Detection
- ✅ Real-time Reflective Jacket Detection
- ✅ Confidence Score Visualization
- ✅ Modern Detection Overlay
- ✅ Stylish Corner Bounding Boxes
- ✅ Live FPS Counter
- ✅ Video File Processing
- ✅ Automatic Output Video Export
- ✅ Modular Project Architecture
- ✅ Easy to Extend and Maintain

---

## 🏗️ Project Architecture

```text
Video
   │
   ▼
Camera Module
   │
   ▼
YOLO Detector
   │
   ▼
Detection Renderer
   │
   ▼
FPS Overlay
   │
   ▼
Display Window
   │
   ▼
Saved Output Video
```

---

## 📁 Project Structure

```text
sentinel-ppe
│
├── dataset/
│
├── demo/
│   ├── sample_output.mp4
│   └── sample_output.gif
│
├── model/
│   └── ppe.pt
│
├── outputs/
│
├── screenshots/
│
├── src/
│   ├── camera/
│   ├── config/
│   ├── detection/
│   ├── utils/
│   └── pipeline.py
│
├── tests/
│
├── videos/
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 🧠 Model Performance

The project uses a custom-trained **Ultralytics YOLO** object detection model.

### Detected Classes

- Safety Helmet
- Reflective Jacket

### Validation Metrics

| Metric    |     Score |
| --------- | --------: |
| Precision | **90.9%** |
| Recall    | **87.6%** |
| mAP@50    | **94.3%** |
| mAP@50-95 | **71.2%** |

---

## 🛠️ Tech Stack

- Python
- OpenCV
- Ultralytics YOLO
- NumPy

---

## ⚙️ Installation

**1. Clone the repository**

```bash
git clone https://github.com/devakashkumar/sentinel-ppe.git
cd sentinel-ppe
```

**2. Create a virtual environment**

```bash
python -m venv venv
```

**3. Activate the environment**

Linux / macOS:
```bash
source venv/bin/activate
```

Windows:
```bash
venv\Scripts\activate
```

**4. Install dependencies**

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

```bash
python main.py
```

The application will:

- Load the trained PPE model
- Process the selected input video
- Detect helmets and reflective jackets
- Display detections in real time
- Render confidence scores
- Show FPS
- Automatically save the processed output video

---

## 🎬 Using Another Video

Open:

```text
src/config/settings.py
```

Change:

```python
VIDEO_NAME = "sample.mp4"
```

to:

```python
VIDEO_NAME = "sample2.mp4"
```

Then run again:

```bash
python main.py
```

---

## 💾 Output

Processed videos are automatically saved inside `outputs/`.

```text
outputs/
├── sample_output.mp4
├── sample2_output.mp4
└── sample3_output.mp4
```

---

## 🚀 Roadmap

### Current

- ✅ Custom YOLO PPE Model
- ✅ Video Processing Pipeline
- ✅ Real-time Detection
- ✅ Modern Detection UI
- ✅ Automatic Video Export

### Upcoming

- 🔄 Worker Tracking
- 🔄 Unique Worker IDs
- 🔄 PPE Compliance Engine
- 🔄 Violation Detection
- 🔄 Screenshot Capture
- 🔄 SQLite Database
- 🔄 Analytics Dashboard
- 🔄 Incident Reports
- 🔄 Webcam Support
- 🔄 Multi-Camera Monitoring

---

## 📸 Screenshots

Add screenshots inside the `screenshots/` directory.

```text
screenshots/
├── detection_1.png
├── detection_2.png
├── detection_3.png
└── dashboard.png
```

---

## 🤝 Contributing

Contributions, feature suggestions, and improvements are always welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

**Akash Kumar**

Passionate about building real-world AI applications, computer vision systems, and scalable software projects.

If you found this project helpful, consider giving it a ⭐ on GitHub.
