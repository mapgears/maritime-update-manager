# MapCache Seeder (`mapcache-seed`)

Seeds a MapCache cache.

```toml
[[updater]]
module = "mapcache-seed"
configfile = "/path/to/mapcache.xml"
tileset = "tileset"

seeder = "/path/to/mapcache_seed"  # Optional

[updater.params]  # Optional
-n = 3
--metasize = "4,4"
```

* `configfile`

  Location of the MapCache xml configuration file.

* `tileset`

  Name of the tileset to seed.

* `seeder` (Optional)

  Path to the mapcache_seed executable. If not set, the module will use the
  first executable named `mapcache_seed` found on the PATH.

* `[update.params]` (Optional)
 
  Additional parameters to pass to to the seeder. If a parameter has the value
  `true`, it will be passed as a flag to the seeder; otherwise, both the flag
  and its value will be passed. For example, the flags `-M 4,4 --verbose` can be
  passed using this params block:

  ```toml
  [updater.params]
  -M = "4,4"
  --verbose = true
  ```


# MapCache Clear (`mapcache-clear`)

Clears a MapCache cache.

```toml
[[updater]]
module = "mapcache-clear"
configfile = "/path/to/mapcache.xml"
tileset = "tileset"

seeder = "/path/to/mapcache_seed"  # Optional

[updater.params]  # Optional
-n = 3
```

* `configfile`

  Location of the MapCache xml configuration file.

* `tileset`

  Name of the tileset to seed.

* `seeder` (Optional)

  Path to the mapcache_seed executable. If not set, the module will use the
  first executable named `mapcache_seed` found on the PATH.

* `[update.params]` (Optional)
 
  Additional parameters to pass to to the seeder. If a parameter has the value
  `true`, it will be passed as a flag to the seeder; otherwise, both the flag
  and its value will be passed.


# MapCache Reseed (`mapcache-reseed`)

Reseeds a MapCache cache.

```toml
[[updater]]
module = "mapcache-reseed"
configfile = "/path/to/mapcache.xml"
tileset = "tileset"

seeder = "/path/to/mapcache_seed"  # Optional

[updater.params]  # Optional
-n = 3
--metasize = "4,4"
```

* `configfile`

  Location of the MapCache xml configuration file.

* `tileset`

  Name of the tileset to seed.

* `seeder` (Optional)

  Path to the mapcache_seed executable. If not set, the module will use the
  first executable named `mapcache_seed` found on the PATH.

* `[update.params]` (Optional)
 
  Additional parameters to pass to to the seeder. If a parameter has the value
  `true`, it will be passed as a flag to the seeder; otherwise, both the flag
  and its value will be passed.
