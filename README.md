# Maritime Update Manager (MUM)

## Prerequisites

* [Pipenv][pipenv]
* Python 3.7
* [Pyenv][pyenv] (Optional, recommended)

## Install

Install python requirements

`pipenv install`

Configure the updaters

`cp config.sample.toml /path/to/config.toml`

Edit the configuration file as needed.
[More info on the updater modules][updater-doc]

## Running MUM

In the virtual environment, run the `mum_update` command with the config file.

`pipenv run mum_update /path/to/toml`

or 

```
pipenv shell
mum_update /path/to/toml
```

[pipenv]: https://github.com/pypa/pipenv
[pyenv]: https://github.com/pyenv/pyenv
[updater-doc]: ./docs/updaters/
