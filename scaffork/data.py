class Config:
    dict_ = {
        "project_source": None,
        "project_name": None,
        "project_dir": None,
        "use_github": False,
        "github_repo": None,
        "github_is_private": False,
        "github_description": None,
        "github_owner": None,
        "github_is_organization": False,
        "github_has_issues": False,
        "github_has_projects": False,
        "github_has_wiki": False,
        "github_token": None,
        "github_home_page": None,
        "use_travis": False,
        "travis_envs": [],
        "use_codeclimate": False,
        "use_codeclimate_maintainability": False,
        "use_codeclimate_coverage": False,
        "codeclimate_token": None,
        "codeclimate_organization_id": None,
    }

    def __init__(self, init_config: dict):
        self._parse_config(init_config)

    def _parse_config(self, init_config: dict) -> None:

        self.dict_["project_source"] = init_config["project"]["source"]
        self.dict_["project_name"] = init_config["project"]["name"]
        self.dict_["project_dir"] = init_config["project"]["dir"]

        if init_config.get("github"):
            self.dict_["use_github"] = True
            self.dict_["github_repo"] = init_config["github"]["repo"]
            self.dict_["github_is_private"] = init_config["github"].get("is_private", False)
            self.dict_["github_description"] = init_config["github"].get("description", None)
            self.dict_["github_owner"] = init_config["github"]["owner"]
            self.dict_["github_is_organization"] = init_config["github"].get("is_organization", False)
            self.dict_["github_has_issues"] = init_config["github"].get("has_issues", False)
            self.dict_["github_has_projects"] = init_config["github"].get("has_projects", False)
            self.dict_["github_has_wiki"] = init_config["github"].get("has_wiki", False)
            self.dict_["github_token"] = init_config["github"].get("token", None)
            self.dict_["github_home_page"] = init_config["github"].get("homepage", None)
            if init_config.get("travis"):
                self.dict_["use_travis"] = True
                for env in init_config["travis"]["envs"]:
                    self.dict_["travis_envs"].append(env)

            if init_config.get("codeclimate"):
                self.dict_["use_codeclimate"] = True
                self.dict_["use_codeclimate_maintainability"] = init_config["codeclimate"].get("maintainability", False)
                self.dict_["use_codeclimate_coverage"] = init_config["codeclimate"].get("coverage", False)
                self.dict_["codeclimate_token"] = init_config["codeclimate"].get("token", None)
                self.dict_["codeclimate_organization_id"] = init_config["codeclimate"].get("organization_id")

    def use_github(self):
        return self.dict_["use_github"]

    def use_travis(self):
        return self.dict_["use_travis"]

    def use_codeclimate(self):
        return self.dict_["use_codeclimate"]

    def github_owner(self):
        return self.dict_["github_owner"]

    def github_token(self):
        return self.dict_["github_token"]

    def github_repo_simple_url(self):
        return f"{self.dict_['github_owner']}/{self.dict_['github_repo']}"

    def github_repo(self):
        return self.dict_["github_repo"]

    def github_description(self):
        return self.dict_["github_description"]

    def github_home_page(self):
        return self.dict_["github_home_page"]

    def github_has_issuer(self):
        return self.dict_["github_has_issues"]

    def github_is_private(self):
        return self.dict_["github_is_private"]

    def github_has_projects(self):
        return self.dict_["github_has_projects"]

    def github_has_wiki(self):
        return self.dict_["github_has_wiki"]

    def github_is_organization(self):
        return self.dict_["github_is_organization"]

    def project_dir(self):
        return self.dict_["project_dir"]

    def project_origin_name(self):
        return self.dict_["project_source"].split("/")[1][:-4]

    def project_origin_owner(self):
        return self.dict_["project_source"].split("/")[0].split(":")[1]

    def project_name(self):
        return self.dict_["project_name"]

    def travis_envs(self):
        return self.dict_["travis_envs"]

    def codeclimate_organization_id(self):
        return self.dict_["codeclimate_organization_id"]

    def codeclimate_token(self):
        return self.dict_["codeclimate_token"]

    def codeclimate_use_coverage(self):
        return self.dict_["use_codeclimate_coverage"]

    def codeclimate_use_maintainability(self):
        return self.dict_["use_codeclimate_maintainability"]
