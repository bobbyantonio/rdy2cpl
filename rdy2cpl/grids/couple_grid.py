import logging
from pathlib import Path

import yaml

from rdy2cpl.grids.base.ifs import (
    F128,
    N32,
    N80,
    N128,
    N160,
    N200,
    N256,
    O96,
    O160,
    O200,
    O320,
    O400,
    O1280,
)
from rdy2cpl.grids.base.nemo.orca import OrcaTGrid, OrcaUGrid, OrcaVGrid
from rdy2cpl.grids.base.regular import EquidistantLatLonGrid
from rdy2cpl.grids.mask_modifiers import (
    invert_mask,
    mask_box,
    oifs_read_mask,
    rnfm_read_mask,
    regular_grid_read_mask
)
from rdy2cpl.loader import _import_pyoasis

pyoasis = _import_pyoasis()

_log = logging.getLogger(__name__)

_base_grids = {
    bg.__name__: bg
    for bg in (
        EquidistantLatLonGrid,
        OrcaTGrid,
        OrcaUGrid,
        OrcaVGrid,
        F128,
        N32,
        N80,
        N128,
        N160,
        N200,
        N256,
        O96,
        O160,
        O200,
        O320,
        O400,
        O1280,
    )
}

_mask_modifiers = {
    f.__name__: f for f in (invert_mask, mask_box, oifs_read_mask, rnfm_read_mask, regular_grid_read_mask)
}

_default_model_spec_file = Path(__file__).parent / "model_specs/ecearth.yml"
_model_spec = None


class CoupleGrid:
    def __init__(self, base, name) -> None:
        self.base = base
        self.name = name
        self.partition = pyoasis.SerialPartition(self.base.size)

    def write(self):
        oas_grid = pyoasis.Grid(
            self.name,
            *self.base.shape,
            self.base.center_longitudes,
            self.base.center_latitudes,
        )
        oas_grid.set_corners(self.base.corner_longitudes, self.base.corner_latitudes)
        oas_grid.set_area(self.base.areas)
        oas_grid.set_mask(self.base.mask)
        if hasattr(self.base, "fractions"):
            oas_grid.set_frac(self.base.fractions)
        if hasattr(self.base, "angles"):
            oas_grid.set_angle(self.base.angles)
        oas_grid.write()


def update_model_spec(model_spec_file):
    global _model_spec
    with open(model_spec_file) as f:
        _model_spec = yaml.safe_load(f)


def from_model_spec(name, model_spec_file=_default_model_spec_file):
    global _model_spec
    if _model_spec is None:
        update_model_spec(model_spec_file)

    try:
        couple_grid_spec = _model_spec[name]
    except KeyError as e:
        _log.error(
            f"Couple grid name '{name}' not found in model spec"
            f" (know grid names: {', '.join(_model_spec.keys())})"
        )
        raise e from None

    try:
        base_grid_type = _base_grids[couple_grid_spec["type"]["name"]]
    except KeyError as e:
        _log.error(
            f"Unknown base grid name '{couple_grid_spec['type']['name']}' in model_spec"
        )
        raise e from None

    base_grid = base_grid_type(
        *couple_grid_spec["type"].get("args", ()),
        **couple_grid_spec["type"].get("kwargs", {}),
    )

    for mm in couple_grid_spec.get("mask_modifiers", []):
        try:
            mm_func = _mask_modifiers[mm["name"]]
        except KeyError as e:
            _log.error("Unknown mask modifier function {mm['name']}")
            raise e from None
        mm_func(base_grid, *mm.get("args", ()), **mm.get("kwargs", {}))

    return CoupleGrid(base_grid, name)


if __name__ == "__main__":

    from_model_spec('ILLL', model_spec_file='/perm/ecme4254/repos/rdy2cpl/rdy2cpl/grids/model_specs/test.yml')