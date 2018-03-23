import os
import shutil

import click
import yaml

from jinja2.exceptions import TemplateNotFound

from .config import Config, TEMPLATE_DIR, BUILD_DIR, DATA_DIR
from .decorators import config_required

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
        with open(conf_file, 'a') as f:
            f.write(yaml.dump({'site_name': project_name}, default_flow_style=False))
            f.write(yaml.dump({'ignore': ['base.html']}, default_flow_style=False))

        # Copy basic html file
        html = os.path.join(base, TEMPLATE_DIR, 'base.html')
        src_html = os.path.join(src_base, 'base.html')
        shutil.copy(src_html, html)

        click.echo(f'{project_name} created')
    else:
        click.echo('Project already exists')


@cli.command(help='Renders project files')
@click.option('-t', '--template', multiple=True, help='Template(s) to render')
@click.pass_context
@config_required
def render(ctx, template):
    files = None
    if template:
        files = [f'{t}.html' for t in template]
    else:
        try:
            files = os.listdir(ctx.obj['TEMPLATE_DIR'])
        except FileNotFoundError:
            click.echo(f'{ctx.obj["TEMPLATE_DIR"]} does not exist')
            exit(1)

        if not files:
            click.echo('No templates were found')
            exit(0)

    try:
        ctx.obj.render_files(files)
    except TemplateNotFound as e:
        print(f'Template not found: {e.message}')
        exit(1)
