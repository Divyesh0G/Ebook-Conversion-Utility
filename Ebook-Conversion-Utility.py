from os import listdir, rename
from os.path import isfile, join
import subprocess

# Return the name of the file to be kept after conversion by changing the extension to .azw3
def get_final_filename(f):
    f = f.split(".")
    filename = ".".join(f[0:-1])
    processed_file_name = filename + ".azw3"
    return processed_file_name

# Return the file extension (pdf, epub, mobi)
def get_file_extension(f):
    return f.split(".")[-1]

# List of extensions to be ignored
ignored_extensions = ["pdf"]

# Path where the downloaded files are stored
mypath = "C:/Users/c/Downloads/ebooks/"

# Path where the converted files will be stored
mypath_converted = "C:/Users/c/Downloads/ebooks/kindle/"

# Path where processed files will be moved to, clearing the downloaded folder
mypath_processed = "C:/Users/c/Downloads/ebooks/processed/"

# Get a list of raw files and converted files
raw_files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
converted_files = [f for f in listdir(mypath_converted) if isfile(join(mypath_converted, f))]

# Iterate through the raw files
for f in raw_files:
    final_file_name = get_final_filename(f)
    extension = get_file_extension(f)
    if final_file_name not in converted_files and extension not in ignored_extensions:
        print("Converting: " + f)
        try:
            subprocess.call(["ebook-convert", join(mypath, f), join(mypath_converted, final_file_name)])
            rename(join(mypath, f), join(mypath_processed, f))
            print("Conversion successful")
        except Exception as e:
            print("Conversion failed:", str(e))
    else:
        print("Already converted or ignored: " + final_file_name)
