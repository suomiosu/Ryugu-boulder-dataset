import os
import json
import random
import cv2
import numpy as np

image_dir = "path/to/image/dir"
json_path = "path/to/annotation.json"
output_dir = "path/to/dstdir"

with open(json_path, mode="rt", encoding="utf-8") as f:
	data = json.load(f)

ann = data["annotations"]

for d in random.sample(data["images"], 3):
    file_name = os.path.join(image_dir, d["file_name"])
    img = cv2.imread(file_name)
    img_id = d["id"]
    output = os.path.join(output_dir, d["file_name"])
    
    for i in range(len(ann)):
        if ann[i]["image_id"] == img_id:
            points = np.array(ann[i]["segmentation"][0])
            num_row = int(points.size/2)
            points = np.reshape(points, [num_row, 2])
            color = np.random.choice(range(256), size=3)
            cv2.fillConvexPoly(img, points, color.tolist())
    cv2.imwrite(output, img)
