from base_64 import get_base_64
from codeclimate import CodeClimate
from data import Data
from deploy import start_deploy
from deploy import update_code_climate_badge
from deploy import update_travis_badge
from github import GitHub
from travis import Travis


def start(data: Data):

    start_deploy(data.project_name(), data.project_dir())

    if data.use_git_hub():
        github = GitHub(data)
        github.execute()
        travis = Travis(data)

        if data.use_travis():
            travis.enable_repo()

            if data.base_64_file():
                travis.set_envs("GCLOUD_SERVICE_KEY_DEV", get_base_64(data), False)

            update_travis_badge(travis.get_badge_value(), data.project_dir())
            github.commit("Update Travis Badge")
        else:
            update_travis_badge("", data.project_dir())
            github.commit("Remove Travis Badge")

        if data.use_codeclimate():
            code_climate = CodeClimate(data)
            code_climate.enable_repo()

            if data.use_travis():
                travis.set_envs("CC_TEST_REPORTER_ID", code_climate.get_test_reporter_id, False)

            update_code_climate_badge(
                code_climate.get_test_coverage_badge(), code_climate.get_maintainability_badge()
            )


# verificar se é organização para o codeclimate
