import os
import subprocess

from data import Data


class AdminFiles:

    data: Data

    def __init__(self, data: Data):

        self.data = data

    def start_deploy(self):

        os.rename(
            f"{self.data.project_dir()}/{self.data.repo_origem_name()}",
            f"{self.data.project_dir()}/{self.data.project_name()}",
        )

        subprocess.call(
            [
                f"find {self.data.project_dir()}/{self.data.project_name()}/. -type f|xargs perl -pi -e 's/PROJECT_NAME/{self.data.project_name()}/g'"
            ],
            shell=True,
        )

    def update_travis_badge(self, value: str):
        subprocess.call(
            [
                f"sed -i '' 's/TRAVIS_BADGE/{value}/g' {self.data.project_dir()}/{self.data.project_name()}/README.md"
            ],
            shell=True,
        )

    def update_code_climate_badge(self, coverage: str, maintainability: str):
        subprocess.call(
            [
                f"sed -i '' 's/CODECLIMATE_COVERAGE/{coverage}/g' {self.data.project_dir()}/{self.data.project_name()}/README.md"
            ],
            shell=True,
        )

        subprocess.call(
            [
                f"sed -i '' 's/CODECLIMATE_MAINTAINABILITY/{maintainability}/g' {self.data.project_dir()}/{self.data.project_name()}/README.md"
            ],
            shell=True,
        )
