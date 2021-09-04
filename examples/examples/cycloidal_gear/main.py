from cadquery.cq import Workplane
from examples.cycloidal_gear.geometry import generate_geometry
from gaya import api


@api.component
class CycloidalGear:
    def __init__(self) -> None:
        self.dimensions: Workplane = generate_geometry()

    @api.geometry
    def geometry(self) -> Workplane:
        return self.dimensions
