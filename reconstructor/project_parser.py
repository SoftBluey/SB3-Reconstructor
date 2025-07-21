import json

def get_asset_filenames(project_json_path):
    asset_filenames = set()
    with open(project_json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    def collect_assets(target):
        if 'costumes' in target:
            for costume in target['costumes']:
                asset_filenames.add(costume['md5ext'])
        if 'sounds' in target:
            for sound in target['sounds']:
                asset_filenames.add(sound['md5ext'])

    if 'targets' in data:
        for target in data['targets']:
            collect_assets(target)

    return list(asset_filenames)