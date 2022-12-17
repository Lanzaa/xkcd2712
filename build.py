


import json
from os.path import exists

import requests


# Grab tiles

XKCD_URL = "https://xkcd.com/2712/tile/{planet}_{x}_{y}.png"
LOCAL_PATH = "tile/{planet}_{x}_{y}.png"

def image_paths(planet, x, y):
    local = LOCAL_PATH.format(planet=planet, x=x, y=y)
    remote = XKCD_URL.format(planet=planet, x=x, y=y)
    return local, remote

def grab(planet, width, height, cache_bust=False):
    for x in range(width):
        for y in range(height):
            lp, rp = image_paths(planet, x, y)
            if cache_bust or exists(lp):
                #print(f"Image exist {lp}")
                pass
            else:
                print(f"Downloading {lp}")
                download(rp, lp)
    print(f"Done with {planet}")

def download(remote_url, local_path):
    req = requests.get(remote_url)
    with open(local_path, "wb") as f:
        f.write(req.content)
    return


def load_locations():
    with open("data.json") as f:
        return json.load(f)["locations"]

def get_bounds(loc):
    return loc["width"]//1024, loc["height"]//1024

print("Locations:")
locations = load_locations()
for k, loc in locations.items():
    bounds = get_bounds(loc)
    print(k, " bounds ", bounds)
    #grab(k, *bounds)

