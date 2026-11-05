#!/usr/bin/env python3
"""Assemble the class Drive ZIP from the approved private kit and the public teaching fork."""
import argparse
import hashlib
import json
import shutil
import tempfile
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

REPO = Path(__file__).resolve().parents[1]
APPROVED_KIT_SHA256 = '463199e8ae302f3c1588c7dac19049d287955e6e7a6a0e0280f88f58e334272a'

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def package(kit, output):
    if digest(kit) != APPROVED_KIT_SHA256:
        raise ValueError('Expected the original ACP Second Brain 0.1.0-alpha.1 distribution ZIP')
    with tempfile.TemporaryDirectory() as stage:
        root = Path(stage) / 'Small Worlds Workshop'
        brain = root / 'Brain'
        with ZipFile(kit) as archive:
            archive.extractall(brain)
        for name in ('Creative', 'Studio', 'Skills'):
            shutil.copytree(REPO / 'classroom' / name, root / name,
                            ignore=shutil.ignore_patterns('.DS_Store', '.godot', '.gradle', 'build', 'local.properties', '__pycache__'))
        shutil.copytree(brain / 'examples/local-gallery', root / 'Studio/local-gallery')
        for template in ('project-memory', 'job-contract', 'completion-receipt'):
            shutil.copy2(brain / 'templates' / (template + '.md'), root / 'Studio')
        shutil.copy2(REPO / 'classroom/start-here.html', root / 'Start Here.html')
        slides = root / 'Slides'
        slides.mkdir()
        for folder in ('images', 'media', 'slides'):
            shutil.copytree(REPO / folder, slides / folder, ignore=shutil.ignore_patterns('.DS_Store'))
        for path in REPO.glob('favicon*'):
            shutil.copy2(path, slides / path.name)
        shutil.copy2(REPO / 'apple-touch-icon.png', slides)
        deck = (REPO / 'index.html').read_text().replace('classroom/start-here.html', '../Start%20Here.html')
        (slides / 'index.html').write_text(deck)
        manifest = {'course': 'Creative AI Workflow Masterclass, Part 1', 'date': '2026-11-05',
                    'start': 'Start Here.html', 'kit_zip_sha256': APPROVED_KIT_SHA256,
                    'files': {p.relative_to(root).as_posix(): digest(p) for p in sorted(root.rglob('*')) if p.is_file()}}
        (root / 'Workshop manifest.json').write_text(json.dumps(manifest, indent=2)+'\n')
        with ZipFile(output, 'x', ZIP_DEFLATED) as archive:
            for path in sorted(root.rglob('*')):
                if path.is_file():
                    archive.write(path, path.relative_to(root.parent))
    print(output)

if __name__ == '__main__':
    args = argparse.ArgumentParser(description=__doc__)
    args.add_argument('kit', type=Path)
    args.add_argument('output', type=Path)
    options = args.parse_args()
    package(options.kit, options.output)
