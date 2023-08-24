import json
import os
from PIL import Image

# Define your YOLOv5 annotation directory and output JSON file path
yolov5_anno_dir1 = '/home/ragini/final_data/valid/labels'
yolov5_anno_dir2 = '/home/ragini/final_data/valid/images'

output_json_path = '/home/ragini/valid_output.json'

# Define your classes
classes = ['0', '1']

# Define the output dictionary
output_dict = []

# Iterate over the annotation files and create the output dictionary
for filename in os.listdir(yolov5_anno_dir1):
    if filename.endswith('.txt'):
        image_id = os.path.splitext(filename)[0]
        image_path = os.path.join(yolov5_anno_dir2, f"{image_id}.jpg")
        image = Image.open(image_path)
        width, height = image.size
        proposals = []
        with open(os.path.join(yolov5_anno_dir1, filename), 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip().split()
                x, y, w, h = map(float, line[1:])
                x_min = int((x - w/2) * width)
                y_min = int((y - h/2) * height)
                x_max = int((x + w/2) * width)
                y_max = int((y + h/2) * height)
                bbox = [x_min, y_min, x_max, y_max]
                mask = [0] * (width * height)
                for i in range(x_min, x_max):
                    for j in range(y_min, y_max):
                        mask[j * width + i] = 1
                proposal = {
                    'mask': mask,
                    'score': 1.0,
                    'bbox': bbox,
                    'category_id': classes.index(line[0])
                }
                proposals.append(proposal)
        output_dict.append({
            'file_path': image_path,
            'proposals': proposals
        })

# Write the output JSON file
with open(output_json_path, 'w') as f:
    json.dump(output_dict, f)
