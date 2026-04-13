#!/usr/bin/env python3
"""Download RJ Heating photos directly to final asset names."""
import urllib.request
import os

assets_dir = '/Users/edwardabramov/Documents/Antigravity/Dambl/projects/website-building-agency/clients/rj-heating-cooling-cleveland/assets/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
    'Referer': 'https://www.rjheating.com/'
}

downloads = [
    # hero: suburban house exterior (house-rotator.jpg)
    ('https://storage.googleapis.com/sos-websvc/uploads/0030062DEA003060/images/house-rotator.jpg', 'hero.jpg'),
    # about: actual RJ Heating storefront (rj-heat-cool-storefront.jpg)
    ('https://storage.googleapis.com/sos-websvc/uploads/0030062DEA003060/images/rj-heat-cool-storefront.jpg', 'about.jpg'),
    # service-1: Bryant AC unit installed outdoors (real job photo)
    ('https://storage.googleapis.com/sos-websvc/uploads/0030062DEA003060/images/gallery/0527151141.jpg', 'service-1.jpg'),
    # service-2: second Bryant AC install (real job photo)
    ('https://storage.googleapis.com/sos-websvc/uploads/0030062DEA003060/images/gallery/0618151558.jpg', 'service-2.jpg'),
    # service-3: Bryant furnace install (real job photo)
    ('https://storage.googleapis.com/sos-websvc/uploads/0030062DEA003060/images/gallery/Furnace-2.jpg', 'service-3.jpg'),
    # service-4: AC condenser close-up (generic-ac-rotator)
    ('https://storage.googleapis.com/sos-websvc/uploads/0030062DEA003060/images/generic-ac-rotator.jpg', 'service-4.jpg'),
    # logo: RJ Heating 2023 logo
    ('https://storage.googleapis.com/sos-websvc/uploads/0030062DEA003060/images/rj-logo-2023-3.png', 'logo.png'),
]


def download(url, filename):
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            data = r.read()
        path = assets_dir + filename
        with open(path, 'wb') as f:
            f.write(data)
        print(f'OK: {filename} ({len(data):,} bytes)')
        return True
    except Exception as e:
        print(f'FAIL: {filename} — {e}')
        return False


if __name__ == '__main__':
    for url, name in downloads:
        download(url, name)
    print('Done.')
