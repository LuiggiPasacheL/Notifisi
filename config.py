
import json
import sys
import os
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M")

config = {}

try:
    with open("config.json", "r") as f:
        config = json.load(f)
except:
    config = {
        "page": {
            "domain": "https://sistemas.unmsm.edu.pe",
            "path": "/site/index.php"
        },
        "file": "news_data.pkl",
        "time": current_time
    }

    json_config = json.dumps(config)

    with open("config.json", "w") as f:
        f.write(json_config)

try:
    base_path = sys._MEIPASS
except Exception:
    base_path = os.path.abspath(".")
domain = config['page']['domain']
path = config['page']['path']
file = config['file']
time = config['time']
image_path = os.path.join(base_path, 'assets', 'logo.png')
