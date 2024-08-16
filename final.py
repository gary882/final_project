
#!/usr/bin/python3
import os
import jetson_inference
import jetson_utils
import argparse
import requests
import json

# Setting up the argument parser
parser = argparse.ArgumentParser()
parser.add_argument("filename", type=str, help="filename of the image to process")
parser.add_argument("--network", type=str, default="googlenet", help="model to use, can be: googlenet, resnet-18, etc.")
opt = parser.parse_args()

# Load the image
img = jetson_utils.loadImage(opt.filename)

# Load the model
net = jetson_inference.imageNet(model="resnet18.onnx",
                                labels="labels.txt",
                                input_blob="input_0",
                                output_blob="output_0"
                                )

# Classify the image
class_idx, confidence = net.Classify(img)

# Get the class description
class_desc = net.GetClassDesc(class_idx)

# Print the classification result
print("image is recognized as " + str(class_desc) + " (class #" + str(class_idx) + ") with " + str(confidence*100) + "% confidence")

# Send a request to ChatGPT API for health benefits
api_url = "https://api.openai.com/v1/chat/completions"  # This is the endpoint to ChatGPT API
api_key = os.environ["OPENAI_API_KEY"]

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

data = {
    "model": "gpt-3.5-turbo",  # Specify the model
    "messages": [
        {"role": "system", "content": "You are an expert nutritionist."},
        {"role": "user", "content": f"What are the health benefits of {class_desc}?"}
    ]
}

response = requests.post(api_url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    response_data = response.json()
    health_benefits = response_data['choices'][0]['message']['content']
    print(f"Health benefits of {class_desc}: {health_benefits}")
else:
    print(f"Failed to retrieve health benefits. Status code: {response.status_code}, Response: {response.text}")


#python3 final.py Image_1.jpg --network=resnet-18