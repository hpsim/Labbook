"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -mlabbook` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``labbook.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``labbook.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
import click
import yaml
import logging

import init as labbook_init
import build as labbook_build
import freeze
import create_cases as labbook_create


def init_logger():
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger()

    config_file = "labbook.yml"

    with open(config_file, "r") as config_handle:
        config = yaml.safe_load(config_handle)

    return logger, config


@click.group()
@click.option("--debug/--no-debug", default=False)
@click.pass_context
def cli(ctx, debug):
    # ensure that ctx.obj exists and is a dict (in case `cli()` is called
    # by means other than the `if` block below)
    ctx.ensure_object(dict)
    ctx.obj["DEBUG"] = debug


@cli.command()
@click.option("--template", default="OpenFOAM")
@click.option("--base", default="base")
@click.option("--extra_build_flags", default="")
@click.pass_context
def init(ctx, **kwargs):
    logger, config = init_logger()

    labbook_init.init_labbook(kwargs, config, logger)


@cli.command()
@click.pass_context
def rebase(ctx, **kwargs):
    print("rebase", kwargs)


@cli.command()
@click.option("--select", default="")
@click.option("--extra_build_flags", default="")
@click.pass_context
def build(ctx, **kwargs):
    logger, config = init_logger()
    labbook_build.labbook_build(kwargs, config, logger)


@cli.command()
@click.option("--case", default="")
@click.option("--select", default="")
@click.pass_context
def create_cases(ctx, **kwargs):
    logger, config = init_logger()
    labbook_create.create_cases(kwargs, config, logger)


@cli.command()
@click.option("--pipeline", default=None)
@click.option("--case", default=None)
@click.pass_context
def execute(ctx, **kwargs):
    import pipeline

    logger, config = init_logger()
    pipeline.execute(kwargs, config, logger)


@cli.command()
@click.option("--message", default=None)
@click.pass_context
def freeze(ctx, **kwargs):
    logger, config = init_logger()
    freeze.freeze(kwargs, config, logger)


@cli.command()
@click.option("--name", default=None)
@click.option("--dependencies", default=False)
@click.pass_context
def sync(ctx, **kwargs):
    import update

    logger, config = init_logger()
    if kwargs.get("dependencies"):
        update.dependencies(kwargs, config, logger)


@cli.command()
@click.option(
    "-e", "--enviroment", default=None, help="Check if env vars in labbook are set"
)
@click.pass_context
def validate(ctx, **kwargs):
    import validate

    logger, config = init_logger()
    validate.validate_env(kwargs, config, logger)


@cli.command()
@click.pass_context
def log(ctx, **kwargs):
    import validate

    logger, config = init_logger()
    validate.validate_env(kwargs, config, logger)


@cli.command()
@click.pass_context
def update(ctx, **kwargs):
    import update

    logger, config = init_logger()
    update.dependencies(kwargs, config, logger)


def main():
    cli(obj={})


if __name__ == "__main__":
    cli(obj={})
