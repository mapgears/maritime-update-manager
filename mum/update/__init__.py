"""Update maritime data using update modules"""
from __future__ import annotations

from argparse import ArgumentParser
import base64
import hashlib
import os
import shelve

import toml

from .modules import get_update_module


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('configfile', metavar='config.toml')
    args = parser.parse_args()

    config = toml.load(args.configfile)
    statefile = config.get('statefile')
    if statefile is None:
        location = os.path.realpath(args.configfile)
        hash = hashlib.sha256(location.encode()).digest()[:6]
        encoded_hash = base64.urlsafe_b64encode(hash).decode()
        statefile = f'/var/tmp/mum-{encoded_hash[:8]}.statefile'

    transient_state = {}
    with shelve.open(statefile, writeback=True) as db:
        for updater_config in config.get('updater', []):
            updater_cls = get_update_module(updater_config['module'])
            if updater_config.get('enabled', True):
                updater = updater_cls(**updater_config)
                if updater.needs_update(db, transient_state):
                    updater.update(db, transient_state)

            db.sync()
