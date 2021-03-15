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
        config = yaml.safe_load(f)
    return config


def process_line(line, config):
    line = sanitize_emails(line, config['email_prefix'])
    line = sanitize_ips(line, config['ip_regex'], config['ip_prefix'])
    line = sanitize_keywords(line, config['keywords'])
    return line


def sanitize_emails(line, email_prefix):
    email_counter = 1
    email_regex = r'[\w\.-]+@[\w\.-]+(?:\.[\w]+)+'
    matches = re.findall(email_regex, line)
    if matches is not None:
        unique_matches = set(matches)
        for email in unique_matches:
            line = line.replace(email, email_prefix + str(email_counter) + '@xyz.com')
            email_counter = email_counter + 1
    return line


def sanitize_ips(line, ip_regex, ip_prefix):
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
