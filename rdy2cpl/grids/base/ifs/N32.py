from rdy2cpl.grids.base.reduced_gaussian import ReducedGaussianGrid


class N32(ReducedGaussianGrid):
    def __init__(self):
        super().__init__(_lats, _nlons)


_lats = (
    87.8637988392326, 85.0965269883174, 82.3129129478863, 79.5256065726594, 76.7368996803683,
    73.9475151539897, 71.1577520115873, 68.3677561083132, 65.5776070108278, 62.7873517989631,
    59.9970201084913, 57.2066315276432, 54.4161995260862, 51.6257336749382, 48.8352409662506,
    46.0447266311017, 43.2541946653509, 40.463648178115, 37.6730896290453, 34.8825209937735,
    32.091943881744, 29.3013596217627, 26.510769325211, 23.7201739335347, 20.9295742544895,
    18.1389709902393, 15.3483647594915, 12.5577561152307, 9.76714555919557, 6.97653355394863,
    4.18592053318915, 1.3953069108195, -1.3953069108195, -4.18592053318915, -6.97653355394863,
    -9.76714555919557, -12.5577561152307, -15.3483647594915, -18.1389709902393, -20.9295742544895,
    -23.7201739335347, -26.510769325211, -29.3013596217627, -32.091943881744, -34.8825209937735,
    -37.6730896290453, -40.463648178115, -43.2541946653509, -46.0447266311017, -48.8352409662506,
    -51.6257336749382, -54.4161995260862, -57.2066315276432, -59.9970201084913, -62.7873517989631,
    -65.5776070108278, -68.3677561083132, -71.1577520115873, -73.9475151539897, -76.7368996803683,
    -79.5256065726594, -82.3129129478863, -85.0965269883174, -87.8637988392326,
)

_nlons = (
    20, 27, 36, 40, 45, 50, 60, 64, 72, 75,
    80, 90, 90, 96, 100, 108, 108, 120, 120, 120,
    128, 128, 128, 128, 128, 128, 128, 128, 128, 128,
    128, 128, 128, 128, 128, 128, 128, 128, 128, 128,
    128, 128, 128, 128, 120, 120, 120, 108, 108, 100,
    96, 90, 90, 80, 75, 72, 64, 60, 50, 45,
    40, 36, 27, 20,
)