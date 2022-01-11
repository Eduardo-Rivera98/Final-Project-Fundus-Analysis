# Final-Project-Fundus-Analysis

![alt text](https://gme.medicine.uiowa.edu/eye/sites/medicine.uiowa.edu.eye/files/wysiwyg_uploads/Fundus_Fig1_Normal-Retina.jpg "Eye Fundus")

Eye fundus images are those obtained by reflecting light into the inside of the eye. This way you obtain a visual two dimensional representation of the retinal tissue. The interest of the eye fundus images lies in the fact that they show a part of the body that provides a lot of information, where the nervous system (via the optic nerve), the vascular system(via the capillaries feeding the nerve), and the eye meet. It is where the visual stimulus is formed, and it is a fantastic gateway into our organism and health conition. In this project I will develop models for the detection of:
* Age-related macualar degeneration
* Diabetic retinopathy
* Hypertension
* Cataracts
* Myopia
* Glaucoma

As well as an extra I attempted to do a model to predict the age of the patient through the eye fundus image



## Objective of the project

The objective of the project is to develop several deep learning models using Convolutional Neural Netwroks. The idea is to build an interface where the user provides an eye fundus image, and recieves a diagnosis for the different diseases that I have trained my models to detect. The biggest challenges will be to develop the models using Convolutional Neural Networks, to obtain the maximum precision with a realitively small sample of images to train, and to avoid overfitting.

## Methodolgy

### First step: Dealing with the Data
I found a dataset in Kaggle with 6000 Eye fundus images from 3000 patients (left and right eye), and their diagnosis. The first problem that I encountered was the lack of clarity in the dataset that established the diagnositcs of the images, as certain indicators showed the presence of a disease, whilst others for the same image said the opposite, so I had to be very careful when classifying the images. Another problem was the data distribution, as for certain diseases like cataracts I only had 300 images, whilst for diabetic retinopathy I had 2000. For this problem th solution that I found was data augmentation as I will explain later

### Second step: Developing the models
At first I wanted to develop a single model that would classify all of the diseases, but due to the distribution of the data, the complexity of such a model and the lack of processing capacity of my computer, I decided to do six different models for the classification of the diseases. For the different models I used different techniques and technolgies. For some I used VGG-16 which is a Convolutional Neural Network architecture, for others I didn't, it depended what worked best and gave me better precision results. I built all my deep learning models using Tensorflow's Keras. Here I faced mainly three difficulties; the first one was the lack of processing power of the CPU and Jupyter Notebook. I tackled this issue by moving my work to Google Colaboratory and by running my models through the GPU. The second problem I had to face was the uneven distribution of the diseases. For this I used a technique called Data Augmentation, where I randomly (within a certain established parameters) made modifications to a number of selected images with the objective of increasing the number of images in a certain classification. Finally my last challenge was to reduce overfitting, which was very common in my models due to the reduced number of images. To approach this problem I researched for effective techniques to reduce overfitting in Convolutional Neural Networks, and I decided to implement 'Dropout' which is a method from Keras that allows you to randmoly hide a certain amount of information to the deep learning model whilst traing, avoiding like that that the model memorizes the data.