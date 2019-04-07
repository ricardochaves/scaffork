import os
import shutil

import requests
from git import Repo

from scaffork.data import Config


class GitHub:

    config: Config
    repo: Repo

    def __init__(self, config: Config):
        self.config = config

    def create_remote_repo(self):
        headers = {"Authorization": f"token {self.config.github_token()}", "Content-Type": "application/json"}
        data = {
            "name": self.config.github_repo(),
            "description": self.config.github_description(),
            "homepage": self.config.github_home_page(),
            "private": self.config.github_is_private(),
            "has_issues": self.config.github_has_issuer(),
            "has_projects": self.config.github_has_projects(),
            "has_wiki": self.config.github_has_wiki(),
        }

        response = requests.post(self._get_url(), json=data, headers=headers)

        if response.status_code != 201:
            raise Exception(f"Erro on post git: {response.text}")

    def init_and_push(self):
        shutil.rmtree(f"{self.config.project_dir()}/.git")

        self.repo = Repo.init(self.config.project_dir())
        self.repo.create_remote("origin", url=f"git@github.com:{self.config.github_repo_simple_url()}.git")
        self.commit("First commit")

    def commit(self, message: str):
        self.repo.git.add(A=True)
        self.repo.index.commit(message)
        self.repo.git.push("origin", "master")

    def clone(self):

        if os.path.exists(self.config.dict_["project_dir"]):
            raise Exception("Git project_dir already exists, choose another location for the clone")

        self.repo = Repo.clone_from(
            self.config.dict_["project_source"], self.config.dict_["project_dir"], branch="master"
        )

    def _get_url(self):
        if self.config.github_is_organization():
            return f"https://api.github.com/orgs/{self.config.github_owner()}/repos"

        return "https://api.github.com/user/repos"
