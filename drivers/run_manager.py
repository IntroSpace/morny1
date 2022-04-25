import json
import os
import sys

from constants import INSTALL_FOLDER


def run_repo(repo_name):
    run_dir = os.path.join(INSTALL_FOLDER, repo_name)
    config = read_configs(repo_name)
    exec_file = os.path.join(*config.get('run', ['main.py']))
    print('-' * 5 + f' {repo_name} ' + '-' * 5)
    os.system('cd %s; %s %s' % (run_dir, sys.executable, exec_file))
    symbols_count = 2 + len(repo_name) / 2
    print('-' * int(symbols_count) + 'finished' + '-' * int(symbols_count + 0.5))


def read_configs(repo_name):
    config_file = os.path.join(INSTALL_FOLDER, repo_name, '.mrn', 'config')
    if not os.path.exists(config_file):
        return dict()
    with open(config_file) as file:
        return json.load(file)
