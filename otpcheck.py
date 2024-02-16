#!/usr/bin/env python3

import os
import subprocess
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Scan the password store for entries with or without OTPAuth URLs, excluding specified directories.')
    parser.add_argument('-e', '--exclude', nargs='*', default=['.git'], help='List of directories to exclude. Default is ".git".')
    parser.add_argument('--missing', action='store_true', help='Print entries missing OTPAuth URLs instead of those containing them.')
    return parser.parse_args()

def check_otpauth(entry):
    try:
        result = subprocess.run(['pass', entry], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True, check=True)
        return 'otpauth' in result.stdout
    except subprocess.CalledProcessError:
        print(f"Error processing entry: {entry}")
        return None  # None indicates an error occurred

def main(exclude_dirs, print_missing):
    pass_dir = os.path.expanduser('~/.password-store')
    for root, dirs, files in os.walk(pass_dir):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]  # Exclude specified directories
        for file in files:
            if file.endswith('.gpg'):
                entry_path = os.path.join(root, file)
                entry = os.path.relpath(entry_path, pass_dir)[:-4]  # Removing '.gpg'
                has_otpauth = check_otpauth(entry)
                if has_otpauth is not None:  # Only proceed if there was no error
                    if (has_otpauth and not print_missing) or (not has_otpauth and print_missing):
                        print(f'{"Missing" if print_missing else "Found"} otpauth in {entry}')

if __name__ == '__main__':
    args = parse_args()
    main(args.exclude, args.missing)
