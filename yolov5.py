import os
import subprocess

def train_yolov5_model():
    weights = "yolov5n.pt"
    data_yaml = "v5data.yaml" #   Path to data.yaml
    epochs = 30 # Number of epochs
    batch_size = 8 # Batch size
    img_size = 640 # Image size (as of the dataset)
    device = "0" # Use the GPU, change it to 'cpu' for CPU

    # Train the model
    train_command = [
        "python", "yolov5\\train.py", # Path to train.py file in the yolov5 folder in the project directory
        "--img", str(img_size),
        "--batch", str(batch_size),
        "--epochs", str(epochs),
        "--data", data_yaml,
        "--weights", weights,
        "--device", device
    ]
    subprocess.run(train_command, check=True)

    # Evaluate the model
    eval_command = [
        "python", "yolov5\\val.py",
        "--data", data_yaml,
        "--weights", "yolov5\\runs\\train\\exp2\\weights\\best.pt" # Path to best.pt file in the yolov5 folder directories in the project directory
    ]
    subprocess.run(eval_command, check=True)

    # Export the model
    export_command = [
        "python", "export.py",
        "--weights", "yolov5\\runs/train/exp/weights/best.pt", # Path to best.pt file in the yolov5 folder directories in the project directory
        "--img", str(img_size),
        "--device", device,
        "--include", "onnx"
    ]
    subprocess.run(export_command, check=True)

if __name__ == '__main__':
    train_yolov5_model()
