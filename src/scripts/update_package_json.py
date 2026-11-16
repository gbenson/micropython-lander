import json
from pathlib import Path

SCRIPTSDIR = Path(__file__).parent
SRCDIR = SCRIPTSDIR.parent
TOPDIR = SRCDIR.parent
OUTPUT = TOPDIR / "package.json"

def main() -> None:
    targets = [
        str(path.relative_to(SRCDIR))
        for path in sorted((SRCDIR / "lander").glob("**/*.py"))
    ]
    OUTPUT.write_text(
        json.dumps(
            {
                "urls": [
                    [target, f"src/{target}"]
                    for target in targets
                ],
            },
            indent=2,
        )
        .replace('[\n      "', '["')
        .replace(",\n      ", ", ")
        .replace('"\n    ]', '"]')
        + "\n"
    )
