from __future__ import annotations

import os
from subprocess import run, CompletedProcess

from mum.util.pipenv import get_pipenv_project

from . import UpdateModule


class SmacUpdater(UpdateModule):
    __slots__ = ('pipenv_project', 'configfile',)

    def __init__(self, smac_location, configfile, **kwargs):
        self.pipenv_project = get_pipenv_project(smac_location)

        self.configfile = configfile
        super().__init__(**kwargs)

    def execute_smac_script(self, script: str) -> CompletedProcess:
        """Execute a script in the SMAC repository using the config file"""
        return run([
            self.python,
            os.path.join(self.pipenv_project.project_directory, script),
            self.configfile
        ])

    @property
    def python(self):
        return self.pipenv_project.which('python')


class SmacDataUpdater(SmacUpdater):
    __slots__ = ()

    _script = 'bin/generate_shapefiles.py'

    def update(self):
        return self.execute_smac_script(self._script)


class SmacMapUpdater(SmacUpdater):
    __slots__ = ()

    _script = 'chart-installation/generate_map_files/generate_map_config.py'

    def update(self):
        return self.execute_smac_script(self._script)
