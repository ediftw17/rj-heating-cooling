import shutil
import os

base = '/Users/edwardabramov/Documents/Antigravity/Dambl/projects/website-building-agency/clients/rj-heating-cooling-cleveland/assets/'

copies = [
    ('hero-candidate-2.jpg', 'hero.jpg'),
    ('about-candidate.jpg', 'about.jpg'),
    ('service-candidate-1.jpg', 'service-1.jpg'),
    ('service-candidate-2.jpg', 'service-2.jpg'),
    ('service-candidate-3.jpg', 'service-3.jpg'),
    ('hero-candidate-3.jpg', 'service-4.jpg'),
]

for src, dst in copies:
    shutil.copy2(base + src, base + dst)
    size = os.path.getsize(base + dst)
    print(f"OK: {dst} ({size} bytes)")

print("Done.")
