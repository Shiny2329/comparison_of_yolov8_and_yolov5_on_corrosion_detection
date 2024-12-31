from ultralytics import YOLO

def train_yolo_model():
    model = YOLO('yolov8n.pt') # Select the model, for this case it is 'n' (nano)

    # Train the model
    model.train(
        data='v8data.yaml', # Path to data.yaml file
        epochs=30, # Number of epochs
        batch=8, # Batch size
        imgsz=640, # Image size (as in the dataset)
        device=0 # Use the GPU, change it to 'cpu' for CPU
    )

    metrics = model.val()

    # Print the evaluation metrics
    print("Evaluation Metrics:", metrics)

    # Exports for implementation
    model.export(format='onnx')

if __name__ == '__main__':
    train_yolo_model()
