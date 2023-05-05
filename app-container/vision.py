import io
import os

# from google.cloud import vision_v1 as vision
from google.cloud import vision

import numpy as np
import cv2
import re

######################################
# Hello Car
######################################

# # Instantiate a client
# client = vision.ImageAnnotatorClient()

# # Get filename
# filename = os.path.abspath('resources/car.jpg')

# # Load image to memory
# with io.open(filename, 'rb') as img:
#     content = img.read()

# # Google vision

# # This line of code creates an instance of the google.cloud.vision_v1.types.Image class
# # which represents an image that can be processed by the Google Cloud Vision API.
# # The content parameter is used to provide the image data (binary content) as a bytes-like object
# # This vision.Image object is then used as input for the Vision API to perform various tasks such as object localization, label detection, etc.

# image = vision.Image(content=content)  # pylint: disable=E1101


# response = client.label_detection(image=image)
# labels = response.label_annotations

# print('Labels: ')
# for label in labels:
#     print(label.description)

######################################
# Functions
######################################


def detect_cars_and_license_plates(image_path, VERBOSE=False):
    # Instantiate a client
    vision_client = vision.ImageAnnotatorClient()

    # Load image to memory
    with io.open(image_path, "rb") as img:
        content = img.read()

    # Create an image object
    image = vision.Image(content=content)

    # Perform label detection to detect cars
    response = vision_client.label_detection(image=image)
    labels = response.label_annotations

    car_colors_license_plates = []

    # Check if any cars are detected
    if any(label.description.lower() == "car" for label in labels):
        # Perform object detection to get bounding boxes
        response = vision_client.object_localization(image=image)
        objects = response.localized_object_annotations

        # Filter objects for cars
        cars = [obj for obj in objects if obj.name.lower() == "car"]

        if VERBOSE:
            print(f"Number of cars found: {len(cars)}")

        # For each detected car
        for car in cars:
            # Crop the car image based on the bounding box
            bbox = car.bounding_poly.normalized_vertices

            # Implement the crop_image function based on your preferred image library (e.g., PIL, OpenCV)
            cropped_car_image = crop_image(content, bbox)

            # Perform image properties detection for color
            image_properties_response = vision_client.image_properties(
                image=vision.Image(content=cropped_car_image)
            )
            dominant_colors = (
                image_properties_response.image_properties_annotation.dominant_colors.colors
            )
            predominant_color = dominant_colors[0]

            # Perform text detection for license plates
            text_response = vision_client.text_detection(
                image=vision.Image(content=cropped_car_image)
            )
            texts = text_response.text_annotations

            if VERBOSE:
                print(f"Number of texts found: {len(texts)}")
                # print all texts found
                for text in texts:
                    print(text.description)

            license_plate_pattern = r"([S|E|F|G|B|X][A-Z]\d{1,4}[A-Z]{0,3})"
            license_plate = ""

            for text in texts:
                match = re.search(license_plate_pattern, text.description)
                if match:
                    license_plate = match.group()
                    break

            car_colors_license_plates.append((predominant_color, license_plate))

    return car_colors_license_plates


def crop_image(image_content, bounding_box):
    # Load image content into a NumPy array
    img = np.asarray(bytearray(image_content), dtype="uint8")
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)

    # Convert the normalized vertices to absolute coordinates
    height, width, _ = img.shape
    left = int(bounding_box[0].x * width)
    top = int(bounding_box[0].y * height)
    right = int(bounding_box[2].x * width)
    bottom = int(bounding_box[2].y * height)

    # Crop the image using the bounding box coordinates
    cropped_img = img[top:bottom, left:right]

    # Convert the cropped image back to bytes
    img_byte_arr = cv2.imencode(".jpg", cropped_img)[1]
    img_byte_arr = img_byte_arr.tobytes()

    display_image_opencv(img_byte_arr)

    return img_byte_arr


def display_image_opencv(image_bytes):
    img = np.asarray(bytearray(image_bytes), dtype="uint8")
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)
    cv2.imshow("Cropped Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


######################################
# Debug
######################################
imagepath = os.path.abspath("resources/car.jpg")
results = detect_cars_and_license_plates(image_path=imagepath, VERBOSE=True)
print(results)

# cropped_image_bytes = crop_image(image_content, bounding_box)
# display_image_opencv(cropped_image_bytes)
