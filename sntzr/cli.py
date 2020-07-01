# -*- coding: utf-8 -*-
import click

from sntzr.__version__ import __version__ as version

@click.command()
@click.version_option(version=version)
def main():
    """SNTZR"""
    print("I'm a SNTZR! ✨")

if __name__ == "__main__":
    main()
