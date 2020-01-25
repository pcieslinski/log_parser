import argparse


parser = argparse.ArgumentParser(
    prog='log-parser',
    description='A CLI tool for parsing logs.'
                ' Contains an utility stats for generating statistics based on server logs.'
)

parser.add_argument('file',
                    type=argparse.FileType('r'),
                    help='Path to log file.')


stats = parser.add_argument_group(
    title='stats',
    description='Generates useful statistics and metrics based on the server log.'
)

stats.add_argument('--since',
                   type=str,
                   help='The date that marks the start of statistics generation.')

stats.add_argument('--until',
                   type=str,
                   help='The date that marks the end of statistics generation.')
