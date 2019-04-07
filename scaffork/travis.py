from time import sleep

import requests
from travispy import TravisPy
from travispy.entities import Repo
from travispy.errors import TravisError

from scaffork.data import Config

TRAVIS_URL = "https://api.travis-ci.com"


class Travis:
    travis: TravisPy
    repo: Repo

    def __init__(self, config: Config):
        self.config = config

    def enable_repo(self):

        self.travis = TravisPy.github_auth(self.config.github_token(), uri=TRAVIS_URL)

        try:
            self.__try_enable_repo()
        except TravisError:
            print("Travis could not find the repository. Let's wait 10 seconds and try again.")
            sleep(10)
            self.__try_enable_repo()

    def __try_enable_repo(self):
        self.repo = self.travis.repo(f"{self.config.github_owner()}/{self.config.github_repo()}")
        self.repo.enable()

    def set_envs(self, name: str, value: str, public: bool = False):

        token = self.travis._session.headers["Authorization"]
        headers = {"Authorization": token, "Accept": "application/vnd.travis-ci.2+json"}
        data = {"env_var": {"name": name, "value": value, "public": public}}
        url = f"{TRAVIS_URL}/settings/env_vars?repository_id={self.repo.id}"

        response = requests.post(url, json=data, headers=headers)

        if response.status_code != 200:
            print("Travis could not find the repository. Let's wait 10 seconds and try again.")
            sleep(10)
            response = requests.post(url, json=data, headers=headers)
            if response.status_code != 200:
                raise Exception(f"Error on set_env: {response.text} and ")
