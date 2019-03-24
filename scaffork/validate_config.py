import sys

import yaml
from blessings import Terminal


def _print_codeclimate_helper() -> None:
    t = Terminal()
    print(
        f"""
        You are using the {t.bold}codeclimate{t.normal} tag, for this you need to tell which codeclimate tools you will use. 
        You have two options, {t.bold}maintainability{t.normal} and / or {t.bold}coverage{t.normal}.

        {t.bold}codeclimate:{t.normal}
          {t.bold}maintainability:{t.normal} {t.green}True{t.normal}
          {t.bold}coverage:{t.normal} {t.green}True{t.normal}
        """
    )


def _print_project_key_helper(key: str) -> None:
    t = Terminal()
    print(
        f"""
        {t.red}{key}{t.normal} key not found, use:

        {t.bold}project:{t.normal}
          {t.bold}name:{t.normal} {t.green}my_project_name{t.normal}
          {t.bold}source:{t.normal} {t.green}url_to_clone{t.normal}
          {t.bold}dir:{t.normal} {t.green}dir_to_create_project{t.normal}
        """
    )


def _print_github_key_helper(key: str) -> None:
    t = Terminal()
    print(
        f"""
        {t.red}{key}{t.normal} key not found, use:

        {t.bold}github:{t.normal}
          {t.bold}repo:{t.normal} {t.green}github_repo_name{t.normal}
          {t.bold}owner:{t.normal} {t.green}github_repo_owner_user{t.normal}
        """
    )


def validate_config(file: str) -> None:
    with open(file, "r") as stream:
        config = yaml.load(stream)

    if config.get("project"):
        if not config["project"].get("name"):
            _print_project_key_helper("project name")
        if not config["project"].get("source"):
            _print_project_key_helper("project source")
        if not config["project"].get("dir"):
            _print_project_key_helper("project dir")
    else:
        _print_project_key_helper("project")

    if config.get("github"):
        if not config["github"].get("repo"):
            _print_github_key_helper("github repo")
        if not config["github"].get("owner"):
            _print_github_key_helper("github owner")

    if config.get("codeclimate"):
        if (
            (config["codeclimate"].get("maintainability", False) is False)
            or (config["codeclimate"].get("maintainability", False) is None)
        ) and (
            (config["codeclimate"].get("coverage", False) is False)
            or (config["codeclimate"].get("coverage", False) is None)
        ):
            _print_codeclimate_helper()


if __name__ == "__main__":
    validate_config(sys.argv[1])
