# -*- coding: utf-8 -*-
import click
import re
import yaml

from sntzr.__version__ import __version__ as version

@click.command()
@click.version_option(version=version)
@click.argument('input_file')
@click.option('--config_file', default='./sntzr.yaml', help='Configuration file.')
def main(input_file, config_file):
    """SNTZR"""
    config = load_config(config_file)
    with open(input_file) as in_file:
        for line in in_file:
            processed_line = process_line(line, config)
            print(processed_line, end='')


def load_config(config_file):
    with open(config_file) as f:
        config = yaml.load(f)
    return config


def process_line(line, config):
    if config['sanitize_ip']:
        line = sanitize_ip(line)
    line = sanitize_keywords(line, config['keywords'])
    return line


def sanitize_ip(line):
    ip_regex = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    ip_prefix = '1.2.3.'
    ip_counter = 1
    matches = re.findall(ip_regex, line)
    if matches is not None:
        unique_matches = set(matches)
        for ip in unique_matches:
            line = line.replace(ip, ip_prefix + str(ip_counter))
            ip_counter = ip_counter + 1
    return line


def sanitize_keywords(line, keywords):
    for pattern, repl in keywords.items():
        line = re.sub(pattern, repl, line)
    return line


if __name__ == "__main__":
    main()
