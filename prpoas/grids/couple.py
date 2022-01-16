import pyoasis


class CoupleGrid:
    def __init__(self, base, name):
        self.base = base
        self.name = name
        self.partition = pyoasis.SerialPartition(self.base.nx * self.base.ny)

    def write(self):
        oas_grid = pyoasis.Grid(
            self.name,
            self.base.nx,
            self.base.ny,
            self.base.cell_longitudes,
            self.base.cell_latitudes,
        )
        oas_grid.set_corners(self.base.corner_longitudes, self.base.corner_latitudes)
        oas_grid.set_area(self.base.areas)
        oas_grid.set_mask(self.base.mask)
        if hasattr(self.base, "fractions"):
            oas_grid.set_frac(self.base.fractions)
        if hasattr(self.base, "angles"):
            oas_grid.set_angle(self.base.angles)
        oas_grid.write()