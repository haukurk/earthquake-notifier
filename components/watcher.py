from components.events import Event

class QuakeWatcher:
    """
    Watcher for quakes (for modules)
    """
    def __init__(self):
        self.quakeEvent = Event()

    def quakeOccured(self, entity):
        """
        Trigger function for the event.
        """
        self.quakeEvent(entity)