from mylib.calc import add, subtract, multiply, divide, power, sqrt
from calCLI import cli
from click.testing import CliRunner
import pytest

# define the runner
def runner():
    return CliRunner()


# write a test for each command in calCLI.py
def test_add():
    result = runner().invoke(cli, ["add", "1", "2"])
    assert result.exit_code == 0
    assert result.output == "3.0\n"


def test_divide():
    result = runner().invoke(cli, ["divide", "1", "2"])
    assert result.exit_code == 0
    assert result.output == "0.5\n"


def test_subtract():
    result = runner().invoke(cli, ["subtract", "1", "2"])
    assert result.exit_code == 0
    assert result.output == "-1.0\n"


def test_multiply():
    result = runner().invoke(cli, ["multiply", "1", "2"])
    assert result.exit_code == 0
    assert result.output == "2.0\n"


def test_power():
    result = runner().invoke(cli, ["power", "1", "2"])
    assert result.exit_code == 0
    assert result.output == "1.0\n"


def test_sqrt():
    result = runner().invoke(cli, ["sqrt", "1"])
    assert result.exit_code == 0
    assert result.output == "1.0\n"


def test_add():
    assert add(1, 2) == 3
    assert add(0, 0) == 0
    assert add(-1, -1) == -2
    assert add(1.5, 1.5) == 3.0


def test_subtract():
    assert subtract(1, 2) == -1
    assert subtract(0, 0) == 0
    assert subtract(-1, -1) == 0
    assert subtract(1.5, 1.5) == 0


def test_multiply():
    assert multiply(1, 2) == 2
    assert multiply(0, 0) == 0
    assert multiply(-1, -1) == 1
    assert multiply(1.5, 1.5) == 2.25


def test_divide():
    assert divide(1, 2) == 0.5
    assert divide(-1, -1) == 1
    assert divide(1.5, 1.5) == 1.0


def test_power():
    assert power(1, 2) == 1
    assert power(0, 0) == 1
    assert power(-1, -1) == -1
    assert power(1.5, 1.5) == 1.8371173070873836


def test_sqrt():
    assert sqrt(1) == 1
    assert sqrt(0) == 0
    assert sqrt(1.5) == 1.224744871391589
