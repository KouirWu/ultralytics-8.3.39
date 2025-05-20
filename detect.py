from ultralytics import YOLO

# 加载模型
model = YOLO("yolo11n.pt")

results = model("D:/yolo/ultralytics-8.3.39/ultralytics-8.3.39/ultralytics/assets/")