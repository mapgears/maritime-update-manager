from pipenv.project import Project

from .path import chdir


def get_pipenv_project(path):
    with chdir(path):
        return Project()
