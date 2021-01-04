# PERSON BLURRING IN 360-DEGREE IMAGES

This repository contains the code for training and testing on people in 360-degree images.

# Steps For Installation:

```bash
git clone https://github.com/Sagarl17/person-blurring.git
cd person-blurring
pip install -r requirements-cpu.txt (If GPU is not available)
               or
pip install -r requirements-gpu.txt (If GPU is available)
```

# Train for a New model:
```bash
Please download the data from the following link and follow the instructions in person.py
https://drive.google.com/open?id=1zvh5zcxxNSQmpS071rJUZMbPhNkkv1x1

During the training process, models will get generated in the logs folder. 
```

# Test for New Dataset:

Please download the model from the following link and place it in models folder and run test.py after placing the relevant images in val folder.
[model](https://drive.google.com/file/d/1VCqyZQUJqg3T6djJdLnuVkRPcV4ZJKzY/view?usp=sharing)
Sample images are provided in the following link.Place the images in val folder:
[test data](https://drive.google.com/file/d/18GuPOpH1hRAP63_nct5YgQfCvNABXGPc/view?usp=sharing)
Once the testing is finished,the results will be visible in results-val folder


