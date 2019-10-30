# MUM configuration file

The configuration file for MUM is a [TOML] file.

## Main configuration

- `statefile`
  
  Path to a file where MUM update modules can save information across runs. If
  not set, MUM will try to find an appropriate place to save its state.

## Email configuration (`[email]`)

  TBD

## Updater module configuration (`[[updater]]`)

  See the [updater documentation] for more information on the updater modules
  configuration.


[TOML]: https://github.com/toml-lang/toml/blob/master/versions/en/toml-v0.5.0.md
[updater documentation]: ./updaters/
