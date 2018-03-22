import os
import click
import yaml

from config import Config, TEMPLATE_DIR, BUILD_DIR, DATA_DIR
from decorators import config_required


@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = Config()


@cli.command(help='Print config details')
@click.pass_context
@config_required
def config(ctx):
    print(ctx.obj)


@cli.command(help='creates new project')
@click.argument('project_name')
def new(project_name):
    if not os.path.exists(project_name):
        base = os.path.join(os.getcwd(), project_name)
        os.makedirs(base)
        os.makedirs(os.path.join(base, TEMPLATE_DIR))
        os.makedirs(os.path.join(base, DATA_DIR))
        os.makedirs(os.path.join(base, BUILD_DIR))
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
        print(f'{ctx.obj["TEMPLATE_DIR"]} does not exist')
        exit(1)

    if not files:
        print('No templates were found')
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
