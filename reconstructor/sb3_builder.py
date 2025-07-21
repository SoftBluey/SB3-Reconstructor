import os
import zipfile
import shutil

def create_sb3(project_json_path, assets_dir, output_path):
    temp_dir = 'temp_sb3_build'
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
        
    shutil.copy(project_json_path, os.path.join(temp_dir, 'project.json'))
    for filename in os.listdir(assets_dir):
        shutil.copy(os.path.join(assets_dir, filename), os.path.join(temp_dir, filename))

    with zipfile.ZipFile(output_path, 'w') as zipf:
        for root, _, files in os.walk(temp_dir):
            for file in files:
                zipf.write(os.path.join(root, file), file)

    shutil.rmtree(temp_dir)
    print(f"Successfully created {output_path}")