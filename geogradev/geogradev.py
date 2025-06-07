"""Main module."""

import ipyleaflet


class Map(ipyleaflet.Map):
    """Custom Map class that extends ipyleaflet.Map."""

    def __init__(self, **kwargs):
        """Initialize the Map with custom settings."""
        super().__init__(**kwargs)
