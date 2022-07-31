import os, platform

os.system('git pull')

 

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    from MR_HAMII import hk

    hk()

elif bit == '32bit':

    from EXTRACT import hk

    hk()
