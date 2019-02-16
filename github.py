import os
import subprocess

import git
import requests

from data import Data


class GitHub:

    data: Data

    def __init__(self, data: Data):
        self.data = data

    def getPostData(self):

        data = {
            "name": self.data.repo_name(),
            "description": "",
            "homepage": "",
            "private": self.data.id_private_repo(),
            "has_issues": "true",
            "has_projects": "true",
            "has_wiki": "true",
        }
        return data

    def getPostHeaders(self):
        headers = {
            "Authorization": f"token {self.data.git_hub_token()}",
            "Content-Type": "application/json",
        }
        return headers

    def create_repo(self):
        response = requests.post(
            self.get_url(), json=self.getPostData(), headers=self.getPostHeaders()
        )
        if response.status_code != 201:
            raise Exception(f"Erro on post git: {response.text}")

    def init_and_push_local_repo(self):
        subprocess.call([f"git init {self.data.project_dir()} > /dev/null 2>&1"], shell=True)

        subprocess.call(
            [
                f"git --git-dir={self.data.project_dir()}/.git remote add origin git@github.com:{self.data.repo_ower()}/{self.data.repo_name()}.git > /dev/null 2>&1"
            ],
            shell=True,
        )

        self.commit("first commit")

    def commit(self, message: str):
        subprocess.call([f"cd {self.data.project_dir()} && git add . > /dev/null 2>&1"], shell=True)
        subprocess.call(
            [
                f"git --git-dir={self.data.project_dir()}/.git commit -m '{message}' > /dev/null 2>&1"
            ],
            shell=True,
        )
        subprocess.call(
            [
                f"git --git-dir={self.data.project_dir()}/.git push -u origin master > /dev/null 2>&1"
            ],
            shell=True,
        )

    def execute(self):
        self.create_repo()
        self.init_and_push_local_repo()

    def get_url(self):
        if self.data.is_organization():
            return f"https://api.github.com/orgs/{self.data.repo_ower()}/repos"
        else:
            return "https://api.github.com/user/repos"

    def clone_repo(self):
        if not os.path.exists(self.data.project_dir()):
            os.mkdir(self.data.project_dir())
        git.Git(self.data.project_dir()).clone(
            f"git@github.com:{self.data.repo_origem_ower()}/{self.data.repo_origem_name()}.git"
        )
