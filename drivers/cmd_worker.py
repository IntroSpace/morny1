from itertools import cycle
from shutil import get_terminal_size
from threading import Thread
from time import sleep

from drivers.internet_manager import get_list_of_repos, get_list_of_installed
from constants import *


class Loader:
    def __init__(self, desc="Loading...", end="Done!", timeout=0.1):
        """
        A loader-like context manager

        Args:
            desc (str, optional): The loader's description. Defaults to "Loading...".
            end (str, optional): Final print. Defaults to "Done!".
            timeout (float, optional): Sleep time between prints. Defaults to 0.1.
        """
        self.desc = desc
        self.end = end
        self.timeout = timeout

        self._thread = Thread(target=self._animate, daemon=True)
        self.steps = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
        self.done = False

    def start(self):
        self._thread.start()
        return self

    def _animate(self):
        for c in cycle(self.steps):
            if self.done:
                break
            print(f"\r{self.desc} {c}", flush=True, end="")
            sleep(self.timeout)

    def __enter__(self):
        self.start()

    def stop(self):
        self.done = True
        cols = get_terminal_size((80, 20)).columns
        print("\r" + " " * cols, end="", flush=True)
        print(f"\r{self.end}", flush=True)

    def __exit__(self, exc_type, exc_value, tb):
        self.stop()


def choose_repo_to_install():
    print('All repos to install:')
    repos = get_list_of_repos()
    print('\n'.join(map(lambda x: f'{x[0] + 1}. {x[1][0]}'
                                  + (f' - {x[1][2]}' if x[1][2] else ''),
                        enumerate(repos))))
    com = int(input('Choose repo: '))
    print('-' * 10)
    return repos, com


def choose_repo_to_run():
    print('All repos to run:')
    repos = get_list_of_installed()
    print('\n'.join(map(lambda x: f'{x[0] + 1}. {x[1]}', enumerate(repos))))
    exit_index = len(repos) + 1
    print(f'{exit_index}. exit')
    com = int(input('Choose repo: '))
    if com == exit_index:
        print('-' * 10)
    return repos, com, com == exit_index


def index_page():
    print('Choose action:')
    print('\n'.join(map(lambda x: f'{x[0] + 1}. {x[1]}', enumerate(MAIN_ACTIONS))))
    com = int(input('Choose action: '))
    print('-' * 10)
    return com
