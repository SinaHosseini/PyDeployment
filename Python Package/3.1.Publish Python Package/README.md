# Fantasy Face

Add an animal mask to the face using OpenCV and Python.

## Description

`Fantasy Face` is a Python package that allows you to overlay an animal mask onto a face in an image. It uses OpenCV for image processing.

## Installation

To install the package, you can use the following command:

```sh
pip install git+https://github.com/SinaHosseini/amoo_sina_lion.git
```

## Usage

Here's an example of how to use the package:
``` python
import fantasy_face
import cv2

# Define the paths to the images
image_path = "path/to/your/image.jpg"
cow_path = "input/cow.jpg"

# Read the images
my_image = cv2.imread(image_path)
image_cow = cv2.imread(cow_path)

# Resize images if needed
my_image = cv2.resize(my_image, [640, 640])
image_cow = cv2.resize(image_cow, [640, 640])

# Apply the mask
image_cow_ghost, image_cow_transparent = fantasy_face.transparent_sticker(image_cow)
convert_image = my_image * image_cow_ghost + image_cow_transparent

# Save the result
cv2.imwrite("output/animal_face.jpg", convert_image)
```

You can also run the script directly from the command line:
```bash
python fantasy_face.py --image_path path/to/your/image.jpg
```
## Requirements
Python 3.6+<br>
OpenCV<br>
NumPy
## Author
Sina Hosseini

Email: sshosseinivaez@gmail.com
## License
This project is licensed under the MIT License - see the LICENSE file for details.