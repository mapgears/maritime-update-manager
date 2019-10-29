"""Update maritime data using update modules"""

from argparse import ArgumentParser

import toml

from .modules import get_update_module


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('configfile', metavar='config.toml')
    args = parser.parse_args()

    config = toml.load(args.configfile)

    for updater_config in config.get('updater', []):
        updater_cls = get_update_module(updater_config['module'])
        if updater_config.get('enabled', True):
            updater = updater_cls(**updater_config)
            if updater.needs_update():
                updater.update()
