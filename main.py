import argparse
import os
import tempfile
from reconstructor.asar_extractor import extract_asar
from reconstructor.project_parser import get_asset_filenames
from reconstructor.asset_finder import find_and_copy_assets
from reconstructor.sb3_builder import create_sb3

def main():
    parser = argparse.ArgumentParser(description="Reconstruct .sb3 files from Electron-packaged TurboWarp projects.")
    parser.add_argument("input_path", help="Path to the Electron application's .asar file or the directory containing the extracted files.")
    parser.add_argument("output_sb3", help="Path to save the reconstructed .sb3 file.")
    
    args = parser.parse_args()

    with tempfile.TemporaryDirectory() as temp_dir:
        source_dir = args.input_path
        if args.input_path.lower().endswith('.asar'):
            print("Detected .asar file, extracting...")
            extract_asar(args.input_path, temp_dir)
            source_dir = temp_dir
        
        project_json_path = os.path.join(source_dir, 'project.json')
        if not os.path.exists(project_json_path):
            for root, _, files in os.walk(source_dir):
                if 'project.json' in files:
                    project_json_path = os.path.join(root, 'project.json')
                    break
            
            if not os.path.exists(project_json_path):
                print("Error: Could not find project.json in the provided path.")
                return

        print(f"Found project.json at: {project_json_path}")
        
        asset_filenames = get_asset_filenames(project_json_path)
        print(f"Found {len(asset_filenames)} asset references in project.json")
        
        assets_build_dir = os.path.join(temp_dir, 'assets_for_sb3')
        found, missing = find_and_copy_assets(asset_filenames, source_dir, assets_build_dir)
        
        print(f"Found {len(found)} assets.")
        if missing:
            print(f"Warning: {len(missing)} assets are missing: {', '.join(missing)}")
            
        create_sb3(project_json_path, assets_build_dir, args.output_sb3)

if __name__ == "__main__":
    main()