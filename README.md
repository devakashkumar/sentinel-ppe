# 🦺 Sentinel PPE AI

> Real-time Personal Protective Equipment (PPE) Detection System for Industrial Safety using Computer Vision.

![Python](https://img.shields.io/badge/Python-3.12+-blue?style=for-the-badge&logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge&logo=opencv)
![YOLO](https://img.shields.io/badge/YOLO-Ultralytics-red?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)

---

# 📌 Overview

**Sentinel PPE AI** is an AI-powered industrial safety monitoring system that detects whether workers are wearing the required Personal Protective Equipment (PPE) in real time.

The current version focuses on:

- 🦺 Safety Helmet Detection
- 🦺 Reflective Jacket Detection
- 🎥 Real-time Video Processing
- 📦 Custom YOLO Model
- 🎨 Modern Detection Overlay
- 🎞️ Automatic Output Video Generation

This project is being built as a production-style software system rather than a simple machine learning demo.

---

# ✨ Features

- ✅ Custom-trained YOLO model
- ✅ Helmet detection
- ✅ Reflective jacket detection
- ✅ Confidence score display
- ✅ Stylish corner bounding boxes
- ✅ Modern UI overlays
- ✅ FPS Counter
- ✅ Video playback
- ✅ Automatic processed video saving
- ✅ Modular architecture
- ✅ Easy to extend

---

# 🖼️ Demo

## Input

```
videos/sample.mp4
```

↓

## Processing

```
YOLO Detection
↓

Helmet Detection
↓

Reflective Jacket Detection
↓

Bounding Box Rendering
↓

FPS Counter
```

↓

## Output

```
outputs/sample_output.mp4
```

---

# 📁 Project Structure

```
Sentinel-PPE-AI
│
├── dataset/
│   ├── train/
│   ├── valid/
│   ├── test/
│   └── data.yaml
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
│   ├── detection/
│   ├── config/
│   ├── utils/
│   └── pipeline.py
│
├── tests/
│
├── videos/
│   ├── sample.mp4
│   └── sample2.mp4
│
├── main.py
├── README.md
└── requirements.txt
```

---

# 🧠 Model

The project uses a custom-trained **Ultralytics YOLO** object detection model.

Detected classes:

- Safety Helmet
- Reflective Jacket

Current validation performance:

| Metric | Score |
|---------|--------|
| Precision | 90.9% |
| Recall | 87.6% |
| mAP@50 | 94.3% |
| mAP@50-95 | 71.2% |

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/sentinel-ppe-ai.git
```

Enter the project

```bash
cd sentinel-ppe-ai
```

Create virtual environment

```bash
python -m venv venv
```

Activate

### Linux / macOS

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running

Simply execute

```bash
python main.py
```

The application will:

- Load the trained model
- Open the selected sample video
- Detect PPE in every frame
- Display the processed video
- Save the processed output automatically

---

# 📹 Selecting Another Video

Open

```
src/config/settings.py
```

Change

```python
VIDEO_NAME = "sample.mp4"
```

to

```python
VIDEO_NAME = "sample2.mp4"
```

Run again

```bash
python main.py
```

---

# 💾 Output

Processed videos are automatically saved inside

```
outputs/
```

Example

```
outputs/
├── sample_output.mp4
└── sample2_output.mp4
```

---

# 🛠️ Tech Stack

- Python
- OpenCV
- Ultralytics YOLO
- NumPy

---

# 🚀 Roadmap

### ✅ Current

- Custom YOLO Model
- PPE Detection
- Video Processing
- Output Video Saving
- Modern Detection Overlay

### 🔄 Next

- Worker Tracking
- Worker IDs
- PPE Compliance Engine
- Missing PPE Alerts
- Violation Screenshots
- SQLite Logging
- Analytics Dashboard
- Report Generation
- Live Webcam Support
- Multi-camera Support

---

# 📸 Screenshots

Add screenshots here after running the project.

```
screenshots/
├── detection_1.png
├── detection_2.png
└── dashboard.png
```

---

# 🤝 Contributing

Contributions, ideas, and improvements are welcome.

Feel free to fork the repository and submit a pull request.

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Sky**

Building practical AI systems with a focus on real-world computer vision applications.

If you found this project useful, consider giving it a ⭐ on GitHub!