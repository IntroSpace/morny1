from drivers.cmd_worker import *
from drivers.internet_manager import *
from drivers.run_manager import run_repo

if __name__ == '__main__':
    while True:
        com = index_page()
        if com == 1:
            repos, com, exit_bool = choose_repo_to_run()
            if exit_bool:
                continue
            cur_repo = repos[com - 1]
            run_repo(cur_repo)
        elif com == 2:
            repos, com = choose_repo_to_install()
            with Loader("Loading repository...", timeout=0.5):
                cur_repo = repos[com - 1]
                install_repo(*cur_repo[:-1])
        elif com == 4:
            print('Bye-bye :)')
            break
