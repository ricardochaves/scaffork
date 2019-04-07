from scaffork.base_64 import get_base_64
from scaffork.codeclimate import CodeClimate
from scaffork.deploy import AdminFiles
from scaffork.github import GitHub
from scaffork.inquirer import execute_inquirer
from scaffork.load_config import load_config_yaml
from scaffork.travis import Travis


def main(scaffork_yml_file: str) -> None:

    config = load_config_yaml(scaffork_yml_file)

    config = execute_inquirer(config)

    git = GitHub(config)
    admin_files = AdminFiles(config)
    travis = Travis(config)
    codeclimate = CodeClimate(config)

    git.clone()
    admin_files.change_project_name()

    if config.use_github():
        git.create_remote_repo()
        git.init_and_push()

    if config.use_travis():
        travis.enable_repo()
        for env in config.travis_envs():
            value = env["value"]
            if env["type"] == "base64":
                value = get_base_64(value)

            travis.set_envs(env["name"], value, env["public"])

        if not config.github_is_private():
            admin_files.update_travis_badge()
            git.commit("Update Travis Badge")

    if config.use_codeclimate():
        codeclimate.enable_repo()

        if config.codeclimate_use_coverage():
            travis.set_envs("CC_TEST_REPORTER_ID", codeclimate.get_test_reporter_id(), False)
            admin_files.update_codeclimate_coverage_badge(codeclimate.get_test_coverage_badge())
            git.commit("Update codeclimate coverage badge")
        if config.codeclimate_use_maintainability():
            admin_files.update_codeclimate_maintainability_badge(codeclimate.get_maintainability_badge())
            git.commit("Update codeclimate maintainability badge")
