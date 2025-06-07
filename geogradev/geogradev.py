"""Main module."""

import ipyleaflet


class Map(ipyleaflet.Map):
    """Custom Map class that extends ipyleaflet.Map."""

    def __init__(self, center=[20, 0], zoom=2, **kwargs):
        """Initialize the Map with custom settings."""
        super().__init__(center=center, zoom=zoom, **kwargs)
