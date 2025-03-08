import os

from actions.action_react_native import rename_pkg, create_dirs
from scripts.tif_env import TEMP_PATH
from scripts.tif_yaml import app_yaml


def pre():
    name = app_yaml.name
    pth = os.path.join(TEMP_PATH, name)

    # cmd = f'npx --yes react-native init {name} \
    # --template react-native-template-typescript'
    # os.system(cmd)
    os.chdir(pth)
    # rename_pkg()
    # create_dirs()
