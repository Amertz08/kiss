import os
import click


@click.group()
def cli():
    pass


@cli.command(help='creates new project')
@click.argument('project_name')
def new(project_name):
    if not os.path.exists(project_name):
        os.makedirs(project_name)
    else:
        click.echo('Project already exists')


if __name__ == '__main__':
    cli()
