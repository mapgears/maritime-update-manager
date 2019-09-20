from __future__ import annotations

from subprocess import run, CompletedProcess

from mum.util.pipenv import get_pipenv_project
from . import UpdateModule


class PgRasterTimeUpdater(UpdateModule):
    def __init__(self, pgrastertime_location, **kwargs):
        self.pipenv_project = get_pipenv_project(pgrastertime_location)

        super().__init__(**kwargs)

    def update(self) -> CompletedProcess:
        return run([self.pipenv_project.which('pgrastertime')])
