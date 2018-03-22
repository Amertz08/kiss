import os
import click
import yaml

from jinja2 import Environment, FileSystemLoader, select_autoescape

PROJ_DIR = os.getcwd()
TEMPLATE_DIR = os.path.join(os.getcwd(), 'templates')
BUILD_DIR = os.path.join(PROJ_DIR, 'build')
env = Environment(
    loader=FileSystemLoader(TEMPLATE_DIR),
    autoescape=select_autoescape(['html'])
)


@click.group()
@click.pass_context
def cli(ctx):
    # Set defaults
    ctx.obj = {}
    ctx.obj['IGNORE'] = {}

    config = os.path.join(PROJ_DIR, '.kiss.yml')
    if os.path.exists(config):
        with open(config, 'r') as conf:
            data = yaml.load(conf)
        if 'ignore' in data:
            if isinstance(data['ignore'], str):
                ctx.obj['IGNORE'] = [data['ignore']]
            else:
                ctx.obj['IGNORE'] = data['ignore']


@cli.command(help='creates new project')
@click.argument('project_name')
def new(project_name):
    if not os.path.exists(project_name):
        os.makedirs(project_name)
        os.makedirs(project_name + '/templates')
        os.makedirs(project_name + '/data')
        os.makedirs(project_name + '/build')
    else:
        click.echo('Project already exists')


@cli.command(help='Renders project files')
@click.pass_context
def render(ctx):
    files = None
    try:
        files = os.listdir(TEMPLATE_DIR)
    except FileNotFoundError:
        print(f'{TEMPLATE_DIR} does not exist')
        exit(1)

    if not files:
        print('No templates were found')
        exit(0)

    for f in files:
        if f not in ctx.obj['IGNORE']:
            template = env.get_template(f)
            data_file_name = f.replace('.html', '.yml')
            full_data = os.path.join('data', data_file_name)
            data = {}
            if os.path.exists(full_data):
                with open(full_data, 'r') as dfile:
                    data = yaml.load(dfile)
            rendered_template = template.render(**data)
            with open(os.path.join(BUILD_DIR, f), 'w') as output:
                output.write(rendered_template)


if __name__ == '__main__':
    cli()
