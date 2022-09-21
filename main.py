import numpy as np
from PIL import Image
import sys

# Open image with pillow
image = Image.open(sys.argv[1])

# Transform image into an array
data = np.asarray(image)
dictChar = {0: " ", 1: "^", 2: "/", 3: "#", 4: "||"}

# Splitting each line
for row in data:
    line = ""
    for c in row:
        # Fit character into our dictChar
        line += dictChar[(sum(c))//200]

    # Output printing
    print(line)

