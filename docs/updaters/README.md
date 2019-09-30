# Updater modules

Each updater block in the configuration file drives an updater module. The
updaters are executed one after the other in the order they are listed in the
configuration file.

Each updater module can be appear multiple times in the configuration file.


# Documentation on specific modules

* [SMAC-M](./SMAC-M.md)


# Documentation format

Each updater is documented in the following format. The `module-name` is the
value to enter in the block's `module` parameter to use this module. Unknown
module names in the configuration file are an error.

## Updater name (`module-name`)

Description of the updater.

```toml
# Example block with dummy values
[[updater]]
module = "module-name"
arg1 = "Value 1"
arg2 = "Value 2"
# ...
```

* `arg1`

  Description of the first argument

* `arg2`

  Description of the second argument
