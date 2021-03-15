# SNTZR

A small tool to help clean up log files.

## Installation

Run:

```bash
pipx install git+https://github.com/kieras/sntzr.git
```

## Usage

Run:

```bash
sntzr --help
```

Sample configuration file:

```yaml
---
ip_regex: '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
ip_prefix: '1.1.1.'
keywords:
  'abc\.com': 'acme.com'
  'www\.com': 'acme.org'
  'zzz\..*\.com': 'acme.edu'
```

## Install from local directory

Clone the repo and execute the command:

```bash
pipx install -e --force .
```
