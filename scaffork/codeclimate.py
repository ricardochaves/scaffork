import requests

from scaffork.data import Config


class CodeClimate:
    repo_data: dict = None

    def __init__(self, config: Config):
        self.config = config

    def enable_repo(self):
        if self.config.github_is_organization():
            self.__enable_organization_repo()
        else:
            self.__enable_user_repo()

    def __enable_organization_repo(self):

        org_id = self.config.codeclimate_organization_id()
        if not org_id:
            org_id = self.__get_first_organization()

        url = f"https://api.codeclimate.com/v1/orgs/{org_id}/repos"
        response = requests.post(url, json=self.__get_data(), headers=self.__get_headers())
        if response.status_code != 201:
            raise Exception(f"Error on CodeClimate: {response.text}")

    def __enable_user_repo(self):
        url = "https://api.codeclimate.com/v1/github/repos"
        response = requests.post(url, json=self.__get_data(), headers=self.__get_headers())
        if response.status_code != 201:
            raise Exception(f"Error on CodeClimate: {response.text}")

    def __get_data(self):
        return {
            "data": {
                "type": "repos",
                "attributes": {"url": f"https://github.com/{self.config.github_owner()}/{self.config.github_repo()}"},
            }
        }

    def __get_headers(self):
        return {
            "Accept": "application/vnd.api+json",
            "Authorization": f"Token token={self.config.codeclimate_token()}",
            "Content-Type": "application/vnd.api+json",
        }

    def __get_first_organization(self):

        url = "https://api.codeclimate.com/v1/orgs"
        response = requests.get(url, headers=self.__get_headers())
        return response.json()["data"][0]["id"]

    def get_maintainability_badge(self) -> str:
        return self.get_repo_data()["data"][0]["links"]["maintainability_badge"]

    def get_test_coverage_badge(self) -> str:
        return self.get_repo_data()["data"][0]["links"]["test_coverage_badge"]

    def get_test_reporter_id(self) -> str:
        return self.get_repo_data()["data"][0]["attributes"]["test_reporter_id"]

    def get_repo_data(self) -> dict:

        if not self.repo_data:
            url = f"https://api.codeclimate.com/v1/repos?github_slug={self.config.github_repo_simple_url()}"
            response = requests.get(url, headers=self.__get_headers())
            self.repo_data = response.json()
        return self.repo_data
