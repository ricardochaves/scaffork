import os
import shutil
import subprocess


def start_deploy(project: str, target_dir: str):

    if os.path.exists(target_dir):
        shutil.rmtree(target_dir)

    shutil.copytree("./project", target_dir)

    os.rename(f"{target_dir}/PROJECT_NAME", f"{target_dir}/{project}")

    subprocess.call(
        [f"sed -i -e 's/PROJECT_NAME/{project}/g' {target_dir}/.travis.yml"], shell=True
    )
    subprocess.call([f"sed -i -e 's/PROJECT_NAME/{project}/g' {target_dir}/manage.py"], shell=True)
    subprocess.call(
        [f"sed -i -e 's/PROJECT_NAME/{project}/g' {target_dir}/{project}/settings.py"], shell=True
    )
    subprocess.call(
        [f"sed -i -e 's/PROJECT_NAME/{project}/g' {target_dir}/{project}/urls.py"], shell=True
    )
    subprocess.call(
        [f"sed -i -e 's/PROJECT_NAME/{project}/g' {target_dir}/{project}/wsgi.py"], shell=True
    )
    subprocess.call([f"sed -i -e 's/PROJECT_NAME/{project}/g' {target_dir}/README.md"], shell=True)
    subprocess.call([f"sed -i -e 's/PROJECT_NAME/{project}/g' {target_dir}/tox.ini"], shell=True)
    subprocess.call(
        [f"sed -i -e 's/PROJECT_NAME/{project}/g' {target_dir}/kubernetes/all.yml"], shell=True
    )
    subprocess.call(
        [f"sed -i -e 's/PROJECT_NAME/{project}/g' {target_dir}/kubernetes/configmap.yml"],
        shell=True,
    )

    os.remove(f"{target_dir}/.travis.yml-e")
    os.remove(f"{target_dir}/manage.py-e")
    os.remove(f"{target_dir}/{project}/urls.py-e")
    os.remove(f"{target_dir}/{project}/wsgi.py-e")
    os.remove(f"{target_dir}/README.md-e")
    os.remove(f"{target_dir}/tox.ini-e")
    os.remove(f"{target_dir}/kubernetes/all.yml-e")
    os.remove(f"{target_dir}/kubernetes/configmap.yml-e")


def update_travis_badge(value: str, target_dir: str):
    subprocess.call([f"sed -i -e 's/TRAVIS_BADGE/{value}/g' {target_dir}/README.md"], shell=True)
    os.remove(f"{target_dir}/README.md-e")


def update_code_climate_badge(coverage: str, maintainability: str, target_dir: str):
    subprocess.call(
        [f"sed -i -e 's/CODECLIMATE_COVERAGE/{coverage}/g' {target_dir}/README.md"], shell=True
    )
    os.remove(f"{target_dir}/README.md-e")

    subprocess.call(
        [f"sed -i -e 's/CODECLIMATE_MAINTAINABILITY/{maintainability}/g' {target_dir}/README.md"],
        shell=True,
    )
    os.remove(f"{target_dir}/README.md-e")

