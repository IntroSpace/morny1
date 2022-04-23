import os

import requests
import git
from constants import *


def get_list_of_repos():
    all_repos = list()
    installed = [f.name for f in os.scandir(INSTALL_FOLDER) if f.is_dir()]
    try:
        response = requests.get('https://api.github.com/users/IntroSpace/repos').json()
        for i in response:
            if i.get('name') not in IGNORE_REPOS and i.get('name') not in installed:
                all_repos.append((i.get('name'), i.get('html_url')))
    except Exception as e:
        print(e)
    return all_repos


def install_repo(repo_name, repo_url):
    git.Repo.clone_from(repo_url, INSTALL_FOLDER + '/' + repo_name)
