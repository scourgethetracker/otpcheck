# Password Store OTPAuth Scanner

This script is designed to scan a password store (managed by the Unix `pass` password manager) for entries containing or missing OTPAuth URLs. It's particularly useful for managing two-factor authentication setups by identifying which entries are configured for one-time passwords.

## Features

- **Scan for OTPAuth URLs**: By default, the script scans all entries in the password store and prints those containing OTPAuth URLs.
- **Exclude Directories**: Users can exclude specific directories from the scan to focus on relevant entries.
- **Missing OTPAuth Option**: With the `--missing` flag, the script inverses its behavior to print entries that do not contain OTPAuth URLs, helping users identify accounts that might need two-factor authentication setup.

## Prerequisites

To use this script, you need to have the `pass` Unix password manager installed and set up on your system. The script assumes that your password store is located in the default location (`~/.password-store`).

## Usage

```bash
./otpauth_scanner.py [-e EXCLUDE [EXCLUDE ...]] [--missing]
```

### Options

- `-e`, `--exclude`: Specify directories to exclude from the scan. Multiple directories can be excluded by listing them after the flag. Default is to exclude the `.git` directory.

  Example:
  ```bash
  ./otpauth_scanner.py -e dir1 dir2
  ```

- `--missing`: Print entries that are missing OTPAuth URLs instead of those containing them.

  Example:
  ```bash
  ./otpauth_scanner.py --missing
  ```

## Example Commands

- Scan all entries excluding the `.git` and `archive` directories:
  ```bash
  ./otpauth_scanner.py -e .git archive
  ```

- Scan for entries missing OTPAuth URLs, excluding the `temp` directory:
  ```bash
  ./otpauth_scanner.py --missing -e temp
  ```

## Error Handling

If the script encounters an error while processing an entry (e.g., permission issues, corrupted files), it prints an error message for that entry and continues with the next one.

## License

This script is provided "as is", without warranty of any kind. Use it at your own risk.
