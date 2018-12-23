# For each picture that we have a url for, download it

import argparse
import urllib.request


parser = argparse.ArgumentParser()
parser.add_argument("category", help="Chose a category, 'cute' or 'ugly'", type=str)
args = parser.parse_args()

if args.category not in ["cute", "ugly"]:
    raise Exception("Invalid category, did not find 'cute' or 'ugly'")

path = f"./{args.category}-images/"

urls = []

with open(f"{args.category}-urls.txt", 'r') as infile:
    urls = [line.rstrip('\n') for line in infile]

# Download the image from the url
for i, url in enumerate(urls):
    urllib.request.urlretrieve(url, path + f"{i:04d}.jpg")
