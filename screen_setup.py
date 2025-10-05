from turtle import Screen

def setup(target_globals=None):
    """Expose Screen methods into the provided globals dictionary.

    If no globals dict is provided, this function will modify the globals() of
    the caller (not recommended). Prefer calling with globals() from the
    module that needs access to turtle/screen functions.
    """
    screen = Screen()
    if target_globals is None:
        try:
            target_globals = globals()
        except Exception:
            target_globals = {}

    for name in dir(screen):
        attr = getattr(screen, name)
        if callable(attr):
            target_globals[name] = attr

    return screen
