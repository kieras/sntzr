# -*- coding: utf-8 -*-
import binascii
import click
import os
import random
import re
import yaml

from sntzr.__version__ import __version__ as version

global_patterns_values = {}

@click.command()
@click.version_option(version=version)
@click.argument('input_file')
@click.option('--config_file', default='./sntzr.yaml', help='Configuration file.')
def main(input_file, config_file):
    """SNTZR"""
    config = load_config(config_file)
    with open(input_file) as in_file:
        for line in in_file:
            # TODO: felipegc we should call process line only if it is data
            processed_line = process_line(line, config)
            print(processed_line, end='')


def load_config(config_file):
    with open(config_file) as f:
        config = yaml.safe_load(f)
    return config


def process_line(line, config):
    # line = sanitize_ips(line, config['ip_regex'], config['ip_prefix'])
    line = sanitize_global_patterns(line, config['global_patterns'])
    line = sanitize_keywords(line, config['keywords'])
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


def generate_random_hexdecimal(length, is_lower_case):
    random_value = binascii.hexlify(os.urandom(int(length/2)))
    str_value = random_value.decode('utf-8')

    return str_value if is_lower_case else str_value.lower()


def generate_random_value_by_type(random_type, length=0):

    if random_type == 'hex_id' or random_type == 'sha256':
        return generate_random_hexdecimal(length, True)
    elif random_type == 'crazy_name':
        r1 = random.randint(1,15)
        r2 = random.randint(15,30)
        r3 = random.randint(1,30)
        return  'S-{}-{}-{}'.format(r1, r2, r3)
    elif random_type == 'mac_address_no_colon':
        return generate_random_hexdecimal(12, True)
    elif random_type == 'ip':
        r1 = random.randint(1,255)
        return '10.20.30.{}'.format(r1)
    elif random_type == 'guid':
        r1 = generate_random_hexdecimal(8, False)
        r2 = generate_random_hexdecimal(4, False)
        r3 = generate_random_hexdecimal(4, False)
        r4 = generate_random_hexdecimal(4, False)
        r5 = generate_random_hexdecimal(12, False)
        return '{}-{}-{}-{}-{}'.format(r1, r2, r3, r4, r5)
    elif random_type == 'machine_name':
        letters = ['A', 'B', 'C', 'X', 'Y', 'Z']
        r1 = ''.join(random.choice(letters) for i in range(4))
        r2 = random.randint(100000,999999)
        r3 = ''.join(random.choice(letters) for i in range(3))
        return '{}{}-{}'.format(r1, r2, r3)

def build_full_pattern(typeof, value, typeof_placeholder):
    if typeof == 'raw':
        return value
    elif typeof == 'tag_xml':
        return '<{}>{}</{}>'.format(typeof_placeholder, value, typeof_placeholder)


def sanitize_global_patterns(line, global_patterns):
    for item in global_patterns:
        name = item['name']
        regex = item['regex']
        typeof = item['typeof']
        typeof_placeholder =  item['typeof_placeholder']
        activated = item['activated']

        if not activated:
            continue

        full_pattern_regex = build_full_pattern(typeof, regex, typeof_placeholder)

        matches = re.findall(full_pattern_regex, line)

        if len(matches) > 0:
            unique_matches = set(matches)
            for match in unique_matches:
                if match in global_patterns_values:
                    line = re.sub(match, global_patterns_values[match]['str_to_replace'], line)
                else:
                    #length = len(match)
                    # str_value = generate_random_value_by_type(name, length)
                    # we keep the value as the key
                    # global_patterns_values[match] = str_value
                    #str_value_to_be_replaced = build_full_pattern(typeof, str_value, typeof_placeholder)
                    # line = re.sub(match, str_value_to_be_replaced, line)
                    save_pattern(item, match)
                    line = re.sub(match, global_patterns_values[match]['str_to_replace'], line)

    return line

def get_new_value_by_original_value(original_value):
    for item in global_patterns_values.values():
        if item['original_value'] == original_value:
            return item['new_value']

    return None


def save_pattern(global_pattern, key):
    original_value = key

    if global_pattern['typeof'] == 'tag_xml':
        i_tag = '<{}>'.format(global_pattern['typeof_placeholder'])
        e_tag = '</{}>'.format(global_pattern['typeof_placeholder'])
        original_value = key.split(i_tag)[1].split(e_tag)[0]

    new_value = get_new_value_by_original_value(original_value)
    if new_value is None:
        length = len(original_value) # TODO: felipegc stop using length
        new_value = generate_random_value_by_type(global_pattern['name'], length)

    str_value_to_be_replaced = build_full_pattern(global_pattern['typeof'], new_value, global_pattern['typeof_placeholder'])

    global_patterns_values[key] = {
      "original_value": original_value,
      "new_value": new_value,
      "str_to_replace": str_value_to_be_replaced
    }


def sanitize_keywords(line, keywords):
    for pattern, repl in keywords.items():
        line = re.sub(pattern, repl, line)
    return line


if __name__ == "__main__":
    main()
