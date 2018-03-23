import pytest
from click.testing import CliRunner

from kiss.cli import cli


@pytest.fixture
def runner():
    return CliRunner()


def test_config_print_no_file(runner):
    result = runner.invoke(cli, ['config'])
    assert result.exit_code == 0, f'Invalid exit code: {result.exit_code}'
    assert result.output == 'Missing .kiss.yml or not in a project directory\n'
