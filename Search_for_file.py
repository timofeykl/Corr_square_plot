import os
import glob

import os
from datetime import datetime

rootdir = '
#c> - smth
'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if "certain_file" in file.lower():
            print(os.path.join(subdir, file))
            # +))
