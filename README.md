# Comparison of YOLOv5 and YOLOv8 on Corrosion Detection

## Overview

This project focuses on training and comparing the YOLOv5 and YOLOv8 object detection models for detecting corrosion in various materials. The aim is to determine which model performs better in terms of accuracy, speed, and robustness when identifying corrosion in images.

## Dataset
The dataset consists of 4942 corrosion images. The split is as following:
- Training images : 4325
- Validation images : 412
- Testing images : 205

The corrosion dataset was downloaded for YOLOv5 and YOLOv8 formats. The link for the dataset is provided below:
- [https://universe.roboflow.com/cawilai-interns-july-2023/corrosion-instance-segmentation-sfcpc/dataset/16]

## Resources

Microsoft Visual Studio 2022 was used.
NVIDIA GeForce GTX 1050 was used.
The model YOLOv5n and YOLOv8n were used.
The model was trained on 30 epochs.

## Prerequisites

Execute the commands given below in Developer Powershell / Console.

For YOLOv5, clone the YOLOv5 repository by Ultralytics:

```bash
git clone https://github.com/ultralytics/yolov5.git
cd yolov5
pip install -r requirements.txt
```

For YOLOv8, open the Developer Powershell / Console and install the required libraries. The commands are given below:

```bash
pip install ultralytics
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
pip install numpy opencv-python
pip install pyyaml
pip install onnx
```

## Training

You may refer to main.py file in this repository.

## Results

The performance of the models I trained is given below:

- Results of YOLOv5:

<h3>YOLOv5</h3>
<table>
  <tr>
    <th rowspan="2">Model</th>
    <th colspan="3">Precision</th>
    <th colspan="3">Recall</th>
    <th colspan="3">mAP@50</th>
    <th colspan="3">mAP@50-95</th>
    <th rowspan="2">Training time (hours)</th>
  </tr>
  <tr>
    <th>Train.</th>
    <th>Val.</th>
    <th>Test.</th>
    <th>Train.</th>
    <th>Val.</th>
    <th>Test.</th>
    <th>Train.</th>
    <th>Val.</th>
    <th>Test.</th>
    <th>Train.</th>
    <th>Val.</th>
    <th>Test.</th>
  </tr>
  <tr>
    <td>YOLOv5n</td>
    <td>0.642</td>
    <td>0.612</td>
    <td>0.567</td>
    <td>0.474</td>
    <td>0.427</td>
    <td>0.400</td>
    <td>0.511</td>
    <td>0.457</td>
    <td>0.406</td>
    <td>0.249</td>
    <td>0.239</td>
    <td>0.197</td>
    <td>2.833</td>
  </tr>
</table>

- Results of YOLOv8:

<h3>YOLOv8</h3>
<table>
  <tr>
    <th rowspan="2">Model</th>
    <th colspan="3">Precision</th>
    <th colspan="3">Recall</th>
    <th colspan="3">mAP@50</th>
    <th colspan="3">mAP@50-95</th>
    <th rowspan="2">Training time (hours)</th>
  </tr>
  <tr>
    <th>Train.</th>
    <th>Val.</th>
    <th>Test.</th>
    <th>Train.</th>
    <th>Val.</th>
    <th>Test.</th>
    <th>Train.</th>
    <th>Val.</th>
    <th>Test.</th>
    <th>Train.</th>
    <th>Val.</th>
    <th>Test.</th>
  </tr>
  <tr>
    <td>YOLOv8n</td>
    <td>0.602</td>
    <td>0.603</td>
    <td>0.537</td>
    <td>0.426</td>
    <td>0.407</td>
    <td>0.353</td>
    <td>0.462</td>
    <td>0.443</td>
    <td>0.365</td>
    <td>0.269</td>
    <td>0.266</td>
    <td>0.203</td>
    <td>3.137</td>
  </tr>
</table>

## Acknowledgments

- [YOLOv5 Repository](https://github.com/ultralytics/yolov5)
- [YOLOv8 Repository](https://github.com/ultralytics/ultralytics)
- Dataset sources and contributors
- [Dataset Owner : CawilAI Interns July 2023](https://universe.roboflow.com/cawilai-interns-july-2023)
- [Dataset](https://universe.roboflow.com/cawilai-interns-july-2023/corrosion-instance-segmentation-sfcpc/dataset/16)

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For questions or feedback, feel free to contact:

- **Name**: Muhammad Ahmad Abbas
- **Email**: ahmad.abbas.2329@gmail.com
