from __future__ import annotations

import itertools
import json
from shutil import which
from subprocess import run
from tempfile import NamedTemporaryFile

from mum.util.geom import list_of_extents_to_geojson
from . import UpdateModule

from typing import List


class _Mapcache(UpdateModule):
    # Class-defined additional parameters
    extra_params = []

    # User-defined additional parameters
    params = []

    def __init__(self, configfile, tileset, params=None, seeder=None,
                 proj='EPSG:4326',
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
        self.proj = proj

        super().__init__(**kwargs)

    def __init_subclass__(cls, *, mode, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.mode = mode

    def needs_update(self, state, transient_state):
        # We need to update if someone set extents for our tag, or if no one
        # using extents is using our tag
        return bool(transient_state.get(f'extents.{self.tag}', True))

    def update(self, state, transient_state):
        extents = transient_state.get(f'extents.{self.tag}', [])
        if not extents:
            self._run_mapcache([])
        else:
            with NamedTemporaryFile(
                suffix='.geojson', mode='w', encoding='utf-8'
            ) as ds:
                json.dump(list_of_extents_to_geojson(extents), ds)
                ds.flush()
                with NamedTemporaryFile(
                    suffix='.geojson',
                    mode='w',
                    encoding='utf-8',
                ) as projected:
                    run([
                        'ogr2ogr',
                        '-f', 'GeoJSON',
                        '-t_srs', self.proj,
                        projected.name,
                        ds.name,
                    ])
                    self._run_mapcache(['-d', projected.name])

    def _run_mapcache(self, datasource: List[str]):
        run([
            self.seeder,
            '-m', self.mode,
            '-c', self.mapcache_xml,
            '-t', self.tileset,
        ] + self.extra_params + self.params + datasource)


class MapcacheClear(_Mapcache, mode='delete'):
    pass


class MapcacheSeed(_Mapcache, mode='seed'):
    pass


class MapcacheReseed(_Mapcache, mode='seed'):
    extra_params = ['-o', 'now']
