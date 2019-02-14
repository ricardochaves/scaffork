# https://docs.travis-ci.com/api/#settings-environment-variables

# If you are working with Python you can use TravisPy to achieve this.

from time import sleep

import requests
from travispy import TravisPy
from travispy.entities import Repo
from travispy.errors import TravisError

from data import Data


class Travis:
    data: Data
    travis: TravisPy
    repo: Repo

    def __init__(self, data: Data):
        self.data = data

    def __get_url(self):
        return (
            "https://api.travis-ci.com"
            if self.data.id_private_repo()
            else "https://api.travis-ci.org"
        )

    def enable_repo(self):

        self.travis = TravisPy.github_auth(self.data.git_hub_token(), uri=self.__get_url())

        try:
            self.__try_enable_repo()
        except TravisError:
            print("Travis could not find the repository. Let's wait 10 seconds and try again.")
            sleep(10)
            self.__try_enable_repo()

    def __try_enable_repo(self):
        self.repo = self.travis.repo(f"{self.data.repo_ower()}/{self.data.repo_name()}")
        self.repo.enable()

    def set_envs(self, name: str, value: str, public: bool):

        token = self.travis._session.headers["Authorization"]

        headers = {"Authorization": token, "Accept": "application/vnd.travis-ci.2+json"}

        data = {"env_var": {"name": name, "value": value, "public": public}}

        url = f"{self.__get_url()}/settings/env_vars?repository_id={self.repo.id}"
        response = requests.post(url, json=data, headers=headers)

        if response.status_code != 200:
            print("Travis could not find the repository. Let's wait 10 seconds and try again.")
            sleep(10)
            response = requests.post(url, json=data, headers=headers)
            if response.status_code != 200:
                raise Exception(f"Erro on set_env: {response.text} and ")

    def get_badge_value(self):
        return (
            ""
            if self.data.id_private_repo()
            else f"[![Build Status](https:\/\/travis-ci.org\/{self.data.repo_ower()}\/{self.data.repo_name()}.svg?branch=master)](https:\/\/travis-ci.org\/{self.data.repo_ower()}\/{self.data.repo_name()}) "
        )
