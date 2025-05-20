# 🚀 YOLO 项目小白指南

---

## 📋 项目简介
这是一个基于 YOLO 的目标检测项目，适合初学者快速上手。本项目使用 Python 实现，依赖 PyTorch 和 OpenCV 等库。

---

## 🖥️ 环境要求
- **Python** 3.8 或更高版本
- **pip**（Python 包管理器）
- **Git**（用于下载项目）

---

## 🛠️ 详细步骤

### 1️⃣ 下载项目
> 打开命令行（Windows 用户按 <kbd>Win + R</kbd>，输入 <kbd>cmd</kbd> 并回车），执行以下命令：

```bash
git clone https://github.com/KouirWu/ultralytics-8.3.39.git
cd ultralytics-8.3.39
```

### 2️⃣ 安装依赖
> 在项目根目录下，执行以下命令安装所需依赖：

```bash
pip install -r requirements.txt
```
> 如果遇到网络问题，可以尝试使用国内镜像：

```bash
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 3️⃣ 运行项目

#### 🎯 目标检测（detect.py）
```bash
python detect.py
```
> 如果遇到错误，请检查：
> - 是否已安装所有依赖
> - 是否在项目根目录下运行命令
> - 是否有 GPU 支持（如果没有，程序会自动使用 CPU）

#### 🏋️‍♂️ 训练模型（train.py）
```bash
python train.py
```
> 注意：训练需要 GPU 支持，且需要准备训练数据。

---

## ❓ 常见问题

| 问题 | 解决方法 |
|------|----------|
| `ModuleNotFoundError: No module named 'torch'` | `pip install torch torchvision torchaudio` |
| `ModuleNotFoundError: No module named 'cv2'` | `pip install opencv-python` |
| `ModuleNotFoundError: No module named 'numpy'` | `pip install numpy` |

---

## 📬 联系方式
如有问题，请提交 Issue 或联系季禾。

---

## 📄 许可证
本项目遵循 MIT 许可证，详情请查看 [LICENSE](LICENSE) 文件。

---
