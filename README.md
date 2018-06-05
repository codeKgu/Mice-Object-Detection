# Research-Weizhou-Code
Relevant code to project in mice object detection and realtime processing

1. [Data Annotation](#data-annotation)
2. [DarkNet Configuration](#darknet-configuration)
3. [Training](#training)
4. [Results](#viewing-results)
5. [Changing Source Code](#changing-source-code)
6. [Real Time Detection with Camera](#real-time-detection-with-camera)


## Overview
We will be training images with a [YOLOV2](https://pjreddie.com/darknet/yolo/) implementation called [darknet](https://github.com/AlexeyAB/darknet) for windows.

This supports:
* both OpenCV 2.x.x and OpenCV <= 3.4.0 (3.4.1 and higher isn't supported)
* both cuDNN v5-v7
* CUDA >= 7.5

To create our own traning set we will be using [BBox-Label-Tool](https://github.com/puzzledqs/BBox-Label-Tool)
This requires:
* python 2.7
* python PIL (Pillow)

Training images and video is from Professor Weizhou

## Data Annotation
To annotate we need to:
* place our training images in `python scripts\BBox-Label-Tool\Images\[Numbered Folder ie. 001, 002, etc]`
* open Bbox-Label-Tool by running `main.py` in the BBox-label-Tool directory

Labels will be in `python scripts\BBox-Label-Tool\Labels` with the same numbered directory as the images in .txt files with the resulting format:
```
[category number]
[bounding box left X] [bounding box top Y] [bounding box right X] [bounding box bottom Y]
...
```

Note, the BBox-Label-Tool requires images to be .jpeg files but that can be adjusted by changing the code in main.py

### Convert to YOLOv2 Format

YOLOv2 takes labels of the form 
```
[category number] [object center in X] [object center in Y] [object width in X] [object width in Y]
```
To fix this there is a script in `python scripts\convert_to_yolo.py` which converts to the YOLO format

## Darknet Configuration 
Darknet needs you to tell it what images are going to be the test set and training set. To do this there `process.py` which takes images and plits up into a test and train set written to test.txt and train.txt.

Next Darknet needs specific configuration files.  Three files needs to be created. 
* `obj.data` in `\darknet\build\darknet\x64\data\cfg`which takes the following format
  
  ```
   classes = [num classes]
   train = train.txt (from earlier)
   valid = test.txt (from earlier)
   names = obj.names 
   backup = /backup
   ```
   Note train.txt and test.txt are stored in `\darknet\build\darknet\x64\` and backup is where the backup weights are stored 
* `obj.names` in `\darknet\build\darknet\x64\`should simply be the following where each new category is on a newline
  ```
  mice
  ```
* `obj.cfg` in `\darknet\build\darknet\x64\cfg` which should look similar to the `yolo2.0.cfg` except with the following changes
  * line 2 `batch=32` this is what works best on my Nvidia GTX 1050 GPU without the traning being stopped due to CUDA being out of memory
  * line 3 `subdivisions=8` in which the batch will be divided by to decrease GPU and VRAM requirements. The higher the number the less load on the GPU
  * line 230 `classes=[Num Classes]` the number of classes to classify
  * line 224 `filters = (Classes + 5) *5` the number of filters in the last convolutional layer
  
 ## Training
 To train, run the following command in cmd
 ```
 darknet.exe detector train data/cfg/obj.data cfg/yolo-obj.cfg darknet19_448.conv.23
 ```
 Note, the 
 ![cmd](https://timebutt.github.io/static/content/images/2017/05/screen17.PNG)
 The line 
 `2: 2.950644, 15.939886 avg, 0.001000 rate, 2.813000 seconds, 128 images` 
 shows the training step followed by the error. Previously I had trained for 2.5 hours in which the error was around 0.06.
 Weights are stored in `/backup` at every 100 iterations.
 
 To continue training from the last saved weights file:
 ```
 darknet.exe detector train data/obj.data cfg/yolo-obj.cfg yolo-obj_2000.weights
 ```
 
 ## Viewing Results
 ![result](https://github.com/codeKgu/Research-WeiZhou/blob/master/screen%20captures/test_result.JPG)
 
 We use the .weights file to run our model on new images. 
 To run on a test image:
 ```
 darknet.exe detector test data/obj.data cfg/yolo-obj.cfg backup/yolo-obj_1600.weights [PATH to image]
 ```
 To view on a AVI file:
 ```
 darknet.exe detector demo data/obj.data cfg/yolo-obj.cfg backup/yolo-obj_1600.weights data/weizhe_videos/MouseA06_20140814_14-25-44_Top_J85.avi
```
With my GPU I get around 20-21 frames per second. 

To run and save a AVI file:
```
darknet.exe detector demo data/obj.data obj/yolo-obj.cfg backup/yolo-obj_1600.weights [Path to AVI] -i 0 -out_filename [Result Filename]
```

 ## Changing Source Code
 To use the output of the network for postprocessing and analysis we can print the bounding box locations to stdout and using another 
 python script to process that in any way necessary. 
 To change the source code open darknet.sln in `/darknet/build/darknet/`. `image.c` contains drawing the borders in the `draw_detections_cv` function which is used in `demo.c`. For YOLOv3 this is `draw_detections_cv_v3`. I have changed the source code to add a midpoint of the bounding box as well as get the frame number of the the video file. 
 
 ## 
