from __future__ import print_function
from __future__ import unicode_literals

from PyInquirer import prompt

from scaffork.data import Config


def execute_inquirer(config: Config) -> Config:
    questions = [
        # {
        #     "type": "input",
        #     "name": "clone_source",
        #     "message": "What is the url to clone?",
        #     "when": not config.clone_source(),
        # },
        # {
        #     "type": "input",
        #     "name": "project_name",
        #     "message": "What is the name of the project?",
        #     "when": not config.project_name(),
        # },
        {
            "type": "password",
            "name": "git_hub_token",
            "message": "Enter your personal GitHub token.",
            "when": lambda answers: config.github_owner() and not config.github_token(),
        },
        # {
        #     "type": "input",
        #     "name": "repo_name",
        #     "message": "What is the name of the repository?",
        #     "when": lambda answers: answers["use_git_hub"],
        #     "default": lambda answers: answers["project_name"],
        # },
        # {"type": "input", "name": "project_name", "message": "What is the name of the project?"},
        # {
        #     "type": "input",
        #     "name": "project_dir",
        #     "message": "What directory should the project be created in?",
        # },
        # {
        #     "type": "confirm",
        #     "name": "use_git_hub",
        #     "message": "Want to create a repository on GitHub?",
        #     "default": True,
        # },
        # {
        #     "type": "confirm",
        #     "name": "git_hub_private_repo",
        #     "message": "Is the repository private?",
        #     "when": lambda answers: answers["use_git_hub"],
        #     "default": True,
        # },
        # {
        #     "type": "input",
        #     "name": "repo_name",
        #     "message": "What is the name of the repository?",
        #     "when": lambda answers: answers["use_git_hub"],
        #     "default": lambda answers: answers["project_name"],
        # },
        # {
        #     "type": "rawlist",
        #     "name": "git_org_or_person",
        #     "message": "Choose where it will be created:",
        #     "choices": ["My personal GitHub.", "On my organization's GitHub."],
        #     "when": lambda answers: answers["use_git_hub"],
        # },
        # {
        #     "type": "input",
        #     "name": "repo_ower",
        #     "message": "Informs the user of the organization in GitHub",
        #     "when": lambda answers: (
        #         answers["use_git_hub"]
        #         and (answers["git_org_or_person"] == "On my organization's GitHub.")
        #     ),
        # },
        # {
        #     "type": "input",
        #     "name": "repo_ower",
        #     "message": "Informs you user in GitHub",
        #     "when": lambda answers: (
        #         answers["use_git_hub"] and (answers["git_org_or_person"] == "My personal GitHub.")
        #     ),
        # },
        # {
        #     "type": "input",
        #     "name": "git_hub_token",
        #     "message": "Enter your personal GitHub token.",
        #     "when": lambda answers: answers["use_git_hub"],
        # },
        # {
        #     "type": "confirm",
        #     "name": "use_travis",
        #     "message": "Enable Travis in this repository?",
        #     "default": True,
        #     "when": lambda answers: answers["use_git_hub"],
        # },
        # {
        #     "type": "confirm",
        #     "name": "use_codeclimate",
        #     "message": "Enable CodeClimate in this repository?",
        #     "default": True,
        #     "when": lambda answers: answers["use_git_hub"],
        # },
        # {
        #     "type": "input",
        #     "name": "code_climate_token",
        #     "message": "Enter your CodeClimate token.",
        #     "when": lambda answers: answers["use_git_hub"] and answers["use_codeclimate"],
        # },
        # {
        #     "type": "rawlist",
        #     "name": "code_climate_org_choise",
        #     "message": "You need to enter the Organization ID in CodeClimate.",
        #     "choices": [
        #         "Okay, I know and I will inform.",
        #         "I do not know, use the first one you find bound to me in CodeClimate.",
        #     ],
        #     "when": lambda answers: (
        #         answers["use_git_hub"]
        #         and answers["use_codeclimate"]
        #         and (answers["git_org_or_person"] == "On my organization's GitHub.")
        #     ),
        # },
        # {
        #     "type": "input",
        #     "name": "code_climate_org_id",
        #     "message": "Enter your Oganization id on CodeClimate.",
        #     "when": lambda answers: (
        #         answers["use_git_hub"]
        #         and answers["use_codeclimate"]
        #         and (answers["git_org_or_person"] == "On my organization's GitHub.")
        #         and (answers["code_climate_org_choise"] == "Okay, I know and I will inform.")
        #     ),
        # },
        # {
        #     "type": "input",
        #     "name": "base_64_url",
        #     "message": "Enter your Google Credential Json file.",
        #     "when": lambda answers: answers["use_git_hub"] and answers["use_travis"],
        # },
    ]

    answers = prompt(questions)

    if answers:
        config.dict_["github_token"] = answers["git_hub_token"]

    return config
