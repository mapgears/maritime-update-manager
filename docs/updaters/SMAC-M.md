# SMAC-M data (`smac-m-data`)

Generates the Shapefiles from ENC data using SMAC-M.

```toml
[[updater]]
module = "smac-m-data"
smac_location = "/path/to/smac-m/"
configfile = "/path/to/config.toml"
```

* `smac_location`

  Location of the SMAC-M repository. This is the directory containing the
  Pipfile for SMAC-M. The repository must already be configured; see [the 
  repository][smac-m repo] for installation instructions.

* `configfile`

  Location of the SMAC-M toml configuration file.

# SMAC-M mapfiles (`smac-m-mapfile`)

Generates the Shapefiles from shapefile data using SMAC-M.

```toml
[[updater]]
module = "smac-m-mapfile"
smac_location = "/path/to/smac-m/"
configfile = "/path/to/config.toml"
```

* `smac_location`

  Location of the SMAC-M repository. This is the directory containing the
  Pipfile for SMAC-M. The repository must already be configured; see [the 
  repository][smac-m repo] for installation instructions.

* `configfile`

  Location of the SMAC-M toml configuration file.

[smac-m repo]: https://github.com/LarsSchy/SMAC-M
