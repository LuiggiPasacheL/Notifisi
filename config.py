
import json

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
        "time": "20:00"
    }

    json_config = json.dumps(config)

    with open("config.json", "w") as f:
        f.write(json_config)
