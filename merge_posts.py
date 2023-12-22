import glob
import fileinput
import os

blogposts_path = r"~/Code/github/blog/content/posts/*.md"

pat = os.path.expanduser(blogposts_path)

with open('single-file.md', 'w', encoding='utf-8') as fout:  # Specify encoding for output file
    for file_name in sorted(glob.glob(pat)):
        with open(file_name, 'r', encoding='utf-8') as f:  # Specify encoding for input files
            for line in f:
                fout.write(line)
