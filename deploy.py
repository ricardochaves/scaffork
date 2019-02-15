import os
import shutil
import subprocess


def start_deploy(project: str, target_dir: str):

    if os.path.exists(target_dir):
        shutil.rmtree(target_dir)

    shutil.copytree("./project", target_dir)

    os.rename(f"{target_dir}/PROJECT_NAME", f"{target_dir}/{project}")

    subprocess.call(
        [f"find {target_dir}/. -type f|xargs perl -pi -e 's/PROJECT_NAME/{project}/g'"], shell=True
    )


def update_travis_badge(value: str, target_dir: str):
    subprocess.call([f"sed -i '' 's/TRAVIS_BADGE/{value}/g' {target_dir}/README.md"], shell=True)


def update_code_climate_badge(coverage: str, maintainability: str, target_dir: str):
    subprocess.call(
        [f"sed -i '' 's/CODECLIMATE_COVERAGE/{coverage}/g' {target_dir}/README.md"], shell=True
    )

    subprocess.call(
        [f"sed -i '' 's/CODECLIMATE_MAINTAINABILITY/{maintainability}/g' {target_dir}/README.md"],
        shell=True,
    )
