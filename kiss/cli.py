import os
import shutil

import click
import yaml

from config import Config, TEMPLATE_DIR, BUILD_DIR, DATA_DIR
from decorators import config_required

LOC = os.path.dirname(os.path.abspath(__file__))


@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = Config()


@cli.command(help='Print config details')
@click.pass_context
@config_required
def config(ctx):
    click.echo(ctx.obj)


@cli.command(help='creates new project')
@click.argument('project_name')
def new(project_name):
    if not os.path.exists(project_name):
        base = os.path.join(os.getcwd(), project_name)
        src_base = os.path.join(LOC, 'skeletons')

        # Create directories
        os.makedirs(base)
        os.makedirs(os.path.join(base, TEMPLATE_DIR))
        os.makedirs(os.path.join(base, DATA_DIR))
        os.makedirs(os.path.join(base, BUILD_DIR))

        # Copy basic config file
        conf_file = os.path.join(base, '.kiss.yml')
        src_conf = os.path.join(src_base, '.kiss.yml')
        shutil.copy(src_conf, conf_file)
        click.echo(f'{project_name} created')
    else:
        click.echo('Project already exists')


@cli.command(help='Renders project files')
@click.pass_context
@config_required
def render(ctx):
    files = None
    try:
        files = os.listdir(ctx.obj['TEMPLATE_DIR'])
    except FileNotFoundError:
        click.echo(f'{ctx.obj["TEMPLATE_DIR"]} does not exist')
        exit(1)

    if not files:
        click.echo('No templates were found')
        exit(0)

    for f in files:
        if f not in ctx.obj['IGNORE']:
            data_file_name = f.replace('.html', '.yml')
            full_data = os.path.join('data', data_file_name)
            data = {}
            if os.path.exists(full_data):
                with open(full_data, 'r') as dfile:
                    data = yaml.load(dfile)
            rendered_template = ctx.obj.render(f, **data)
            with open(os.path.join(ctx.obj['BUILD_DIR'], f), 'w') as output:
                output.write(rendered_template)


if __name__ == '__main__':
    cli()
