import base64

from data import Data


def get_base_64(data: Data) -> str:
    if data.base_64_is_url():
        return ""
    else:
        with open(data.base_64_file(), "rb") as json_file:
            return base64.b64encode(json_file.read()).decode("utf-8")
