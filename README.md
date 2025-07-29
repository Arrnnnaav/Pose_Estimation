# 🕺 Pose Estimation using OpenPose (OpenCV + Python)

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-DNN-green.svg)](https://opencv.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

This project demonstrates **human pose estimation** using a **pre-trained OpenPose model** with **OpenCV's DNN module** in Python. It detects body keypoints and draws a skeleton on a single image.

---

> 👤 Detects and connects 15 body parts: head, limbs, and torso using pre-defined keypoint pairs.

---

## 🚀 Features

- Load and run **OpenPose (Caffe)** model using OpenCV
- Detect 15 human body keypoints
- Draw circles and labels for each detected joint
- Connect the keypoints to form a pose **skeleton**
- Supports static image input

---

## 🛠️ How It Works

1. Load `.prototxt` and `.caffemodel` files using `cv2.dnn.readNetFromCaffe`
2. Preprocess image into a blob and forward it through the network
3. Extract body keypoints from the output heatmaps
4. Draw the keypoints and connect them using OpenPose pair rules

---

## Keypoints & Skeleton Definition
0: Head
1: Neck
2: Right Shoulder
3: Right Elbow
4: Right Wrist
5: Left Shoulder
6: Left Elbow
7: Left Wrist
8: Right Hip
9: Right Knee
10: Right Ankle
11: Left Hip
12: Left Knee
13: Left Ankle
14: Chest

