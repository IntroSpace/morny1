from drivers.cmd_worker import *
from drivers.internet_manager import *


if __name__ == '__main__':
    com = index_page()
    if com == 2:
        repos, com = choose_repo_to_install()
        with Loader("Loading repository...", timeout=0.5):
            cur_repo = repos[com - 1]
            install_repo(*cur_repo)
