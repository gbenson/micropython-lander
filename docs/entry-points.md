# Entry points

## Badgeware

Installation is entering disk mode and copying `src/lander` into the
`apps` folder.  MicroPython will see this as `/system/apps/lander`.

On badge startup, the existence of `/system/apps/lander/__init__.py`
or `.mpy` makes the launcher include a "Lander" application in its
menu, with `/system/apps/lander/icon.png` as its icon if present.
Note that the loader's doesn't seem to support all PNG modes, though
24×24 RGBA seems to work.

To launch Lander the system will:

```python
os.chdir("/system/apps/lander")
sys.path.insert(0, "/system/apps/lander")
__import__("/system/apps/lander")
```

## Pimoroni Presto

Installation is via `mpremote mip`.  `src/lander` is installed in
`/lander`, and `ports/presto/lander.py` is installed as
`/presto_lander.py`.  The Presto launcher (`/main.py`) adds every
`*.py` in the filesystem root aside from itself and `/secrets.py`
to the rotating menu, so `/presto_lander.py` can't be `*.mpy`
(though everything else likely can).  You may need to add
`"image": "\ue3f4"` to the `icons` mapping in `/main.py` if the
icon isn't shown.
