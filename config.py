
import json
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

domain = config['page']['domain']
path = config['page']['path']
file = config['file']
time = config['time']
