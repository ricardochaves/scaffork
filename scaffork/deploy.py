import fileinput
import os
import subprocess

from scaffork.data import Config


class AdminFiles:
    def __init__(self, config: Config):
        self.config = config

    def _get_readme_file_dir(self):
        return f"{self.config.project_dir()}/README.md"

    def change_project_name(self):

        os.rename(
            f"{self.config.project_dir()}/{self.config.project_origin_name()}",
            f"{self.config.project_dir()}/{self.config.project_name()}",
        )

        subprocess.call(
            [
                f"find {self.config.project_dir()}/. -type f|xargs perl -pi -e 's/{self.config.project_origin_name()}/{self.config.project_name()}/g'"
            ],
            shell=True,
        )

    def update_travis_badge(self):
        subprocess.call(
            [
                f"sed -i '' 's;{self.config.project_origin_owner()}/{self.config.project_name()};{self.config.github_owner()}/{self.config.github_repo()};g' {self._get_readme_file_dir()}"
            ],
            shell=True,
        )

    def update_codeclimate_coverage_badge(self, value: str) -> None:

        regex_coverage = r"Coverage](\(https://api.codeclimate.com/v1/badges/.*?test_coverage)"
        subprocess.call(
            [f"perl -p -i -e 's;{regex_coverage};Coverage]({value};g' {self._get_readme_file_dir()}"], shell=True
        )

    def update_codeclimate_maintainability_badge(self, value: str) -> None:
        regex_maintainability = r"Maintainability](\(https://api.codeclimate.com/v1/badges/.*?maintainability)"
        subprocess.call(
            [f"perl -p -i -e 's;{regex_maintainability};Maintainability]({value};g' {self._get_readme_file_dir()}"],
            shell=True,
        )
