# Go through all images to make sure they can be read with OpenCV
# If not, delete the image.

import argparse
import os
import cv2


parser = argparse.ArgumentParser()
parser.add_argument("category", help="Chose a category, 'cute' or 'ugly'", type=str)
args = parser.parse_args()

if args.category not in ["cute", "ugly"]:
    raise Exception("Invalid category, did not find 'cute' or 'ugly'")

path = f"./{args.category}-images/"

count_removed = 0

for filename in os.listdir(path):
    try:
        img = cv2.imread(path + filename)

        if img is None:
            raise Exception
    except:
        print(f"Deleting {filename}")
        os.remove(path + filename)
        count_removed += 1

print(f"Total Removed: {count_removed}")
