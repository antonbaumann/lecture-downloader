import argparse
import os


# check if output file already exists
# if not check if dir does already exist
def validate_output_file(p, filepath) -> str:
    abspath = os.path.abspath(filepath)
    dirname = os.path.dirname(abspath)
    if os.path.isfile(abspath):
        p.error(f'The file {filepath} does already exist.')
    elif not os.path.exists(dirname):
        p.error(f'The directory {dirname} does not exist.')
    else:
        return filepath


def arguments():
    parser = argparse.ArgumentParser(description="Download lectures")
    parser.add_argument(
        '-u',
        dest='url',
        required=True,
        help='stream playlist url',
        metavar='URL',
        type=str
    )
    parser.add_argument(
        '-o',
        dest='output_file',
        required=True,
        help='output file name',
        metavar='OUT_FILE',
        type=lambda x: validate_output_file(parser, x),
    )
    return parser.parse_args()
