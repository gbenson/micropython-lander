# micropython-lander

MicroPython port of [Lander](https://lander.bbcelite.com/),
David Braben's epic game for the Acorn Archimedes.

![Screenshot of Lander on the Acorn Archimedes](assets/archimedes-lander.png)


## Installation

### Badgeware

Copy `src/lander` into the badge's `apps` folder.

### Pimoroni Presto

```sh
mpremote mip install --target / github:gbenson/micropython-lander/ports/presto
```

## Development

```sh
git clone https://github.com/gbenson/micropython-lander.git
cd micropython-lander
python3 -m venv .venv
. .venv/bin/activate
pip install --upgrade pip
pip install -e .
```
