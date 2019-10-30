from __future__ import annotations

import itertools
from shutil import which
from subprocess import run

from . import UpdateModule


class _Mapcache(UpdateModule):
    # Class-defined additional parameters
    extra_params = []

    # User-defined additional parameters
    params = []

    def __init__(self, configfile, tileset, params=None, seeder=None,
                 **kwargs):
        if seeder is None:
            seeder = which('mapcache_seed')

        if params is not None:
            self.params = list(itertools.chain.from_iterable(
                (str(k), str(v)) if v is not True else (str(k),)
                for k, v in params.items()
            ))

        self.mapcache_xml = configfile
        self.tileset = tileset
        self.seeder = seeder

        super().__init__(**kwargs)

    def __init_subclass__(cls, *, mode, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.mode = mode

    def update(self, state):
        run([
            self.seeder,
            '-m', self.mode,
            '-c', self.mapcache_xml,
            '-t', self.tileset,
        ] + self.extra_params + self.params)


class MapcacheClear(_Mapcache, mode='delete'):
    pass


class MapcacheSeed(_Mapcache, mode='seed'):
    pass


class MapcacheReseed(_Mapcache, mode='seed'):
    extra_params = ['-o', 'now']
