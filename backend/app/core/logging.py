import logging
import json

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format=json.dumps({
            "level": "%(levelname)s",
            "message": "%(message)s",
            "time": "%(asctime)s"
        })
    )
