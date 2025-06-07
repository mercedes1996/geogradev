"""Main module."""

import intro


class Map(intro.Map):
    def __init__(self, center=(0, 0), zoom=2, **kwargs):
        super().__init__(location=center, zoom_start=zoom, **kwargs)
        intro.LayerControl().add_to(self)
