import base64

import requests


def get_base_64(file: str) -> str:
    if "http" in file:
        response = requests.get(file)
        text = response.text.encode("ascii")
        return base64.b64encode(text).decode("utf-8")
    else:
        with open(file, "rb") as file_:
            return base64.b64encode(file_.read()).decode("utf-8")
