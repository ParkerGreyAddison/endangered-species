#! Note for README:
#
# I didn't include urls from the "cute-animal-photo" search since a large
#  proportion of the results were irrelevant to pictures of animals!


###


# Read urls from files cute-animal*.txt
# urls are separated by a line-break (some of the urls actually have commas!)
#
# Add urls to a set (no duplicates)
#
# Then write to another file, again separated by newline

import argparse
import fnmatch
import os


parser = argparse.ArgumentParser()
parser.add_argument("category", help="Chose a category, 'cute' or 'ugly'", type=str)
args = parser.parse_args()

if args.category not in ["cute", "ugly"]:
    raise Exception("Invalid category, did not find 'cute' or 'ugly'")

urls = set()

path = "./search-urls/"

# Taken more-or-less directly from fnmatch documentation
# Looks at filenames in the given directory
for filename in os.listdir(path):
    # * takes anything
    if fnmatch.fnmatch(filename, f"{args.category}-animal*.txt"):
        with open(path + filename, 'r') as infile:
            to_add_list = [line.rstrip('\n') for line in infile]
            urls = urls.union(set(to_add_list))

# The urls are strings, so we'll have a set of strings.
# Join them with new line \n
to_write = '\n'.join(urls)

with open(f"{args.category}-urls.txt", 'w') as outfile:
    outfile.write(to_write)

# Also, just out of curiosity, print out how many urls were scraped
print(f"Total count: {len(urls)}")
