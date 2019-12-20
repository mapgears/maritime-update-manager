from __future__ import annotations

import os
from pathlib import Path
import re
from subprocess import run, CompletedProcess

import toml

from mum.util.pipenv import get_pipenv_project

from . import UpdateModule


class SmacUpdater(UpdateModule):
    __slots__ = ('pipenv_project', 'configfile', 'config', 'basepath')

    def __init__(self, smac_location, configfile, **kwargs):
        self.pipenv_project = get_pipenv_project(smac_location)

        self.configfile = configfile
        self.config = None
        self.basepath = Path(self.configfile).parent.resolve()

        super().__init__(**kwargs)

    def execute_smac_script(self, script: str) -> CompletedProcess:
        """Execute a script in the SMAC repository using the config file"""
        return run([
            self.python,
            os.path.join(self.pipenv_project.project_directory, script),
            self.configfile
        ])

    def get_path(self, path_key):
        if self.config is None:
            self.config = toml.load(self.configfile)

        return self.basepath / self.config['paths'][path_key]

    @property
    def python(self):
        return self.pipenv_project.which('python')


class SmacDataUpdater(SmacUpdater):
    __slots__ = ()

    _script = 'bin/generate_shapefiles.py'

    re_num = r'(-?[0-9]+(?:\.[0-9]+)?)'

    EXTENT_RE = re.compile(
        rf'Extent: \({re_num}, {re_num}\) - \({re_num}, {re_num}\)'
    )
    del re_num

    def get_extent(self, file):
        proc = run(
            ['ogrinfo', os.fspath(file), '-so', 'M_COVR'],
            capture_output=True,
            text=True,
        )
        for line in proc.stdout.splitlines():
            m = self.EXTENT_RE.match(line)
            if m:
                return [float(c) for c in m.groups()]

    def needs_update(self, state, transient_state):
        smac_charts = state.setdefault('smac charts', {})
        charts_last_seen = smac_charts.setdefault(self.tag, {})

        new_files_tag = f'smac.{self.tag}'
        transient_state[new_files_tag] = False
        extents = transient_state.setdefault(f'extents.{self.tag}', [])

        charts_root = self.get_path('chart')
        for chart in charts_root.glob('**/*.000'):
            chart_dir = chart.parent
            old_charts = charts_last_seen.get(chart_dir.name, set())
            new_charts = {c.name for c in chart_dir.glob('*')}
            if old_charts != new_charts:
                extent = self.get_extent(chart)
                if extent:
                    transient_state[new_files_tag] = True
                    charts_last_seen[chart_dir.name] = new_charts
                    extents.append(extent)

        return transient_state[new_files_tag]

    def update(self, state, transient_state):
        return self.execute_smac_script(self._script)


class SmacMapUpdater(SmacUpdater):
    __slots__ = ()

    _script = 'chart-installation/generate_map_files/generate_map_config.py'

    def needs_update(self, state, transient_state):
        return transient_state.get(f'smac.{self.tag}', True)

    def update(self, state, transient_state):
        return self.execute_smac_script(self._script)
