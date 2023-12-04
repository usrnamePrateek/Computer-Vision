# Image Segmentation Using Custom Seeds

## Overview

Using Watershed algorithm for image segmentation by using user input custom seeds.

## Preview

<img width="802" alt="Screenshot 2023-06-13 at 9 17 30 PM" src="https://github.com/prateek2103/Computer-Vision/assets/30109806/3afbd18e-9db7-4c43-b06a-9b8890d385a8">

## How to

### Start the application

```bash
python main.py --image-path <image_path>
```

- **--image-path** argument can be used to provide a custom image for segmentation
- if **--image-path** is not provided then default image **(data/mountain.jpeg)** is used.

### Put markers

- matplotlib tab10 colormap is used in the application
- use keyboard numbers (1-9) to select a color.
- use left mouse button click to put a marker at a particular location
