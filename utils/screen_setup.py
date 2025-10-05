from turtle import Screen

def setup(target_globals=None, screen=None):
    """Expose Screen methods into the provided globals dictionary.

    Returns a tuple (screen, created) where created is True when this
    function constructed the Screen itself (i.e. screen was None on entry).
    """
    created = False
    if screen is None:
        screen = Screen()
        created = True

    if target_globals is None:
        try:
            target_globals = globals()
        except Exception:
            target_globals = {}

    for name in dir(screen):
        attr = getattr(screen, name)
        if callable(attr):
            target_globals[name] = attr

    return screen, created
