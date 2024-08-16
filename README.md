#Classifying fruits and vegtables and returing their health benefits

DESCRIPTION: The project i created trained the resnet-18 network to create a model that can classify different fruits and vegtables. Using the label, my project sends it to chatGPT through an api-key and returns the health benefits of the fruit or vegtable. Although the model was trained for 2 epochs and its accuracy is lacking. With more training time, the model would be very accurate and useful. It can allow people to find health benefits of fruits and vegtables they did not know the name of.

The Algorithm
In the code, my project loads the image provided by the user and loads the model. Then using the model it classifys the image and gives it a label. Then sends a request to ChatGPT API for the health beneifits for the labeled food. Then returns the health benefits to the user.

Running this project
1.First change the directory to the final_project 2. import jetson_inference import jetson_utils import argparse import requests import json 3. run the following code in the terminal python3 final.py Image_1.jpg

video link to my voice over: https://youtu.be/nPqP9uvv7t4
