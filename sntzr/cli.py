# -*- coding: utf-8 -*-
import click
import re
import yaml
from sntzr.__version__ import __version__ as version
from sntzr import replacers_fn

global_patterns_values = {}
all_config = None

@click.command()
@click.version_option(version=version)
@click.argument('input_file')
@click.option('--config_file', default='./sntzr.yaml', help='Configuration file.')
def main(input_file, config_file):
    """SNTZR"""
    global all_config
    all_config = load_config(config_file)
    with open(input_file) as in_file:
        for line in in_file:
            is_data_line = line.find('data:') > -1
            if is_data_line:
                processed_line = process_line(line)
                print(processed_line, end='')
            else:
                print(line, end='')



def load_config(config_file):
    with open(config_file) as f:
        config = yaml.safe_load(f)
    return config


def process_line(line):
    line = sanitize_patterns(line)
    return line


def validate_and_normalize_item(item):
    """
    Validate if there is any mandatory field missing such as pattern, replace.
    If non mandatory fields are missing, they are normalized to default values.
    """

    if 'pattern' not in item.keys():
        raise Exception('The pattern field is missing for item -> {}'.format(item))
    elif 'replace' not in item.keys():
        raise Exception('The pattern field is missing for item -> {}'.format(item))

    if 'data' not in item.keys():
        item['data'] = 'raw'

    if 'field' not in item.keys():
        item['field'] = '-'

    if 'activated' not in item.keys():
        item['activated'] = True


# Utils to manipulate global_pattern
def build_full_pattern(global_pattern, value, to_record=False):
    """
    Builds the pattern by merging the data type and field with the value dependig on the data.
    Ex: if the data is xml and the field is Name the return will be <Name>value</Name>.
    """

    data = global_pattern['data']
    field =  global_pattern['field']

    if data == 'raw':
        return value
    elif data == 'xml':
        return '<{}>{}</{}>'.format(field, value, field)
    elif data == 'kv':
        return '{}={}'.format(field, value)
    elif data == 'json':
        raw_field = '\\"{}\\"'.format(field) if to_record else '\\\\"{}\\\\"'.format(field)
        full_pattern = '{}:{}'.format(raw_field, value)
        return full_pattern


def extract_value(global_pattern, key):
    """
    Extracts the value from the key by removing tags, fields or something else it may have.
    Ex: If the value is <Name>Jhon Dow</Name>, it will return 'Jonh Dow'.
    """

    original_value = key

    if global_pattern['data'] == 'xml':
        i_tag = '<{}>'.format(global_pattern['field'])
        e_tag = '</{}>'.format(global_pattern['field'])
        original_value = key.split(i_tag)[1].split(e_tag)[0]
    elif global_pattern['data'] == 'kv':
        kv = '{}='.format(global_pattern['field'])
        original_value = key.split(kv)[1]
    elif global_pattern['data'] == 'json':
        full_pattern = '\\\\"{}\\\\":({})'.format(global_pattern['field'], get_regex_pattern(global_pattern['pattern']))
        original_value = re.search(full_pattern, key).group(1)

    return original_value


# Utils to manipulate global_patterns_values
def get_new_value_by_original_value(original_value):
    """
    Iterates over the patterns already saved in memory to find the new generated value for an original value.
    """

    for item in global_patterns_values.values():
        if item['original_value'] == original_value:
            return item['new_value']

    return None


def add_global_pattern_value(global_pattern, key):
    """
    Generates an object containing the original value, new value and the full pattern
    to be replaced and saves it in memory to be re-used when necessary.
    """

    original_value = extract_value(global_pattern, key)

    new_value = get_new_value_by_original_value(original_value)

    if new_value is None:
        length = len(original_value)
        new_value = generate_new_value(global_pattern, length)

    str_value_to_be_replaced = build_full_pattern(global_pattern, new_value, True)

    global_patterns_values[key] = {
      'original_value': original_value,
      'new_value': new_value,
      'str_to_replace': str_value_to_be_replaced
    }


def get_regex_pattern(pattern):
    """
    Tries to find the pattern in according to the key 'gr://' and returns its value otherwise
    the pattern itself is returned.
    """

    global_regex = all_config['global_regex']

    if pattern.startswith('gr://'):
        return global_regex[pattern]
    else:
        return pattern


def sanitize_patterns(line):
    """
    Iterates over the patterns in order to find them in the file and replace them by their custom value.
    It preserves the found values in memory so it always replace the same patterns by the same values.
    """

    global_patterns = all_config['patterns']

    for item in global_patterns:
        validate_and_normalize_item(item)
        activated = item['activated']

        if not activated:
            continue

        #item['pattern'] = get_regex_pattern(item['pattern'])
        pattern = get_regex_pattern(item['pattern'])

        full_pattern_regex = build_full_pattern(item, pattern)
        matches = re.findall(full_pattern_regex, line)

        if len(matches) > 0:
            unique_keys = set(matches)
            for key in unique_keys:
                if key not in global_patterns_values:
                    add_global_pattern_value(item, key)

                line = line.replace(key, global_patterns_values[key]['str_to_replace'])
                line = line.replace(global_patterns_values[key]['original_value'], global_patterns_values[key]['new_value'])

    return line


def generate_new_value(global_pattern, length=0):
    """
    Generates the value according to the replace function or value defined.
    If the function is not found it uses the raw string istead.
    """

    replace = global_pattern['replace']

    if hasattr(replacers_fn, replace):
        replace = getattr(replacers_fn, replace)(length)

    if global_pattern['pattern'] == 'gr://json_string_value':
        replace = '\\"{}\\"'.format(replace)

    return replace


if __name__ == "__main__":
    main()
