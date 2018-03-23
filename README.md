# K.I.S.S. (keep it simple static)

This is a simply static site tool build on Jinja2.

- `project/templates` - Add templates to ignore to `.kiss.yml` file
- `project/data` - `YAML` files that hold data. Must match template name
- `project/build` - Rendered templates folder

## Config

Reads `.kiss.yml` from project directory.

```yaml
# Templates to ignore on render
site_name: mysite
ignore:
    - base.html
```


## CLI

```bash
$ kiss
Usage: kiss [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  config  Print config details
  new     creates new project
  render  Renders project files
  
$ kiss new --help
Usage: kiss new [OPTIONS] PROJECT_NAME

  creates new project

Options:
  --help  Show this message and exit.
  
$ kiss render --help
Usage: kiss render [OPTIONS]

  Renders project files

Options:
  -t, --template TEXT  Template(s) to render
  --help               Show this message and exit.
```

## TODO
- Handle "static" files
- AWS deployment
- Tests
