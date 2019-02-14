import requests

from data import Data


class CodeClimate:

    data: Data
    repo_data: dict

    def __init__(self, data: Data):
        self.data = data

    def enable_repo(self):
        if self.data.is_organization():
            self.__enable_organization_repo()
        else:
            self.__enable_user_repo()

    def __enable_organization_repo(self):
        if not self.data.code_climate_org_id():
            org_id = self.__get_first_organization()
        else:
            org_id = self.data.code_climate_org_id()

        url = f"https://api.codeclimate.com/v1/orgs/{org_id}/repos"
        response = requests.post(url, json=self.__get_data(), headers=self.__get_headers())
        if response.status_code != 201:
            raise Exception(f"Erro on CodeClimate: {response.text}")

    def __enable_user_repo(self):
        url = "https://api.codeclimate.com/v1/github/repos"
        response = requests.post(url, json=self.__get_data(), headers=self.__get_headers())
        if response.status_code != 201:
            raise Exception(f"Erro on CodeClimate: {response.text}")

    def __get_data(self):
        return {
            "data": {
                "type": "repos",
                "attributes": {
                    "url": f"https://github.com/{self.data.repo_ower()}/{self.data.repo_name()}"
                },
            }
        }

    def __get_headers(self):
        return {
            "Accept": "application/vnd.api+json",
            "Authorization": f"Token token={self.data.code_climate_token()}",
            "Content-Type": "application/vnd.api+json",
        }

    def __get_first_organization(self):

        url = "https://api.codeclimate.com/v1/orgs"
        response = requests.get(url, headers=self.__get_headers())
        return response.json()["data"][0]["id"]

    def get_maintainability_badge(self):
        return self.get_repo_data()["data"]["links"]["maintainability_badge"]

    def get_test_coverage_badge(self):
        return self.get_repo_data()["data"]["links"]["test_coverage_badge"]

    def get_test_reporter_id(self):
        return self.get_repo_data()["data"]["attributes"]["test_reporter_id"]

    def get_repo_data(self):

        if not self.repo_data:
            url = f"https://api.codeclimate.com/v1/repos?github_slug={self.data.repo_ower()}/{self.data.repo_name()}"
            response = requests.get(url, headers=self.__get_headers())
            self.repo_data = response.json()
        return self.repo_data


# [![Test Coverage](CODECLIMATE_COVERAGE_MASTER)](https://codeclimate.com/repos/5c5b75c01102160285001cef/test_coverage) [![Maintainability](CODECLIMATE_MAINTAINABILITY_MASTER)](https://codeclimate.com/repos/5c5b75c01102160285001cef/maintainability)
