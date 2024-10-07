This project is about the development of smoke detection algorithms in case of forest fires.
Our main problem statement is applying classification and object detection to identify smoke / fire through images
I am using Mask RCNN model for object detection in this case.

Step 1: Data gathering and collection:
https://sintecsys-omdena.s3.amazonaws.com/images3.zip
Dataset has almost 16.5K images (~8k masked and ~8k original images). 

Step 2: Exploration of data:
Masked images have been already created. The model needs to be trained on existing masked images and start predicting.
Size of images is: 1920 X 1080
 
Step 3: Applying Image recognition and Object detection models.

Iteration 1:  Simple image recognition model and tried to train with simple CNN model

Iteration 2: Alexnet model for classification

Iteration 3: Mask RCNN model

Step 4: Demonstration of Mask RCNN model

a. Overview of Mask RCNN:
![alt text](https://i.ibb.co/YNr6ybj/Screen-Shot-2020-05-05-at-12-41-48-AM.png)

b. Training and Validation Loss:
![alt text](https://i.ibb.co/SBqsddh/Screen-Shot-2020-05-05-at-12-42-14-AM.png)

c. Precision and Recall numbers:
![alt text](https://i.ibb.co/ts34QXm/Screen-Shot-2020-05-05-at-12-42-29-AM.png)
