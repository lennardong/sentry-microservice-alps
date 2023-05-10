import os
from vision import detect


def test_detect_cars_and_license_plates_with_cars():
    image_path = os.path.abspath("resources/car.jpg")

    with open(image_path, "rb") as f:
        image_data = f.read()
    results = detect(image_data=image_data, VERBOSE=True)

    # Check if the correct number of cars is detected
    assert len(results) == 1

    # Check if the predominant color and license plate are correctly detected for each car
    car_color, license_plate = results[0]
    assert car_color == (237.0, 240.0, 242.0)
    assert license_plate == "SKL7401L"
