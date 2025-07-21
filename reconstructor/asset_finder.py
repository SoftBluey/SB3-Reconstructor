import os
import shutil

def find_and_copy_assets(asset_filenames, source_dir, dest_dir):
    found_assets = []
    missing_assets = []
    
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for root, _, files in os.walk(source_dir):
        for filename in files:
            if filename in asset_filenames:
                source_path = os.path.join(root, filename)
                dest_path = os.path.join(dest_dir, filename)
                shutil.copy2(source_path, dest_path)
                found_assets.append(filename)

    missing_assets = list(set(asset_filenames) - set(found_assets))
    
    return found_assets, missing_assets