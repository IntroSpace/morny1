import os
import shutil

import requests
import git
from constants import *
from drivers.run_manager import read_configs


def get_list_of_repos():
    all_repos = list()
    installed = get_list_of_installed()
    try:
        response = requests.get('https://api.github.com/users/IntroSpace/repos').json()
        for i in response:
            if i.get('name') not in IGNORE_REPOS and i.get('name') not in installed:
                all_repos.append((i.get('name'), i.get('html_url'), i.get('description', '')))
    except Exception as e:
        print(e)
    return all_repos


def get_list_of_installed():
    return [f.name for f in os.scandir(INSTALL_FOLDER) if f.is_dir()]


def install_repo(repo_name, repo_url):
    save_dir = os.path.join(INSTALL_FOLDER, repo_name)
    git.Repo.clone_from(repo_url, save_dir)
    for to_del in os.scandir(save_dir):
        if to_del.name.startswith('.git'):
            if to_del.is_dir():
                shutil.rmtree(to_del.path)
            else:
                os.remove(to_del.path)
    config = read_configs(repo_name)
    libs = config.get('libs', 'no')
    if libs != 'no':
        libs_fullpath = os.path.join(save_dir, libs)
        if os.path.exists(libs_fullpath):
            os.system(f'pip install -r {libs_fullpath} >/dev/null 2>&1')
