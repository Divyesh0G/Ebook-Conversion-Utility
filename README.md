# Ebook Conversion Utility

This script automates the process of converting ebooks to the AZW3 format, compatible with Kindle devices.

## Usage

1. Install the required packages by running `pip install -r requirements.txt`.
2. Update the `mypath` variable with the path to the directory where your raw ebook files are located.
3. Update the `mypath_converted` variable with the path to the directory where you want the converted files to be saved.
4. Update the `mypath_processed` variable with the path to the directory where you want the processed files to be moved after conversion.
5. Run the script by executing `python convert_ebooks.py`.

The script will scan the specified directory for raw ebook files (PDF, EPUB, MOBI) and convert them to the AZW3 format using the `ebook-convert` command-line tool from Calibre. The converted files will be saved to the specified `mypath_converted` directory, and the processed files will be moved to the `mypath_processed` directory for cleanup.

Make sure to have Calibre installed and the `ebook-convert` command accessible from the command line.

Feel free to customize the script as per your requirements and contribute to the project by submitting pull requests.
