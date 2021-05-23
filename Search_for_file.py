import os
import glob

import os
from datetime import datetime

rootdir = 'I:\\0RU_RCI\\RCI_FIN\\subsidy\\bank_subs\\2020'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if "nissan" in file.lower():
            print(os.path.join(subdir, file))
            # +))
