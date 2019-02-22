import logging
import os
import shutil

_logger = logging.getLogger('hestia.paths')

# noqa


def check_or_create_path(path: str = None) -> None:
    if not os.path.exists(path):
        os.makedirs(path)


def delete_path(path: str) -> None:
    if not os.path.exists(path):
        return
    try:
        if os.path.isfile(path):
            os.remove(path)
        else:
            shutil.rmtree(path)
    except OSError:
        _logger.warning('Could not delete path `%s`', path)


def create_path(path: str) -> None:
    try:
        os.mkdir(path)
    except FileExistsError:
        pass
    except OSError as e:
        _logger.warning('Could not create path `%s`, exception %s', path, e)


def get_tmp_path(path: str) -> str:
    return os.path.join('/tmp', path)


def create_tmp_dir(dir_name: str) -> None:
    create_path(get_tmp_path(dir_name))


def delete_tmp_dir(dir_name: str) -> None:
    delete_path(get_tmp_path(dir_name))


def copy_to_tmp_dir(path: str, dir_name: str) -> str:
    tmp_path = get_tmp_path(dir_name)
    if os.path.exists(tmp_path):
        return tmp_path
    try:
        shutil.copytree(path, tmp_path)
    except FileExistsError as e:
        _logger.warning('Path already exists `%s`, exception %s', path, e)
    return tmp_path
