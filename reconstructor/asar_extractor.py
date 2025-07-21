import os
import asar

def extract_asar(asar_path, output_dir):
    try:
        with open(asar_path, 'rb') as f:
            archive = asar.Archive(f)
            archive.extract(output_dir)
        print(f"Successfully extracted {asar_path} to {output_dir}")
        return True
    except Exception as e:
        print(f"Error extracting {asar_path}: {e}")
        return False