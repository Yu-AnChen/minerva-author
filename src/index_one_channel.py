from app import (
    make_subgroups, Opener
)
import json
import sys

def from_json(img_path, fname, idx):
    with open(fname, "r") as fh:
        data = json.load(fh)
        opener = Opener(img_path)
        single_channel_groups = make_subgroups(
            data['groups'], opener.rgba
        )
        group = single_channel_groups[idx]
        data['defaults'] = group['render']
        data['groups'] = [group]
        data['waypoints'] = []
        if 'autosave' in data:
            del data['autosave']
        return data

if __name__ == "__main__":
    img_path = sys.argv[1]
    fname = sys.argv[2]
    idx = sys.argv[3]
    idx_channel_group = from_json(img_path, fname, idx)
    print(json.dumps(idx_channel_group))
