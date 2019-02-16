class Data:

    data = None

    def __init__(self, inquirer_data: dict):
        self.data = inquirer_data

    def repo_origem_ower(self) -> str:
        return self.data["project_origem"].split("/")[0]

    def repo_origem_name(self) -> str:
        return self.data["project_origem"].split("/")[1]

    def project_name(self) -> str:
        return self.data["project_name"]

    def project_dir(self) -> str:
        return self.data["project_dir"]

    def use_git_hub(self) -> bool:
        return self.data["use_git_hub"]

    def id_private_repo(self) -> bool:
        return self.data["git_hub_private_repo"]

    def repo_name(self) -> str:
        return self.data["repo_name"]

    def is_organization(self) -> bool:
        return self.data["git_org_or_person"] == "On my organization's GitHub."

    def repo_ower(self) -> str:
        return self.data["repo_ower"]

    def git_hub_token(self) -> str:
        return self.data["git_hub_token"]

    def use_travis(self) -> bool:
        return self.data["use_travis"]

    def use_codeclimate(self) -> bool:
        return self.data["use_codeclimate"]

    def code_climate_token(self) -> str:
        return self.data["code_climate_token"]

    def base_64_file(self) -> str:
        return self.data.get("base_64_url")

    def base_64_is_url(self) -> bool:
        return "http:" in self.data["base_64_url"]

    def code_climate_org_id(self) -> str:
        return self.data.get("code_climate_org_id", None)
