from app import (
    make_subgroups, Opener
)
import json
import sys

def from_json(img_path, fname):
    with open(fname, "r") as fh:
        data = json.load(fh)
        opener = Opener(img_path)
        single_channel_groups = make_subgroups(
            data['groups'], opener.rgba
        )
        return len(single_channel_groups)

if __name__ == "__main__":
    img_path = sys.argv[1]
    fname = sys.argv[1]
    count  = from_json(img_path, fname)
    print(int(count))
