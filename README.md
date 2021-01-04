# PERSON BLURRING IN 360-DEGREE IMAGES

This repository contains the code for training and testing on people in 360-degree images.

# Steps For Installation:

git clone https://github.com/Sagarl17/person-blurring.git <br />
cd person-blurring<br />
pip install -r requirements-cpu.txt (If GPU is not available)<br />
               or<br />
pip install -r requirements-gpu.txt (If GPU is available)<br />

# Train for a New model:
Please download the data from the following link and follow the instructions in person.py<br />
[train data](https://drive.google.com/open?id=1zvh5zcxxNSQmpS071rJUZMbPhNkkv1x1)<br />

During the training process, models will get generated in the logs folder. <br />

# Test for New Dataset:

Please download the model from the following link and place it in models folder and run test.py after placing the relevant images in val folder.<br />
[model](https://drive.google.com/file/d/1VCqyZQUJqg3T6djJdLnuVkRPcV4ZJKzY/view?usp=sharing)<br />
Sample images are provided in the following link.Place the images in val folder:<br />
[test data](https://drive.google.com/file/d/18GuPOpH1hRAP63_nct5YgQfCvNABXGPc/view?usp=sharing)<br />
Once the testing is finished,the results will be visible in results-val folder<br />


