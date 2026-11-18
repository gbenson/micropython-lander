if __name__ != "lander":
    import sys
    if "badgeware" in sys.modules:
        from .ports.boards.tufty2350 import main
        main()
