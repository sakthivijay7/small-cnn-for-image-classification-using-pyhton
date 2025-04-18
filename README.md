# small-cnn-for-image-classification-using-pyhton
create small convolution neural network for image classification 
Intro:
Small image dataset it contains trainning had each class 40images and testing had each class 10 images.
ALL images_size (224,224) and format .jpg it structured dataset.
overview:
This project an image classification model using Tensorflow,keras.
It predict whether input of image to be Ironman or ultron ,no pretrained model used

Tools:
Tensorflow,keras
CNN architecture,
Numpy,
Jupyternotebook,
Data augmentation

Model summary:
cnn:Convolution layers,Maxpooling,flatten,dense layer
optimizer:adam (Adaptive moment estimation)
loss:binary_crossentropy
Train and Validation accuracy:
![Capture1](https://github.com/user-attachments/assets/c0fd6e15-9723-4c18-9a2c-22c1a250d989)


Model training accuracy: 0.8 to 0.9 (epoch 6-9)learn good,validation accuracy: reached 1.0 by after epoch 5.
Model save in h5(Hierarchical dataformat5)
Model prediction:

Streamlit small UI for prediction;
![Capture](https://github.com/user-attachments/assets/c1c7bd24-031b-4212-a19a-2c293a5c3179)





